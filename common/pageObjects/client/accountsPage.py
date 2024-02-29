import os.path
import yaml

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from common.validations.validateClientAccounts import ClientAccountsValidation


class AccountsPage:

    def __init__(self, driver):
        self.driver = driver
        self.get_accounts_page_loc = os.environ.get('ACCOUNTS_PAGE')

        with open(self.get_accounts_page_loc, 'r') as f:
            self.my_dict = yaml.safe_load(f)

    def click_accounts(self):
        accounts = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located([By.CLASS_NAME, self.my_dict['lnkAccounts']]))
        accounts.click()

    def navigate_to_live_accounts(self):
        self.click_accounts()
        self.driver.find_element(By.CLASS_NAME, self.my_dict['lnkLiveAccounts']).click()

    def navigate_to_demo_accounts(self):
        self.click_accounts()
        demo = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located([By.CLASS_NAME, self.my_dict['lnkDemoAccounts']]))
        demo.click()

    def get_trading_card_info(self):
        self.navigate_to_live_accounts()
        cl_trading_account_number = self.driver.find_element(By.CLASS_NAME, self.my_dict['lblTradingAccountNumber']).text
        cl_currency = self.driver.find_element(By.CLASS_NAME, self.my_dict['lblTradingAccountCurrency']).text
        return [cl_trading_account_number, cl_currency]

    def validate_live_accounts_records_in_db(self, username):
        vca = ClientAccountsValidation(self.driver)
        vca.validate_live_accounts_trading_card_details_in_db(username)

    def validate_demo_accounts_records_in_db(self, username):
        vca = ClientAccountsValidation(self.driver)
        vca.validate_demo_accounts_trading_card_details_in_db(username)

    def open_live_account(self):
        open_live_account = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located([By.XPATH, self.my_dict['lnkOpenLiveAccount']]))
        open_application = open_live_account.click()
        return open_application
