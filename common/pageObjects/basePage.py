import allure

from selenium import webdriver
from allure_commons.types import AttachmentType
from selenium.common.exceptions import WebDriverException


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def attach_screenshot(self, test):
        allure.attach(self.driver.get_screenshot_as_png(), name=test + " Page Screenshot",
                      attachment_type=AttachmentType.PNG)

    @staticmethod
    def select_browser(browser_type):
        if browser_type == 'firefox':
            return webdriver.Firefox()
        elif browser_type == 'edge':
            return webdriver.Edge()
        elif browser_type == 'chrome':
            return webdriver.Chrome()
        else:
            raise WebDriverException
