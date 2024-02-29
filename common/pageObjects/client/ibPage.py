import time

import yaml
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class IBPage:

    def __init__(self, driver):
        self.driver = driver
        self.get_ib_page_loc = os.environ.get('IB_PAGE')

        with open(self.get_ib_page_loc, 'r') as f:
            self.my_dict = yaml.safe_load(f)

    def click_ib(self):
        ib = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable([By.CLASS_NAME, self.my_dict['lnkIb']]))
        ib.click()

    def click_register_clients(self):
        register_clients = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable([By.CLASS_NAME, self.my_dict['lnkRegisterClients']]))
        register_clients.click()

    def navigate_to_register_clients(self):
        self.click_ib()
        self.click_register_clients()

    def submit_register_clients(self, client_email):
        self.navigate_to_register_clients()
        new_email = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located([By.ID, self.my_dict['txtNewEmail']]))
        new_email.send_keys(client_email + Keys.INSERT)
        self.driver.find_element(By.ID, self.my_dict['txtConfirmEmail']).send_keys(client_email + Keys.INSERT)
        self.driver.find_element(By.ID, self.my_dict['btnSubmit']).click()
