import time

import yaml
import os

from selenium.webdriver.common.by import By
from common.api.registration.postRegisterNewAccountApi import RegisterNewAccountApi
from common.utility.db.onlineMexGroupDB import DatabaseUtility


class AdminBackOfficeAreaValidation:

    def __init__(self, driver):
        self.driver = driver
        self.get_back_office_area_page_loc = os.environ.get('BACK_OFFICE_AREA_PAGE')
        with open(self.get_back_office_area_page_loc, 'r') as f:
            self.my_dict = yaml.safe_load(f)

    def validate_admin_bo_id_por_status_matches_records_in_db(self, bo_id_status, bo_por_status):
        pass
        # time.sleep(2)
        # forex_real_profile = os.environ.get('FOREX_REAL_PROFILE')
        # id = RegisterNewAccountApi.get_id()
        # db = DatabaseUtility
        # records = db.db_connection(forex_real_profile + str(id) + ";")
        # bo_id_status_db = records['bo_id_status']
        # bo_por_status_db = records['bo_por_status']
        # try:
        #     if bo_id_status == 'Approve' and bo_por_status is None:
        #         bo_id_approved = self.driver.find_element(By.CSS_SELECTOR, self.my_dict['lblBOIdApproved']).text
        #         if bo_id_approved == 'APPROVED' and bo_id_status_db == '1' and bo_por_status_db == '2':
        #             assert True
        #         else:
        #             assert False
        #     elif bo_id_status == 'Reject' and bo_por_status is None:
        #         bo_id_reject = self.driver.find_element(By.CSS_SELECTOR, self.my_dict['lblBOIdOrPORReject']).text
        #         if bo_id_reject == 'REJECT' and bo_id_status_db == '0' and bo_por_status_db == '2':
        #             assert True
        #         else:
        #             assert False
        #     elif bo_id_status == 'Approve' and bo_por_status == 'Approve':
        #         bo_id_approved = self.driver.find_element(By.CSS_SELECTOR, self.my_dict['lblBOIdApproved']).text
        #         if bo_id_approved == 'APPROVED' and bo_id_status_db == '1' and bo_por_status_db == '1':
        #             assert True
        #         else:
        #             assert False
        #     elif bo_id_status == 'Approve' and bo_por_status == 'Reject':
        #         bo_id_reject = self.driver.find_element(By.CSS_SELECTOR, self.my_dict['lblBOIdOrPORReject']).text
        #         if bo_id_reject == 'REJECT' and bo_id_status_db == '1' and bo_por_status_db == '0':
        #             assert True
        #         else:
        #             assert False
        #     else:
        #         print("Error: bo_id_status and bo_por_status combination not found!!!")
        # except TypeError:
        #     print("DB connection error!!!")
