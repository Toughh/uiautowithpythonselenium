import yaml
import os

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.commonFunctions import CommonFunctions
from common.data.admin.complianceArea.complianceRealUsersData import ComplianceRealUsersData
from common.enum.admin.complianceArea.complianceRealUsers.compStatusType import CompStatusType
from common.helper.getWebTableData import GetWebTableData
from common.pageObjects.admin.backOfficeAreaPage import BackOfficeAreaPage
from common.validations.validateAdminComplianceArea import AdminComplianceAreaValidation


class ComplianceAreaPage:

    def __init__(self, driver):
        self.driver = driver
        self.get_compliance_area_page_loc = os.environ.get('COMPLIANCE_AREA_PAGE')
        with open(self.get_compliance_area_page_loc, 'r') as f:
            self.my_dict = yaml.safe_load(f)
        self.get_back_office_area_page_loc = os.environ.get('BACK_OFFICE_AREA_PAGE')
        with open(self.get_back_office_area_page_loc, 'r') as f:
            self.my_dict1 = yaml.safe_load(f)

    def compliance_area(self):
        try:
            self.driver.find_element(By.CLASS_NAME, self.my_dict['lnkComplianceArea']).click()
        except NoSuchElementException:
            print("No Such Element found in the web page!!!")

    def compliance_real_users(self):
        try:
            compliance_real_users = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located([By.CLASS_NAME, self.my_dict['lnkComplianceRealUsers']]))
            compliance_real_users.click()
        except NoSuchElementException:
            print("No Such Element found in the web page!!!")

    def rejected_applications(self):
        try:
            self.driver.find_element(By.CLASS_NAME, self.my_dict['lnkRejectedApplications']).click()
        except NoSuchElementException:
            print("No Such Element found in the web page!!!")

    def navigate_to_compliance_real_users(self, username):
        self.compliance_area()
        self.compliance_real_users()
        self.search_by_email_id(username)

    def select_client_risk(self, compliance_real_users):
        client_risk = self.driver.find_element(By.ID, self.my_dict['ddSelectClientRisk'])
        self.driver.execute_script(CommonFunctions.set_admin_element_attribute('s554d599b97_clientRisk'), client_risk)
        CommonFunctions.select_values(client_risk, compliance_real_users.get_client_risk())

    def select_client_categorization(self, compliance_real_users):
        client_categorization = self.driver.find_element(By.ID, self.my_dict['ddSelectClientCategorization'])
        self.driver.execute_script(CommonFunctions.set_admin_element_attribute('s554d599b97_clientCategorization'), client_categorization)
        CommonFunctions.select_values(client_categorization, compliance_real_users.get_client_categorization())

    def select_id_expiration_month(self, compliance_real_users):
        id_exp_month = self.driver.find_element(By.ID, self.my_dict['ddSelectIdExpirationMonth'])
        self.driver.execute_script(CommonFunctions.set_admin_element_attribute('s554d599b97_PortalUser__idExpirationDate_month'), id_exp_month)
        CommonFunctions.select_values(id_exp_month, compliance_real_users.get_id_exp_date_month())

    def select_id_expiration_day(self, compliance_real_users):
        id_exp_day = self.driver.find_element(By.ID, self.my_dict['ddSelectIdExpirationDay'])
        self.driver.execute_script(CommonFunctions.set_admin_element_attribute('s554d599b97_PortalUser__idExpirationDate_day'), id_exp_day)
        CommonFunctions.select_values(id_exp_day, compliance_real_users.get_id_exp_date_day())

    def select_id_expiration_year(self, compliance_real_users):
        id_exp_year = self.driver.find_element(By.ID, self.my_dict['ddSelectIdExpirationYear'])
        self.driver.execute_script(CommonFunctions.set_admin_element_attribute('s554d599b97_PortalUser__idExpirationDate_year'), id_exp_year)
        CommonFunctions.select_values(id_exp_year, compliance_real_users.get_id_exp_date_year())

    def select_id_exp_date(self, compliance_real_users):
        self.select_id_expiration_month(compliance_real_users)
        self.select_id_expiration_day(compliance_real_users)
        self.select_id_expiration_year(compliance_real_users)

    def select_por_expiration_month(self, compliance_real_users):
        por_exp_month = self.driver.find_element(By.ID, self.my_dict['ddSelectPorExpirationMonth'])
        self.driver.execute_script(CommonFunctions.set_admin_element_attribute('s554d599b97_PortalUser__porExpirationDate_month'), por_exp_month)
        CommonFunctions.select_values(por_exp_month, compliance_real_users.get_por_exp_date_month())

    def select_por_expiration_day(self, compliance_real_users):
        por_exp_day = self.driver.find_element(By.ID, self.my_dict['ddSelectPorExpirationDay'])
        self.driver.execute_script(CommonFunctions.set_admin_element_attribute('s554d599b97_PortalUser__porExpirationDate_day'), por_exp_day)
        CommonFunctions.select_values(por_exp_day, compliance_real_users.get_por_exp_date_day())

    def select_por_expiration_year(self, compliance_real_users):
        por_exp_year = self.driver.find_element(By.ID, self.my_dict['ddSelectPorExpirationYear'])
        self.driver.execute_script(CommonFunctions.set_admin_element_attribute('s554d599b97_PortalUser__porExpirationDate_year'), por_exp_year)
        CommonFunctions.select_values(por_exp_year, compliance_real_users.get_por_exp_date_year())

    def select_por_exp_date(self, compliance_real_users):
        self.select_por_expiration_month(compliance_real_users)
        self.select_por_expiration_day(compliance_real_users)
        self.select_por_expiration_year(compliance_real_users)

    def select_comp_id_status(self, compliance_real_users):
        comp_id_status = self.driver.find_element(By.ID, self.my_dict['ddSelectCompIdStatus'])
        self.driver.execute_script(CommonFunctions.set_admin_element_attribute('s554d599b97_PortalUser__compIdStatus'), comp_id_status)
        CommonFunctions.select_values(comp_id_status, compliance_real_users.get_comp_id_status())

    def select_comp_por_status(self, compliance_real_users):
        comp_por_status = self.driver.find_element(By.ID, self.my_dict['ddSelectCompPorStatus'])
        self.driver.execute_script(CommonFunctions.set_admin_element_attribute('s554d599b97_PortalUser__compPorStatus'), comp_por_status)
        CommonFunctions.select_values(comp_por_status, compliance_real_users.get_comp_por_status())

    def note_comp(self, compliance_real_users):
        note = self.driver.find_element(By.ID, self.my_dict['txtNoteComp'])
        note.clear()
        note.send_keys(compliance_real_users.get_note_comp() + Keys.INSERT)

    def user_docs_upload(self, compliance_real_users):
        click_to_upload = self.driver.find_element(By.XPATH, self.my_dict['lnkExtraDocuments'])
        self.driver.execute_script("arguments[0].click();", click_to_upload)
        self.driver.find_element(By.CSS_SELECTOR, self.my_dict['txtDocumentName']).send_keys(
            compliance_real_users.get_document_name() + Keys.INSERT)
        # choose_file = self.driver.find_element(By.CSS_SELECTOR, self.my_dict['btnChooseFile'])
        # self.driver.execute_script("arguments[0].click();", choose_file)
        # compliance_real_users.get_user_documents()

    def set_compliance_real_users_details(self, compliance_real_users):
        self.select_client_risk(compliance_real_users)
        self.select_client_categorization(compliance_real_users)
        self.select_id_exp_date(compliance_real_users)
        self.select_por_exp_date(compliance_real_users)
        self.select_comp_id_status(compliance_real_users)
        self.select_comp_por_status(compliance_real_users)
        self.note_comp(compliance_real_users)
        # self.user_docs_upload(compliance_real_users)

    def fill_compliance_real_users_details(self, compliance_real_users):
        self.set_compliance_real_users_details(compliance_real_users)
        self.click_update()

    def search_by_email_id(self, username):
        email = self.driver.find_element(By.CLASS_NAME, self.my_dict['lblUsernameEmail'])
        email.clear()
        email.send_keys(username + Keys.INSERT)
        self.driver.find_element(By.CLASS_NAME, self.my_dict['btnFilter']).click()

    def search_by_rejected_email_id(self, username):
        email = self.driver.find_element(By.CLASS_NAME, self.my_dict['lblUsernameEmailRejected'])
        email.clear()
        email.send_keys(username + Keys.INSERT)
        self.driver.find_element(By.CLASS_NAME, self.my_dict['btnFilterRejected']).click()

    def search_by_id(self):
        self.driver.find_element(By.XPATH, self.my_dict['lnkId']).click()

    def check_if_back_office_area_is_in_expand_mode(self):
        try:
            expand_menu = self.driver.find_element(By.CLASS_NAME, self.my_dict1['lnkRealAccounts'])
            if expand_menu.is_displayed():
                backoffice_area = self.driver.find_element(By.CLASS_NAME, self.my_dict1['lnkBackofficeArea'])
                self.driver.execute_script("arguments[0].click();", backoffice_area)
        except NoSuchElementException:
            print("NoSuchElementException")

    def validate_change_compliance_id_status(self, username, compliance_id_status, comp_id_status, comp_por_status):
        self.check_if_back_office_area_is_in_expand_mode()
        self.navigate_to_compliance_real_users(username)
        self.search_by_id()
        if compliance_id_status == 'Approve':
            return ComplianceAreaPage.approve_compliance_id(self, username, compliance_id_status, comp_id_status, comp_por_status)
        else:
            return ComplianceAreaPage.reject_compliance_id(self, username, compliance_id_status, comp_id_status, comp_por_status)

    def validate_change_ic_campaign_compliance_id_status(self, username, compliance_id_status, comp_id_status, comp_por_status):
        self.check_if_back_office_area_is_in_expand_mode()
        self.navigate_to_compliance_real_users(username)
        self.search_by_id()
        if compliance_id_status == 'Approve':
            return ComplianceAreaPage.approve_ic_campaign_compliance_id(self, username, compliance_id_status, comp_id_status, comp_por_status)
        else:
            return ComplianceAreaPage.reject_ic_campaign_compliance_id(self, username, compliance_id_status, comp_id_status, comp_por_status)

    @staticmethod
    def comp_status(compliance_status):
        try:
            if compliance_status == 'Approve':
                return CompStatusType.approved.value
            elif compliance_status == 'Reject':
                return CompStatusType.reject.value
            elif compliance_status == 'Pending':
                return CompStatusType.pending.value
            elif compliance_status == 'Unverified Account':
                return CompStatusType.unverified_account.value
        except Exception as exc:
            ...
            raise RuntimeError("Selected Compliance Id status not found!!!") from exc

    def check_compliance_status_under_compliance_real_users(self, username, compliance_id_status, comp_id_status, comp_por_status):
        self.driver.find_element(By.XPATH, self.my_dict['lnkApproveApplication']).click()
        compliance_real_users_data = ComplianceRealUsersData.compliance_real_users(
            self.comp_status(comp_id_status), self.comp_status(comp_por_status))
        self.fill_compliance_real_users_details(compliance_real_users_data)
        self.compliance_real_users()
        self.search_by_email_id(username)
        validate_compliance_id = AdminComplianceAreaValidation(self.driver)
        validate_compliance_id.validate_admin_compliance_status_matches_records_in_db(compliance_id_status, comp_id_status, comp_por_status)

    def check_compliance_status_under_real_accounts(self, username):
        bo = BackOfficeAreaPage(self.driver)
        bo.navigate_to_real_account(username)
        compliance_status = (self.driver.find_element(
            By.XPATH, GetWebTableData.get_cols_data(self.my_dict1['tblRealAccounts'], 1, 11))).text
        return compliance_status

    def check_compliance_status_under_campaign_accounts(self, username):
        bo = BackOfficeAreaPage(self.driver)
        bo.navigate_to_campaign_account(username)
        compliance_status = (self.driver.find_element(
            By.XPATH, GetWebTableData.get_cols_data(self.my_dict1['tblCampaignAccounts'], 1, 11))).text
        return compliance_status

    def select_reject_compliance_reason(self):
        missing_documents = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable([By.XPATH, self.my_dict['lnkMissingDocuments']]))
        missing_documents.click()
        self.driver.find_element(By.XPATH, '//*[@id="RejectApplication_predefined_reasons"]/div[1]/label').click()
        self.driver.find_element(By.ID, self.my_dict['txtOtherReason']). \
            send_keys('Not in a mood to approve. Testing Purpose.' + Keys.INSERT)
        return self.driver.find_element(By.XPATH, self.my_dict['cbNotifyClient']).click()

    def click_update(self):
        update = self.driver.find_element(By.XPATH, self.my_dict['btnUpdate'])
        self.driver.execute_script("arguments[0].click();", update)

    def check_compliance_status_under_rejected_applications(self, username, compliance_id_status, comp_id_status, comp_por_status):
        self.select_reject_compliance_reason()
        self.click_update()
        self.rejected_applications()
        self.search_by_rejected_email_id(username)
        validate_compliance_id = AdminComplianceAreaValidation(self.driver)
        validate_compliance_id.validate_admin_compliance_status_matches_records_in_db(compliance_id_status, comp_id_status, comp_por_status)

    def approve_compliance_id(self, username, compliance_id_status, comp_id_status, comp_por_status):
        return self.check_compliance_status_under_compliance_real_users(username, compliance_id_status, comp_id_status, comp_por_status), \
               self.check_compliance_status_under_real_accounts(username)

    def approve_ic_campaign_compliance_id(self, username, compliance_id_status, comp_id_status, comp_por_status):
        return self.check_compliance_status_under_compliance_real_users(username, compliance_id_status, comp_id_status, comp_por_status), \
                self.check_compliance_status_under_campaign_accounts(username)

    def reject_compliance_id(self, username, compliance_id_status, comp_id_status, comp_por_status):
        return self.check_compliance_status_under_rejected_applications(username, compliance_id_status, comp_id_status, comp_por_status), \
               self.check_compliance_status_under_real_accounts(username)

    def reject_ic_campaign_compliance_id(self, username, compliance_id_status, comp_id_status, comp_por_status):
        return self.check_compliance_status_under_rejected_applications(username, compliance_id_status, comp_id_status, comp_por_status), \
               self.check_compliance_status_under_campaign_accounts(username)

    def enter_trading_accounts(self, text):
        trading_accounts = self.driver.find_element(By.CLASS_NAME, self.my_dict['txtTradingAccounts']).send_keys(
            text + Keys.INSERT)
        return trading_accounts

    def select_compliance_status(self, status):
        compliance_status = self.driver.find_element(By.ID, self.my_dict['ddComplianceStatus'])
        self.driver.execute_script(CommonFunctions.set_admin_element_attribute('filter_compStatus_value'), compliance_status)
        CommonFunctions.select_values(self.driver.find_element(By.ID, self.my_dict['ddSelectComplianceStatus']), status)
