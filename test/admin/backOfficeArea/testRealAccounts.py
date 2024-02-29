import unittest
import allure

from common.commonFunctions import CommonFunctions
from common.enum.client.clientType import ClientType
from common.enum.client.regulatorPlatformTierType import RegulatorPlatformTierType
from common.steps.adminSteps import AdminSteps
from common.steps.clientSteps import ClientSteps

from test.baseTest import BaseTest

username = ""
client_email = CommonFunctions.generate_random_email()


class TestRealAccountsTest(unittest.TestCase):

    def setUp(self):
        global username
        username = CommonFunctions.generate_random_email()

    @allure.feature('BO ID')
    @allure.story('US12345: As an admin user, I should be able to approve/reject BO Id/por submitted by IC user')
    @allure.testcase('To verify if admin user is able to approve BO Id submitted by IC user')
    def test_IC_TC1_To_verify_if_admin_user_is_able_to_approve_bo_id(self):
        cs = ClientSteps()
        cs.submit_ic_application(username)
        ast = AdminSteps()
        ast.validate_bo_id_por_change_status_for_ic_or_ib(username, 'Approve', None)

    @allure.feature('BO ID')
    @allure.testcase('To verify if admin user is able to reject BO Id submitted by IC user')
    def test_IC_TC2_To_verify_if_admin_user_is_able_to_reject_bo_id(self):
        cs = ClientSteps()
        cs.submit_ic_application(username)
        ast = AdminSteps()
        ast.validate_bo_id_por_change_status_for_ic_or_ib(username, 'Reject', None)

    @allure.feature('BO POR')
    @allure.testcase('To verify if admin user is able to approve BO POR submitted by IC user')
    def test_IC_TC3_To_verify_if_admin_user_is_able_to_approve_bo_por(self):
        cs = ClientSteps()
        cs.submit_ic_application(username)
        ast = AdminSteps()
        ast.validate_bo_id_por_change_status_for_ic_or_ib(username, 'Approve', 'Approve')

    @allure.feature('BO POR')
    @allure.testcase('To verify if admin user is able to reject BO POR submitted by IC user')
    def test_IC_TC4_To_verify_if_admin_user_is_able_to_reject_bo_por(self):
        cs = ClientSteps()
        cs.submit_ic_application(username)
        ast = AdminSteps()
        ast.validate_bo_id_por_change_status_for_ic_or_ib(username, 'Approve', 'Reject')

    @allure.feature('C-Trader')
    @allure.testcase('To verify if admin user is able to approve BO ID submitted by IC user with C-Trader')
    def test_IC_TC5_To_verify_if_admin_user_is_able_to_approve_bo_id_with_c_trader(self):
        client_type = ClientType.individual.value
        regulator_platform_tier_type = RegulatorPlatformTierType.mex_atlantic_c_trader_standard.value
        cs = ClientSteps
        cs.api_ic_registration_without_trading_accounts_settings(username)
        cs.navigate_to_dashboard_after_filling_ic_details_with_c_trader(username, client_type, regulator_platform_tier_type)
        ast = AdminSteps()
        ast.validate_bo_id_por_change_status_for_ic_or_ib(username, 'Approve', None)

    @allure.feature('C-Trader')
    @allure.testcase('To verify if admin user is able to reject BO ID submitted by IC user with C-Trader')
    def test_IC_TC6_To_verify_if_admin_user_is_able_to_reject_bo_id_with_c_trader(self):
        client_type = ClientType.individual.value
        regulator_platform_tier_type = RegulatorPlatformTierType.mex_atlantic_c_trader_standard.value
        cs = ClientSteps
        cs.api_ic_registration_without_trading_accounts_settings(username)
        cs.navigate_to_dashboard_after_filling_ic_details_with_c_trader(username, client_type,
                                                                        regulator_platform_tier_type)
        ast = AdminSteps()
        ast.validate_bo_id_por_change_status_for_ic_or_ib(username, 'Reject', None)

    @allure.feature('C-Trader')
    @allure.testcase('To verify if admin user is able to approve BO POR submitted by IC user with C-Trader')
    def test_IC_TC7_To_verify_if_admin_user_is_able_to_approve_bo_por_with_c_trader(self):
        client_type = ClientType.individual.value
        regulator_platform_tier_type = RegulatorPlatformTierType.mex_atlantic_c_trader_standard.value
        cs = ClientSteps
        cs.api_ic_registration_without_trading_accounts_settings(username)
        cs.navigate_to_dashboard_after_filling_ic_details_with_c_trader(username, client_type,
                                                                        regulator_platform_tier_type)
        ast = AdminSteps()
        ast.validate_bo_id_por_change_status_for_ic_or_ib(username, 'Approve', 'Approve')

    @allure.feature('C-Trader')
    @allure.testcase('To verify if admin user is able to reject BO POR submitted by IC user with C-Trader')
    def test_IC_TC8_To_verify_if_admin_user_is_able_to_reject_bo_por_with_c_trader(self):
        client_type = ClientType.individual.value
        regulator_platform_tier_type = RegulatorPlatformTierType.mex_atlantic_c_trader_standard.value
        cs = ClientSteps
        cs.api_ic_registration_without_trading_accounts_settings(username)
        cs.navigate_to_dashboard_after_filling_ic_details_with_c_trader(username, client_type,
                                                                        regulator_platform_tier_type)
        ast = AdminSteps()
        ast.validate_bo_id_por_change_status_for_ic_or_ib(username, 'Approve', 'Reject')

    @allure.feature('BO ID')
    @allure.story('US12345: As an admin user, I should be able to approve/reject BO Id/por submitted by ic campaign user')
    @allure.testcase('To verify if admin user is able to approve BO Id submitted by ic campaign user')
    def test_IC_Campaign_TC9_To_verify_if_admin_user_is_able_to_approve_BO_Id(self):
        client_type = ClientType.individual.value
        cs = ClientSteps()
        cs.submit_ic_campaign_application(username, client_type, None)
        ast = AdminSteps()
        ast.validate_bo_id_por_change_status_for_ic_campaign(username, 'Approve', None)

    @allure.feature('BO ID')
    @allure.testcase('To verify if admin user is able to reject BO Id submitted by ic campaign user')
    def test_IC_Campaign_TC10_To_verify_if_admin_user_is_able_to_reject_BO_Id(self):
        client_type = ClientType.individual.value
        cs = ClientSteps()
        cs.submit_ic_campaign_application(username, client_type, None)
        ast = AdminSteps()
        ast.validate_bo_id_por_change_status_for_ic_campaign(username, 'Reject', None)

    @allure.feature('BO POR')
    @allure.testcase('To verify if admin user is able to approve BO Por submitted by ic campaign user')
    def test_IC_Campaign_TC11_To_verify_if_admin_user_is_able_to_approve_BO_POR(self):
        client_type = ClientType.individual.value
        cs = ClientSteps()
        cs.submit_ic_campaign_application(username, client_type, None)
        ast = AdminSteps()
        ast.validate_bo_id_por_change_status_for_ic_campaign(username, 'Approve', 'Approve')

    @allure.feature('BO POR')
    @allure.testcase('To verify if admin user is able to reject BO Por submitted by ic campaign user')
    def test_IC_Campaign_TC12_To_verify_if_admin_user_is_able_to_reject_BO_POR(self):
        client_type = ClientType.individual.value
        cs = ClientSteps()
        cs.submit_ic_campaign_application(username, client_type, None)
        ast = AdminSteps()
        ast.validate_bo_id_por_change_status_for_ic_campaign(username, 'Approve', 'Reject')

    @allure.feature('BO ID')
    @allure.story('US12345: As an admin user, I should be able to approve/reject BO Id/por submitted by IB user')
    @allure.testcase('To verify if admin user is able to approve BO Id submitted by IB user')
    def test_IB_TC13_To_verify_if_admin_user_is_able_to_approve_bo_id(self):
        cs = ClientSteps
        cs.submit_ib_application(username)
        ast = AdminSteps
        ast.validate_bo_id_por_change_status_for_ic_or_ib(username, 'Approve', None)

    @allure.feature('BO ID')
    @allure.testcase('To verify if admin user is able to reject BO Id submitted by IB user')
    def test_IB_TC14_To_verify_if_admin_user_is_able_to_reject_bo_id(self):
        cs = ClientSteps
        cs.submit_ib_application(username)
        ast = AdminSteps
        ast.validate_bo_id_por_change_status_for_ic_or_ib(username, 'Reject', None)

    @allure.feature('BO POR')
    @allure.testcase('To verify if admin user is able to approve BO POR submitted by IB user')
    def test_IB_TC15_To_verify_if_admin_user_is_able_to_approve_bo_por(self):
        cs = ClientSteps
        cs.submit_ib_application(username)
        ast = AdminSteps
        ast.validate_bo_id_por_change_status_for_ic_or_ib(username, 'Approve', 'Approve')

    @allure.feature('BO POR')
    @allure.testcase('To verify if admin user is able to reject BO POR submitted by IB user')
    def test_IB_TC16_To_verify_if_admin_user_is_able_to_reject_bo_por(self):
        cs = ClientSteps
        cs.submit_ib_application(username)
        ast = AdminSteps
        ast.validate_bo_id_por_change_status_for_ic_or_ib(username, 'Approve', 'Reject')

    @allure.feature('Forward To Compliance')
    @allure.story('US12345: As an admin user, I should be able to approve IB Application and forward to compliance')
    @allure.testcase('To verify if admin user is able to approve IB Application and forward it to compliance')
    def test_IB_TC17_To_verify_if_admin_user_is_able_to_forward_ib_approved_application_to_compliance(self):
        cs = ClientSteps
        cs.submit_ib_application(username)
        ast = AdminSteps
        self.assertEqual('FORWARDED', ast.validate_bo_ib_application_status(username, 'Approve', 'Approve'),
                         "BO Application Status not changing as expected!!!")

    @allure.feature('IB Client')
    @allure.testcase('To verify if admin user is able to approve IB client BO ID')
    def test_IB_Client_TC18_To_verify_if_admin_user_able_to_approve_IB_client_bo_id(self):
        base_test = BaseTest
        base_test.ib_registered_clients(username, client_email, 'Approve', 'Approve', 'Approve', 'Approve', 'Approve')
        ast = AdminSteps()
        ast.validate_bo_id_por_change_status_for_ic_or_ib(client_email, 'Approve', None)

    @allure.feature('IB Client')
    @allure.testcase('To verify if admin user is able to reject IB client BO ID')
    def test_IB_Client_TC19_To_verify_if_admin_user_able_to_reject_IB_client_bo_id(self):
        base_test = BaseTest
        base_test.ib_registered_clients(username, client_email, 'Approve', 'Approve', 'Approve', 'Approve', 'Approve')
        ast = AdminSteps()
        ast.validate_bo_id_por_change_status_for_ic_or_ib(client_email, 'Reject', None)

    @allure.feature('IB Client')
    @allure.testcase('To verify if admin user is able to approve IB client BO POR')
    def test_IB_Client_TC20_To_verify_if_admin_user_able_to_approve_IB_client_bo_por(self):
        base_test = BaseTest
        base_test.ib_registered_clients(username, client_email, 'Approve', 'Approve', 'Approve', 'Approve', 'Approve')
        ast = AdminSteps()
        ast.validate_bo_id_por_change_status_for_ic_or_ib(client_email, 'Approve', 'Approve')

    @allure.feature('IB Client')
    @allure.testcase('To verify if admin user is able to reject IB client BO POR')
    def test_IB_Client_TC21_To_verify_if_admin_user_able_to_reject_IB_client_bo_por(self):
        base_test = BaseTest
        base_test.ib_registered_clients(username, client_email, 'Approve', 'Approve', 'Approve', 'Approve', 'Approve')
        ast = AdminSteps()
        ast.validate_bo_id_por_change_status_for_ic_or_ib(client_email, 'Approve', 'Reject')

    def tearDown(self):
        ClientSteps.teardown('Real Accounts')
        AdminSteps.teardown('Bo Id Por')


if __name__ == "__main__":
    unittest.main()
