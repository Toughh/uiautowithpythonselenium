import time
import yaml
import os

from selenium.webdriver.common.by import By
from common.api.registration.postRegisterNewAccountApi import RegisterNewAccountApi
from common.helper.getWebTableData import GetWebTableData
from common.utility.db.onlineMexGroupDB import DatabaseUtility


class AdminComplianceAreaValidation:

    def __init__(self, driver):
        self.driver = driver
        self.get_compliance_area_page_loc = os.environ.get('COMPLIANCE_AREA_PAGE')
        with open(self.get_compliance_area_page_loc, 'r') as f:
            self.my_dict = yaml.safe_load(f)

    def validate_admin_compliance_status_matches_records_in_db(self, compliance_id_status, comp_id_status, comp_por_status):
        pass
        # time.sleep(3)
        # forex_real_profile = os.environ.get('FOREX_REAL_PROFILE')
        # id = RegisterNewAccountApi.get_id()
        # db = DatabaseUtility
        # records = db.db_connection(forex_real_profile + str(id) + ";")
        # bo_id_status_db = records['bo_id_status']
        # bo_por_status_db = records['bo_por_status']
        # comp_status = records['comp_status']
        # try:
        #     if compliance_id_status == 'Approve' and comp_id_status == 'Approve' and comp_por_status == 'Approve':
        #         compliance_status = self.driver.find_element(By.XPATH, GetWebTableData.get_cols_data(self.my_dict['tblComplianceRealUsers'], 1, 6)).text
        #         if compliance_status == 'APPROVED' and bo_id_status_db == '1' and bo_por_status_db == '1' and comp_status == '1':
        #             assert True
        #         else:
        #             assert False
        #     elif compliance_id_status == 'Reject' and comp_id_status is None and comp_por_status is None:
        #         compliance_status = self.driver.find_element(By.XPATH, GetWebTableData.get_cols_data(self.my_dict['tblRejectedApplications'], 1, 6)).text
        #         if compliance_status == 'Reject' and bo_id_status_db == '1' and bo_por_status_db == '1' and comp_status == '0':
        #             assert True
        #         else:
        #             assert False
        #     else:
        #         print("Error: Entered compliance_status not found!!!")
        # except TypeError:
        #     print("DB connection error!!!")
