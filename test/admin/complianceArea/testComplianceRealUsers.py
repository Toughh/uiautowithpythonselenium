from common.commonFunctions import CommonFunctions
from common.enum.client.clientType import ClientType
from common.enum.client.regulatorPlatformTierType import RegulatorPlatformTierType
from common.steps.adminSteps import AdminSteps
from common.steps.clientSteps import ClientSteps
import unittest
import allure

from test.baseTest import BaseTest

username = ""
client_email = CommonFunctions.generate_random_email()


class TestComplianceRealUsersTest(unittest.TestCase):

    def setUp(self):
        global username
        username = CommonFunctions.generate_random_email()

    @allure.story('US12345: As an admin user, I should be able to approve/reject compliance for ic user')
    @allure.testcase('To verify if admin user able to approve compliance for ic user')
    def test_IC_TC1_To_verify_if_admin_user_is_able_to_approve_compliance(self):
        cs = ClientSteps
        cs.submit_ic_application(username)
        ast = AdminSteps
        ast.validate_compliance_change_status_for_ic(username, 'Approve', 'Approve', 'Approve', 'Approve', 'Approve')

    @allure.testcase('To verify if admin user able to reject compliance for ic user')
    def test_IC_TC2_To_verify_if_admin_user_is_able_to_reject_compliance(self):
        cs = ClientSteps
        cs.submit_ic_application(username)
        ast = AdminSteps
        ast.validate_compliance_change_status_for_ic(username, 'Approve', 'Approve', 'Reject', None, None)

    @allure.feature('C-Trader')
    @allure.testcase('To verify if admin user is able to approve compliance for ic user with C-Trader')
    def test_IC_TC3_To_verify_if_admin_user_is_able_to_approve_compliance_with_c_trader(self):
        client_type = ClientType.individual.value
        regulator_platform_tier_type = RegulatorPlatformTierType.mex_atlantic_c_trader_standard.value
        cs = ClientSteps
        cs.api_ic_registration_without_trading_accounts_settings(username)
        cs.navigate_to_dashboard_after_filling_ic_details_with_c_trader(username, client_type,
                                                                        regulator_platform_tier_type)
        ast = AdminSteps
        ast.validate_compliance_change_status_for_ic(username, 'Approve', 'Approve', 'Approve', 'Approve', 'Approve')

    @allure.feature('C-Trader')
    @allure.testcase('To verify if admin user is able to reject compliance for ic user with C-Trader')
    def test_IC_TC4_To_verify_if_admin_user_is_able_to_reject_compliance_with_c_trader(self):
        client_type = ClientType.individual.value
        regulator_platform_tier_type = RegulatorPlatformTierType.mex_atlantic_c_trader_standard.value
        cs = ClientSteps
        cs.api_ic_registration_without_trading_accounts_settings(username)
        cs.navigate_to_dashboard_after_filling_ic_details_with_c_trader(username, client_type,
                                                                        regulator_platform_tier_type)
        ast = AdminSteps
        ast.validate_compliance_change_status_for_ic(username, 'Approve', 'Approve', 'Reject', None, None)

    @allure.story('US12345: As an admin user, I should be able to approve/reject compliance for ic campaign user')
    @allure.testcase('To verify if admin user able to approve compliance for ic campaign user')
    def test_IC_Campaign_TC5_To_verify_if_admin_user_is_able_to_approve_compliance(self):
        client_type = ClientType.individual.value
        cs = ClientSteps
        cs.submit_ic_campaign_application(username, client_type, None)
        ast = AdminSteps
        ast.validate_compliance_change_status_for_ic_campaign(username, 'Approve', 'Approve', 'Approve', 'Approve', 'Approve')

    @allure.testcase('To verify if admin user able to reject compliance for ic campaign user')
    def test_IC_Campaign_TC6_To_verify_if_admin_user_is_able_to_reject_compliance(self):
        client_type = ClientType.individual.value
        cs = ClientSteps
        cs.submit_ic_campaign_application(username, client_type, None)
        ast = AdminSteps
        ast.validate_compliance_change_status_for_ic_campaign(username, 'Approve', 'Approve', 'Reject', None, None)

    @allure.story('US12345: As an admin user, I should be able to approve/reject compliance for ib user')
    @allure.testcase('To verify if admin user able to approve compliance for ib user')
    def test_IB_TC7_To_verify_if_admin_user_is_able_to_approve_compliance(self):
        cs = ClientSteps
        cs.submit_ib_application(username)
        ast = AdminSteps
        ast.validate_compliance_change_status_for_ib(username, 'Approve', 'Approve', 'Approve', 'Approve', 'Approve')

    @allure.testcase('To verify if admin user able to reject compliance for ib user')
    def test_IB_TC8_To_verify_if_admin_user_is_able_to_reject_compliance(self):
        cs = ClientSteps
        cs.submit_ib_application(username)
        ast = AdminSteps
        ast.validate_compliance_change_status_for_ib(username, 'Approve', 'Approve', 'Reject', None, None)

    @allure.feature('IB Client')
    @allure.testcase('To verify if admin user is able to approve IB client compliance')
    def test_IB_Client_TC9_To_verify_if_admin_user_able_to_approve_IB_client_compliance(self):
        base_test = BaseTest
        base_test.ib_registered_clients(username, client_email, 'Approve', 'Approve', 'Approve', 'Approve', 'Approve')
        ast = AdminSteps()
        ast.validate_compliance_change_status_for_ic(client_email, 'Approve', 'Approve', 'Approve', 'Approve', 'Approve')

    @allure.feature('IB Client')
    @allure.testcase('To verify if admin user is able to reject IB client compliance')
    def test_IB_Client_TC10_To_verify_if_admin_user_able_to_reject_IB_client_compliance(self):
        base_test = BaseTest
        base_test.ib_registered_clients(username, client_email, 'Approve', 'Approve', 'Approve', 'Approve', 'Approve')
        ast = AdminSteps()
        ast.validate_compliance_change_status_for_ic(client_email, 'Approve', 'Approve', 'Reject', None, None)

    def tearDown(self):
        ClientSteps.teardown("User Submitted Application")
        AdminSteps.teardown("Compliance Real Users")


if __name__ == "__main__":
    unittest.main()
