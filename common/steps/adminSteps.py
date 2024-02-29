import os
import time

from common.data.admin.backOfficeArea.commissionAccountSettingsData import CommissionAccountSettingsData
from common.pageObjects.admin.backOfficeAreaPage import BackOfficeAreaPage
from common.pageObjects.admin.complianceAreaPage import ComplianceAreaPage
from common.pageObjects.basePage import BasePage
from common.pageObjects.client.loginPage import LoginPage
from common.setup.setup import SetupPage

driver = ''


class AdminSteps:

    @staticmethod
    def login_admin():
        global driver
        asp = SetupPage(driver)
        driver = asp.admin_setup()
        lp = LoginPage(driver)
        lp.admin_login(os.environ.get('ADMIN_USERNAME'), os.environ.get('ADMIN_PASSWORD'))

    @staticmethod
    def validate_bo_id_por_change_status_for_ic_or_ib(username, bo_id_status, bo_por_status):
        AdminSteps.login_admin()
        bo = BackOfficeAreaPage(driver)
        bo.navigate_to_real_account(username)
        result = bo.change_bo_id_por_status_for_ic_or_ib(bo_id_status, bo_por_status)
        return result

    @staticmethod
    def upload_bo_documents():
        bo = BackOfficeAreaPage(driver)
        result = bo.upload_documents_by_admin()
        return result

    @staticmethod
    def validate_bo_id_por_change_status_for_ic_campaign(username, bo_id_status, bo_por_status):
        AdminSteps.login_admin()
        bo = BackOfficeAreaPage(driver)
        bo.navigate_to_campaign_account(username)
        result = bo.change_bo_id_por_status_for_ic_campaign(bo_id_status, bo_por_status)
        return result

    @staticmethod
    def validate_bo_ib_application_status(username, bo_id_status, bo_por_status):
        AdminSteps.validate_bo_id_por_change_status_for_ic_or_ib(username, bo_id_status, bo_por_status)
        bo = BackOfficeAreaPage(driver)
        ib_commission_account_settings_data = CommissionAccountSettingsData.commission_account_settings()
        bo.fill_ib_commission_account_settings(ib_commission_account_settings_data)
        result = bo.change_ib_bo_application_status(username)
        return result

    @staticmethod
    def validate_compliance_change_status_for_ic(username, bo_id_status, bo_por_status, compliance_id_status,
                                                 comp_id_status, comp_por_status):
        AdminSteps.validate_bo_id_por_change_status_for_ic_or_ib(username, bo_id_status, bo_por_status)
        bo = BackOfficeAreaPage(driver)
        bo.click_forward_to_compliance()
        ca = ComplianceAreaPage(driver)
        result = ca.validate_change_compliance_id_status(username, compliance_id_status, comp_id_status,
                                                         comp_por_status)
        return result

    @staticmethod
    def validate_withdrawal_request(username):
        AdminSteps.login_admin()
        bo = BackOfficeAreaPage(driver)
        bo.navigate_to_real_account(username)
        result = bo.withdrawal_request()
        return result

    @staticmethod
    def validate_compliance_change_status_for_ib(username, bo_id_status, bo_por_status, compliance_id_status,
                                                 comp_id_status, comp_por_status):
        AdminSteps.validate_bo_ib_application_status(username, bo_id_status, bo_por_status)
        ca = ComplianceAreaPage(driver)
        result = ca.validate_change_compliance_id_status(username, compliance_id_status, comp_id_status,
                                                         comp_por_status)
        return result

    @staticmethod
    def validate_compliance_change_status_for_ic_campaign(username, bo_id_status, bo_por_status, compliance_id_status,
                                                          comp_id_status, comp_por_status):
        AdminSteps.validate_bo_id_por_change_status_for_ic_campaign(username, bo_id_status, bo_por_status)
        bo = BackOfficeAreaPage(driver)
        bo.click_forward_to_compliance()
        ca = ComplianceAreaPage(driver)
        result = ca.validate_change_ic_campaign_compliance_id_status(username, compliance_id_status, comp_id_status,
                                                                     comp_por_status)
        return result

    @staticmethod
    def edit_info_requests_change_status(username, status):
        AdminSteps.login_admin()
        bo = BackOfficeAreaPage(driver)
        bo.edit_info_request_change_status(username, status)

    @staticmethod
    def ic_to_ib():
        bo = BackOfficeAreaPage(driver)
        bo.convert_ic_to_ib_user()

    @staticmethod
    def ib_to_ic():
        bo = BackOfficeAreaPage(driver)
        bo.convert_ib_to_ic_user()

    @staticmethod
    def trading_account_number():
        bo = BackOfficeAreaPage(driver)
        result = bo.get_trading_account_number()
        return result

    @staticmethod
    def show_real_accounts():
        bo = BackOfficeAreaPage(driver)
        bo.show_real_accounts()

    @staticmethod
    def switch_to_client_portal(window_tab_index):
        bo = BackOfficeAreaPage(driver)
        bo.switch_to_client_portal(window_tab_index)

    @staticmethod
    def teardown(test):
        base_page = BasePage(driver)
        base_page.attach_screenshot(test)
        asp = SetupPage(driver)
        return asp.teardown()
