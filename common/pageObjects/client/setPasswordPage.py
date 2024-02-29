import yaml
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SetPasswordPage:

    def __init__(self, driver):
        self.driver = driver
        self.get_set_password_page_loc = os.environ.get('SET_PASSWORD_PAGE')

        with open(self.get_set_password_page_loc, 'r') as f:
            self.data = yaml.safe_load(f)

    def enter_password(self):
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located([By.CLASS_NAME, self.data['txtSetPassword']]))
        return self.driver.find_element(By.CLASS_NAME, self.data['txtSetPassword']).send_keys(os.environ.get('CLIENT_PASSWORD') + Keys.INSERT)

    def enter_confirm_password(self):
        return self.driver.find_element(By.CLASS_NAME, self.data['txtConfirmPassword']).send_keys(os.environ.get('CLIENT_PASSWORD') + Keys.INSERT)

    def submit(self):
        proceed = self.driver.find_element(By.ID, self.data['btnProceed'])
        return self.driver.execute_script("arguments[0].click();", proceed)

    def enter_password_and_submit(self):
        self.enter_password()
        proceed = self.driver.find_element(By.ID, self.data['btnProceed'])
        return self.driver.execute_script("arguments[0].click();", proceed)

    def enter_confirm_password_and_submit(self):
        self.enter_confirm_password()
        proceed = self.driver.find_element(By.ID, self.data['btnProceed'])
        return self.driver.execute_script("arguments[0].click();", proceed)

    def set_password(self):
        self.enter_password()
        self.enter_confirm_password()
        self.submit()
