import os
import yaml

from selenium.common.exceptions import NoSuchElementException, InvalidSelectorException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from common.commonFunctions import CommonFunctions
from common.helper.getWebTableData import GetWebTableData
from common.validations.validateAdminBackOfficeArea import AdminBackOfficeAreaValidation


class BackOfficeAreaPage:

    def __init__(self, driver):
        self.driver = driver
        self.get_back_office_area_page_loc = os.environ.get('BACK_OFFICE_AREA_PAGE')
        with open(self.get_back_office_area_page_loc, 'r') as f:
            self.my_dict = yaml.safe_load(f)

    def backoffice_area(self):
        try:
            backoffice_area = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable([By.CLASS_NAME, self.my_dict['lnkBackofficeArea']]))
            backoffice_area.click()
        except InvalidSelectorException:
            print("Invalid Selector - BackOffice Area")

    def real_accounts(self):
        try:
            real_accounts = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable([By.CLASS_NAME, self.my_dict['lnkRealAccounts']]))
            real_accounts.click()
        except InvalidSelectorException:
            print("Invalid Selector - Real Accounts")

    def campaign_accounts(self):
        try:
            campaign_accounts = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located([By.CLASS_NAME, self.my_dict['lnkCampaignAccounts']]))
            campaign_accounts.click()
        except NoSuchElementException:
            print("No Such Element found in the web page!!!")

    def edit_info_requests(self):
        try:
            edit_info_requests = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located([By.XPATH, self.my_dict['lnkEditInfoRequest']]))
            edit_info_requests.click()
        except NoSuchElementException:
            print("No Such Element found in the web page!!!")

    def search_by_email_id(self, username):
        email = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located([By.CLASS_NAME, self.my_dict['txtEmail']]))
        # email = self.driver.find_element(By.CLASS_NAME, self.my_dict['txtEmail'])
        email.clear()
        email.send_keys(username + Keys.INSERT)
        self.driver.find_element(By.CLASS_NAME, self.my_dict['btnFilter']).click()

    def search_by_email_id_campaign(self, username):
        email = self.driver.find_element(By.CLASS_NAME, self.my_dict['txtEmailCampaign'])
        email.clear()
        email.send_keys(username + Keys.INSERT)
        self.driver.find_element(By.CLASS_NAME, self.my_dict['btnFilterCampaign']).click()

    def search_by_email_id_edit_info_request(self, username):
        email = self.driver.find_element(By.ID, self.my_dict['txtEditInfoEmail'])
        email.clear()
        email.send_keys(username + Keys.INSERT)

    def navigate_to_edit_info_requests(self, username):
        self.backoffice_area()
        self.edit_info_requests()
        self.search_by_email_id_edit_info_request(username)

    def edit_info_request_change_status(self, username, status):
        self.navigate_to_edit_info_requests(username)
        self.show_table(self.my_dict['tblEditInfoRequest'])
        self.driver.find_element(By.XPATH, self.my_dict['ddActions']).click()
        if status == "Approve":
            approve = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located([By.XPATH, self.my_dict['ddOptionsApproveAll']]))
            approve.click()
            self.driver.switch_to.alert.accept()
        else:
            reject = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located([By.XPATH, self.my_dict['ddOptionsRejectAll']]))
            reject.click()
            self.driver.switch_to.alert.accept()

    def show_table(self, table_name):
        ids = self.driver.find_element(By.XPATH, GetWebTableData.get_cols_data(table_name, 1, 1))
        ids = ids.text
        self.driver.find_element(By.XPATH, "//*[contains(text(),'" + str(ids) + "')]").click()

    def withdrawal_request(self):
        self.show_table(self.my_dict['tblRealAccounts'])
        self.driver.find_element(By.XPATH, self.my_dict['lnkUserActions']).click()
        withdrawal_request = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable([By.XPATH, self.my_dict['lnkWithdrawalRequest']]))
        withdrawal_request.click()

    def navigate_to_real_account(self, username):
        self.backoffice_area()
        self.real_accounts()
        self.search_by_email_id(username)

    def navigate_to_campaign_account(self, username):
        self.backoffice_area()
        self.campaign_accounts()
        self.search_by_email_id_campaign(username)

    def set_to_approve(self, type_of_account, id_or_por_approval):
        approve = WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable([By.XPATH, CommonFunctions.bo_id_por_approve(type_of_account, id_or_por_approval)]))
        return approve.click()

    def set_to_reject(self, type_of_account):
        return self.driver.execute_script("arguments[0].click();", self.driver.find_element(
            By.XPATH, CommonFunctions.bo_id_reject(type_of_account)))

    def check_if_bo_id_approved(self, bo_id_status, bo_por_status):
        self.driver.switch_to.alert.accept()
        validate_bo_id_por = AdminBackOfficeAreaValidation(self.driver)
        validate_bo_id_por.validate_admin_bo_id_por_status_matches_records_in_db(bo_id_status, bo_por_status)

    def check_if_bo_id_or_por_rejected(self, bo_id_status, bo_por_status):
        self.driver.switch_to.alert.accept()
        self.driver.find_element(By.XPATH, CommonFunctions.select_reject_reason(2)).click()
        self.driver.find_element(By.ID, self.my_dict['txtRejectNote']). \
            send_keys('Not in a mood to approve. Testing Purpose.' + Keys.INSERT)
        self.driver.find_element(By.CSS_SELECTOR, self.my_dict['btnRejectId']).click()
        validate_bo_id_por = AdminBackOfficeAreaValidation(self.driver)
        validate_bo_id_por.validate_admin_bo_id_por_status_matches_records_in_db(bo_id_status, bo_por_status)

    def change_bo_id_por_status_for_ic_or_ib(self, bo_id_status, bo_por_status):
        self.show_table(self.my_dict['tblRealAccounts'])
        if bo_id_status == 'Approve' and bo_por_status is None:
            self.set_to_approve('realprofile', 'id')
            return BackOfficeAreaPage.check_if_bo_id_approved(self, bo_id_status, bo_por_status)
        elif bo_id_status == 'Reject' and bo_por_status is None:
            self.set_to_reject('realprofile')
            return BackOfficeAreaPage.check_if_bo_id_or_por_rejected(self, bo_id_status, bo_por_status)
        elif bo_id_status == 'Approve' and bo_por_status == 'Approve':
            self.set_to_approve('realprofile', 'id')
            self.driver.switch_to.alert.accept()
            self.set_to_approve('realprofile', 'por')
            return BackOfficeAreaPage.check_if_bo_id_approved(self, bo_id_status, bo_por_status)
        elif bo_id_status == 'Approve' and bo_por_status == 'Reject':
            self.set_to_approve('realprofile', 'id')
            self.driver.switch_to.alert.accept()
            self.set_to_reject('realprofile')
            return BackOfficeAreaPage.check_if_bo_id_or_por_rejected(self, bo_id_status, bo_por_status)

    def change_bo_id_por_status_for_ic_campaign(self, bo_id_status, bo_por_status):
        # self.click_table_data('tblCampaignAccounts', 1, 1)
        self.show_table(self.my_dict['tblRealAccounts'])
        if bo_id_status == 'Approve' and bo_por_status is None:
            self.set_to_approve('campaign_real_accounts', 'id')
            return BackOfficeAreaPage.check_if_bo_id_approved(self, bo_id_status, bo_por_status)
        elif bo_id_status == 'Reject' and bo_por_status is None:
            self.set_to_reject('campaign_real_accounts')
            return BackOfficeAreaPage.check_if_bo_id_or_por_rejected(self, bo_id_status, bo_por_status)
        elif bo_id_status == 'Approve' and bo_por_status == 'Approve':
            self.set_to_approve('campaign_real_accounts', 'id')
            self.driver.switch_to.alert.accept()
            self.set_to_approve('campaign_real_accounts', 'por')
            return BackOfficeAreaPage.check_if_bo_id_approved(self, bo_id_status, bo_por_status)
        elif bo_id_status == 'Approve' and bo_por_status == 'Reject':
            self.set_to_approve('campaign_real_accounts', 'id')
            self.driver.switch_to.alert.accept()
            self.set_to_reject('campaign_real_accounts')
            return BackOfficeAreaPage.check_if_bo_id_or_por_rejected(self, bo_id_status, bo_por_status)

    def click_forward_to_compliance(self):
        forward_to_compliance = WebDriverWait(self.driver, 90).until(
                EC.element_to_be_clickable([By.XPATH, self.my_dict['lnkForwardToCompliance']]))
        forward_to_compliance.click()
        self.driver.switch_to.alert.accept()

    def select_ib_login(self, commission_account_settings):
        login = self.driver.find_element(By.ID, self.my_dict['selectLogin'])
        self.driver.execute_script(CommonFunctions.set_admin_element_attribute('commission_account_login'), login)
        CommonFunctions.select_values(login, commission_account_settings.get_login())

    def select_ib_company(self, commission_account_settings):
        company = self.driver.find_element(By.ID, self.my_dict['selectCompany'])
        self.driver.execute_script(CommonFunctions.set_admin_element_attribute('commission_account_regulatedEntity'), company)
        CommonFunctions.select_values(company, commission_account_settings.get_company())

    def select_ib_platform(self, commission_account_settings):
        platform = self.driver.find_element(By.ID, self.my_dict['selectPlatform'])
        self.driver.execute_script(CommonFunctions.set_admin_element_attribute('commission_account_Platform'), platform)
        CommonFunctions.select_values(platform, commission_account_settings.get_platform())

    def select_ib_trading_group(self, commission_account_settings):
        trading_group = self.driver.find_element(By.ID, self.my_dict['selectTradingGroup'])
        self.driver.execute_script(CommonFunctions.set_admin_element_attribute('commission_account_CodeTradingGroup'), trading_group)
        CommonFunctions.select_values(trading_group, commission_account_settings.get_trading_group())

    def select_ib_trading_currency(self, commission_account_settings):
        trading_currency = self.driver.find_element(By.ID, self.my_dict['selectTradingCurrency'])
        self.driver.execute_script(CommonFunctions.set_admin_element_attribute('commission_account_TradingCurrency'), trading_currency)
        CommonFunctions.select_values(trading_currency, commission_account_settings.get_trading_currency())

    def select_ib_leverage(self, commission_account_settings):
        leverage = self.driver.find_element(By.ID, self.my_dict['selectLeverage'])
        self.driver.execute_script(CommonFunctions.set_admin_element_attribute('commission_account_leverage'), leverage)
        CommonFunctions.select_values(leverage, commission_account_settings.get_leverage())

    def ib_agreement(self, commission_account_settings):
        ib_agreement = self.driver.find_element(By.ID, self.my_dict['txtIbAgreement'])
        ib_agreement.clear()
        ib_agreement.send_keys(commission_account_settings.get_ib_agreement() + Keys.INSERT)

    def fill_ib_commission_account_settings(self, commission_account_settings):
        approve_ib_application = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable([By.XPATH, self.my_dict['lnkApproveIbApplication']]))
        approve_ib_application.click()
        self.select_ib_login(commission_account_settings)
        self.select_ib_company(commission_account_settings)
        self.select_ib_platform(commission_account_settings)
        self.select_ib_trading_group(commission_account_settings)
        self.select_ib_trading_currency(commission_account_settings)
        self.select_ib_leverage(commission_account_settings)
        self.ib_agreement(commission_account_settings)

    def change_ib_bo_application_status(self, username):
        self.ib_approve_application()
        self.click_forward_to_compliance()
        self.real_accounts()
        self.search_by_email_id(username)
        bo_application_status = (self.driver.find_element(
            By.XPATH, GetWebTableData.get_cols_data(self.my_dict['tblRealAccounts'], 1, 9))).text
        return bo_application_status

    def ib_approve_application(self):
        application_approve = self.driver.find_element(By.CSS_SELECTOR, self.my_dict['btnApproveApplication'])
        self.driver.execute_script("arguments[0].click();", application_approve)

    def get_trading_account_number(self):
        trading_account_number = self.driver.find_element(By.XPATH,
                                                          GetWebTableData.get_cols_data(self.my_dict['tblRealAccounts'],
                                                                                        1, 15))
        trading_account_number = trading_account_number.text
        return trading_account_number

    def select_bo_id_status(self, status):
        bo_id_status = self.driver.find_element(By.ID, self.my_dict['ddBOIdStatus'])
        self.driver.execute_script(CommonFunctions.set_element_attribute('bo_id_status'), bo_id_status)
        CommonFunctions.select_values(self.driver.find_element(By.ID, self.my_dict['ddSelectBOIdStatus']), status)

    def enter_trading_accounts(self, text):
        trading_accounts = self.driver.find_element(By.CLASS_NAME, self.my_dict['txtTradingAccounts']).send_keys(
            text + Keys.INSERT)
        return trading_accounts

    def select_wlid(self, value):
        wlid = self.driver.find_element(By.ID, self.my_dict['ddWlid'])
        self.driver.execute_script(CommonFunctions.set_element_attribute('filter_PortalUser__wlid_value'), wlid)
        CommonFunctions.select_values(self.driver.find_element(By.ID, self.my_dict['ddSelectWlid']), value)

    def select_has_account(self, value):
        has_account = self.driver.find_element(By.ID, self.my_dict['ddHasAccount'])
        self.driver.execute_script(CommonFunctions.set_element_attribute('filter_hasAccountFilter_value'), has_account)
        CommonFunctions.select_values(self.driver.find_element(By.ID, self.my_dict['ddSelectHasAccount']), value)

    def select_has_attachment(self, value):
        has_attachment = self.driver.find_element(By.ID, self.my_dict['ddHasAttachment'])
        self.driver.execute_script(CommonFunctions.set_element_attribute('filter_hasAttachmentFilter_value'),
                                   has_attachment)
        CommonFunctions.select_values(self.driver.find_element(By.ID, self.my_dict['ddSelectHasAttachment']), value)

    def click_generated_trading_account_number(self, index):
        self.driver.find_element(By.XPATH, self.my_dict['lnkTradingAccounts' + str(index)]).click()

    def navigate_to_trading_account_details(self, username, trading_account_index):
        self.driver.find_element(By.XPATH, str(CommonFunctions.select_parent_admin_menu(3))).click()
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located([
            By.XPATH, str(CommonFunctions.select_child_admin_menu(3, 4))]))
        self.driver.find_element(By.XPATH, str(CommonFunctions.select_child_admin_menu(3, 4))).click()
        self.search_by_email_id(username)
        self.click_generated_trading_account_number(str(trading_account_index))
        self.driver.switch_to.window(self.driver.window_handles[1])

    def get_trading_account_detailed_info(self, username, trading_account_index):
        self.navigate_to_trading_account_details(username, trading_account_index)
        try:
            row_size = len(self.driver.find_elements(By.XPATH, GetWebTableData.get_rows('table table-custom')))
            trading_account_info = {}
            for i in range(1, row_size):
                key = self.driver.find_elements(
                    By.XPATH, GetWebTableData.get_cols_header('table table-custom', i, 1))[0]
                value = self.driver.find_elements(
                    By.XPATH, GetWebTableData.get_cols_data('table table-custom', i, 1))[0]
                trading_account_info[key.text] = value.text
            return trading_account_info
        except NoSuchElementException:
            print("NoSuchElementException")

    def real_profile_show(self, username):
        self.driver.find_element(By.XPATH, str(CommonFunctions.select_parent_admin_menu(3))).click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located([By.XPATH, str(CommonFunctions.select_child_admin_menu(3, 4))]))
        self.driver.find_element(By.XPATH, str(CommonFunctions.select_child_admin_menu(3, 4))).click()
        self.driver.find_element(By.CLASS_NAME, self.my_dict['txtEmail']).send_keys(username + Keys.INSERT)
        self.driver.find_element(By.CLASS_NAME, self.my_dict['btnFilter']).click()
        self.driver.find_element(By.XPATH, self.my_dict['lnkId']).click()

    def convert_ic_to_ib_user(self):
        self.driver.find_element(By.XPATH, self.my_dict['lnkConvertToIb']).click()
        self.driver.switch_to.alert.accept()
        submit = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable([By.NAME, self.my_dict['btnSubmit']]))
        submit.click()

    def convert_ib_to_ic_user(self):
        self.driver.find_element(By.XPATH, self.my_dict['lnkConvertToIc']).click()
        self.driver.switch_to.alert.accept()
        submit = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable([By.NAME, self.my_dict['btnSubmit']]))
        submit.click()

    def upload_documents_by_admin(self):
        filename = os.environ.get('UPLOAD_FILE') + str('fakePassport.jpg')
        self.driver.find_element(By.CLASS_NAME, self.my_dict['lnkDocuments']).click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable([By.ID, self.my_dict['uploadDocumentId2']]))
        ActionChains(self.driver).move_to_element(
            self.driver.find_element(By.ID, self.my_dict['uploadDocumentId2'])).click().perform()
        result = CommonFunctions.upload_files(filename)
        return result

    def click_main_information(self):
        self.driver.find_element(By.CLASS_NAME, self.my_dict['lnkMainInformation']).click()

    def click_impersonate_user(self):
        self.driver.find_element(By.CSS_SELECTOR, self.my_dict['lnkImpersonateUser']).click()

    def show_real_accounts(self):
        return self.show_table(self.my_dict['tblRealAccounts'])

    def switch_to_client_portal(self, window_tab_index):
        try:
            self.click_impersonate_user()
            self.driver.switch_to.window(self.driver.window_handles[window_tab_index])
        except RuntimeError:
            print("Unable to open Impersonate user in client portal")
