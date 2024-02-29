from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import yaml
import os

from common.pageObjects.client.applicationPage import ApplicationPage


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.get_login_page_loc = os.environ.get('LOGIN_PAGE')

        with open(self.get_login_page_loc, 'r') as f:
            self.my_dict = yaml.safe_load(f)

    def client_login(self, username):
        WebDriverWait(self.driver, 60).until(
            EC.visibility_of_element_located([By.ID, self.my_dict['txtUsername']]))
        self.driver.find_element(By.ID, self.my_dict['txtUsername']).send_keys(username + Keys.INSERT)
        self.enter_password_and_submit()

    def client_login_with_new_password(self, username):
        WebDriverWait(self.driver, 60).until(
            EC.visibility_of_element_located([By.ID, self.my_dict['txtUsername']]))
        self.driver.find_element(By.ID, self.my_dict['txtUsername']).send_keys(username + Keys.INSERT)
        self.driver.find_element(By.CLASS_NAME, self.my_dict['txtPassword']).send_keys('iTouch@1234' + Keys.INSERT)
        self.driver.find_element(By.ID, self.my_dict['btnSecureLogin']).send_keys(Keys.ENTER)

    def client_re_login_with_changed_password(self, username):
        self.client_login_with_new_password(username)
        ap = ApplicationPage(self.driver)
        ap.click_personal_information()
        ap.validate_personal_information_under_logged_in_user(username)

    def enter_password_and_submit(self):
        WebDriverWait(self.driver, 60).until(
            EC.visibility_of_element_located([By.CLASS_NAME, self.my_dict['txtPassword']]))
        self.driver.find_element(By.CLASS_NAME, self.my_dict['txtPassword']).send_keys(os.environ.get('CLIENT_PASSWORD')
                                                                                       + Keys.INSERT)
        self.driver.find_element(By.ID, self.my_dict['btnSecureLogin']).send_keys(Keys.ENTER)

    def admin_login(self, username, password):
        self.driver.find_element(By.CSS_SELECTOR, self.my_dict['txtAdminUsername']).send_keys(username + Keys.INSERT)
        self.driver.find_element(By.CSS_SELECTOR, self.my_dict['txtAdminPassword']).send_keys(password + Keys.INSERT)
        self.driver.find_element(By.CSS_SELECTOR, self.my_dict['btnLogin']).send_keys(Keys.ENTER)
