import os
import time

from common.api.registration.getEmailVerificationApi import EmailVerificationApi
from common.api.registration.postRegisterNewAccountApi import RegisterNewAccountApi
from common.data.api.dataSet.registration.registrationData import RegistrationData
from common.pageObjects.client.loginPage import LoginPage
from common.pageObjects.client.setPasswordPage import SetPasswordPage
from common.pageObjects.basePage import BasePage


class SetupPage:

    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def browser_select():
        browser_type = os.environ.get('BROWSER')
        return BasePage.select_browser(browser_type)

    def ic_setup_with_trading_accounts_settings(self, username):
        RegisterNewAccountApi.register_ic_user(username)
        # set_password_url = RegisterNewAccountApi.get_set_password_url()
        login_to_client_app = RegisterNewAccountApi.get_verification_dev()
        RegisterNewAccountApi.add_trading_account()
        self.driver = self.browser_select()
        self.driver.get(login_to_client_app)
        self.driver.maximize_window()
        # self.driver.get(set_password_url)
        # sp = SetPasswordPage(self.driver)
        # sp.set_password()
        # self.login_to_client_application()
        return self.driver

    def ic_setup_without_trading_accounts_settings(self, username):
        RegisterNewAccountApi.register_ic_user(username)
        set_password_url = RegisterNewAccountApi.get_set_password_url()
        login_to_client_app = RegisterNewAccountApi.get_verification_dev()
        self.driver = self.browser_select()
        self.driver.get(set_password_url)
        sp = SetPasswordPage(self.driver)
        sp.set_password()
        self.driver.get(login_to_client_app)
        self.login_to_client_application()
        return self.driver

    def ic_duplicate_setup_without_trading_account_settings(self, username):
        RegisterNewAccountApi.register_ic_user(username)
        login_to_client_app = RegisterNewAccountApi.get_verification_dev()
        self.driver = self.browser_select()
        self.driver.get(login_to_client_app)
        self.driver.maximize_window()
        sp = SetPasswordPage(self.driver)
        sp.set_password()
        return self.driver

    def ib_setup(self, username):
        RegisterNewAccountApi.register_ib_user(username)
        # set_password_url = RegisterNewAccountApi.get_ib_set_password_url()
        login_to_client_app = RegisterNewAccountApi.get_verification_dev()
        self.driver = self.browser_select()
        # self.driver.get(set_password_url)
        # sp = SetPasswordPage(self.driver)
        # sp.set_password()
        self.driver.get(login_to_client_app)
        self.driver.maximize_window()
        # login = self.login_to_client_application()
        return self.driver

    def ic_campaign_setup_with_trading_account_settings(self, username):
        EmailVerificationApi.get_email_verified_for_ic_campaign_user(username)
        login = RegisterNewAccountApi.get_set_password_url()
        self.driver = self.browser_select()
        self.driver.get(login)
        self.driver.maximize_window()
        return self.driver

    def ic_campaign_setup_without_trading_account_settings(self, username):
        EmailVerificationApi.get_email_verified_for_ic_campaign_user_without_trading_account(username)
        login = RegisterNewAccountApi.get_set_password_url()
        self.driver = self.browser_select()
        self.driver.get(login)
        self.driver.maximize_window()
        return self.driver

    def demo_setup(self, username):
        demo_registration = RegistrationData.register_demo_user(username)
        RegisterNewAccountApi.get_register_new_account_res(demo_registration)
        login_to_client_app = RegisterNewAccountApi.get_verification_dev()
        self.driver = self.browser_select()
        self.driver.get(login_to_client_app)
        self.driver.maximize_window()
        sp = SetPasswordPage(self.driver)
        sp.set_password()
        return self.driver

    def login_to_client_application(self):
        self.driver.maximize_window()
        login = LoginPage(self.driver)
        login.enter_password_and_submit()
        return self.driver

    def admin_setup(self):
        self.driver = self.browser_select()
        self.driver.get(os.environ.get('ADMIN_URL'))
        self.driver.maximize_window()
        return self.driver

    def client_setup(self):
        self.driver = self.browser_select()
        self.driver.get(os.environ.get('CLIENT_URL'))
        self.driver.maximize_window()
        return self.driver

    def teardown(self):
        self.driver.quit()
