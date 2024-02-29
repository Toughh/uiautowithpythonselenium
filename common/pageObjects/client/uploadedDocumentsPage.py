import os.path
import time

import yaml

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from common.commonFunctions import CommonFunctions


class UploadedDocumentsPage:

    def __init__(self, driver):
        self.driver = driver
        self.get_uploaded_documents_page_loc = os.environ.get('UPLOADED_DOCUMENTS_PAGE')

        with open(self.get_uploaded_documents_page_loc, 'r') as f:
            self.my_dict = yaml.safe_load(f)

        self.driver = driver
        self.get_app_page_loc = os.environ.get('APPLICATION_PAGE')

        with open(self.get_app_page_loc, 'r') as f:
            self.my_dict1 = yaml.safe_load(f)

    def validate_if_able_to_upload_documents(self, status):
        time.sleep(10)
        self.driver.find_element(By.CLASS_NAME, self.my_dict['btnUploadSelfie']).click()
        if status != "Approve":
            self.validate_user_able_to_upload_documents()
        else:
            self.validate_error_on_trying_to_upload_documents()

    def validate_user_able_to_upload_documents(self):
        filepath = os.environ.get('UPLOAD_FILE')
        filename = filepath + str('fakePassport.jpg')
        CommonFunctions.upload_files(filename)
        ok = WebDriverWait(self.driver, 60).until(
            EC.visibility_of_element_located([By.CLASS_NAME, self.my_dict1['btnOk']]))
        if ok.is_displayed():
            assert True
        else:
            assert False

    def validate_error_on_trying_to_upload_documents(self):
        upload_error_mes = self.driver.find_element(By.CLASS_NAME, self.my_dict['txtUploadError']).text
        if upload_error_mes != "Failed to upload, document already approved. Please contact our support for further assistance":
            assert False
        else:
            assert True

    def validate_user_able_to_see_admin_uploaded_documents(self):
        admin_uploaded_doc = self.driver.find_element(By.ID, self.my_dict['imgUploadAnIdentificationFile']).get_attribute("data-doc")
        if admin_uploaded_doc != '/':
            assert True
        else:
            assert False
