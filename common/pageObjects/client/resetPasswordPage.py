import os.path
import yaml

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class ResetPasswordPage:

    def __init__(self, driver):
        self.driver = driver
        self.get_reset_password_page_loc = os.environ.get('RESET_PASSWORD_PAGE')

        with open(self.get_reset_password_page_loc, 'r') as f:
            self.my_dict = yaml.safe_load(f)

    def submit_reset_password(self):
        self.driver.find_element(By.ID, self.my_dict['txtCurrentPassword']).send_keys(os.environ.get('CLIENT_PASSWORD') + Keys.INSERT)
        self.driver.find_element(By.ID, self.my_dict['txtNewPassword']).send_keys('iTouch@1234' + Keys.INSERT)
        self.driver.find_element(By.ID, self.my_dict['txtConfirmPassword']).send_keys('iTouch@1234' + Keys.INSERT)
        self.driver.find_element(By.ID, self.my_dict['btnResetPasswordSubmit']).click()

    def submit_reset_trading_password(self):
        self.driver.find_element(By.XPATH, self.my_dict['btnTradingAccountSendOtp']).click()
        self.driver.find_element(By.ID, self.my_dict['txtEmailVerificationCode']).send_keys(os.environ.get('OTP') + Keys.INSERT)
        self.driver.find_element(By.ID, self.my_dict['txtNewPassword']).send_keys('iTouch@1234' + Keys.INSERT)
        self.driver.find_element(By.ID, self.my_dict['txtConfirmPassword']).send_keys('iTouch@1234' + Keys.INSERT)
        self.driver.find_element(By.CSS_SELECTOR, self.my_dict['btnTradingAccountSubmit']).click()

    def validate_if_able_to_reset_password(self):
        self.submit_reset_password()

    def validate_if_able_to_reset_trading_password(self):
        self.submit_reset_trading_password()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located([By.CSS_SELECTOR, self.my_dict['txtAlertSuccessMes']]))
