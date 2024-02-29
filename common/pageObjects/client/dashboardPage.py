import yaml
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage:

    def __init__(self, driver):
        self.driver = driver
        self.get_dashboard_page_loc = os.environ.get('DASHBOARD_PAGE')

        with open(self.get_dashboard_page_loc, 'r') as f:
            self.my_dict = yaml.safe_load(f)

    def is_dashboard_page_displayed(self):
        WebDriverWait(self.driver, 40).until(EC.text_to_be_present_in_element([
            By.CSS_SELECTOR, self.my_dict['lblDashboard']], 'Dashboard'))
        dashboard_text = self.driver.find_element(By.CSS_SELECTOR, self.my_dict['lblDashboard']).text
        return dashboard_text
