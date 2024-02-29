import yaml
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginValidation:

    def __init__(self, driver):
        self.driver = driver
        self.get_login_loc = os.environ.get('LOGIN_PAGE')

        self.get_app_page_loc = os.environ.get('APPLICATION_PAGE')

        with open(self.get_login_loc, 'r') as f:
            self.my_dict = yaml.safe_load(f)

        with open(self.get_app_page_loc, 'r') as f:
            self.my_dict1 = yaml.safe_load(f)

    def validate_if_user_able_to_logout(self):
        login = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located([By.ID, self.my_dict['txtUsername']]))
        if login.is_displayed():
            assert True
        else:
            assert False

    def validate_if_user_able_to_re_login_with_changed_email(self, changed_email):
        actual_changed_email = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located([By.ID, self.my_dict1['lblUsername']]))
        actual_changed_email = actual_changed_email.text
        if actual_changed_email != changed_email:
            assert False
        else:
            assert True

