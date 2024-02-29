import os.path
import yaml

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from common.api.registration.getEmailVerificationApi import EmailVerificationApi


class ChangeEmailPage:

    def __init__(self, driver):
        self.driver = driver
        self.get_change_email_page_loc = os.environ.get('CHANGE_EMAIL_PAGE')

        with open(self.get_change_email_page_loc, 'r') as f:
            self.my_dict = yaml.safe_load(f)

    def submit_change_email(self, changed_email):
        self.driver.find_element(By.ID, self.my_dict['txtNewEmail']).send_keys(changed_email + Keys.INSERT)
        self.driver.find_element(By.ID, self.my_dict['txtConfirmEmail']).send_keys(changed_email + Keys.INSERT)
        self.driver.find_element(By.ID, self.my_dict['btnSubmit']).click()

    def verify_email_with_otp(self):
        self.driver.find_element(By.ID, self.my_dict['txtOneTimePassword']).send_keys(os.environ.get('OTP') + Keys.INSERT)
        self.driver.find_element(By.ID, self.my_dict['btnVerify']).click()
        EmailVerificationApi.confirm_email()
        try:
            confirm_popup = self.driver.find_element(By.XPATH, "/html/body/div[5]/div/div[3]/button[1]")
            if confirm_popup.is_displayed():
                confirm_popup.click()
        except TypeError:
            print("Element not found")

    def validate_if_user_able_to_change_email(self, changed_email):
        self.submit_change_email(changed_email)
        self.verify_email_with_otp()
