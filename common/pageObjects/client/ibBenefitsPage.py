import yaml
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class IBBenefitsPage:

    def __init__(self, driver):
        self.driver = driver
        self.get_ib_benefits_page_loc = os.environ.get('IB_BENEFITS_PAGE')

        with open(self.get_ib_benefits_page_loc, 'r') as f:
            self.my_dict = yaml.safe_load(f)

    def is_ib_benefits_page_displayed(self):
        self.driver.find_element(By.CLASS_NAME, self.my_dict['lnkIbBenefits']).click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located([
            By.CLASS_NAME, self.my_dict['lblIntroducingBrokerBenefits']]))
        return self.driver.find_element(By.CLASS_NAME, self.my_dict['lblIntroducingBrokerBenefits']).text
