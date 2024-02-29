from common.commonFunctions import CommonFunctions
from common.enum.client.clientType import ClientType
from common.enum.client.regulatorPlatformTierType import RegulatorPlatformTierType
from common.steps.adminSteps import AdminSteps
from common.steps.clientSteps import ClientSteps
import unittest
import allure

from test.baseTest import BaseTest

username = CommonFunctions.generate_random_email()
client_email = CommonFunctions.generate_random_email()


class TestRegisterClientsTest(unittest.TestCase):

    def setUp(self):
        base_test = BaseTest
        base_test.ib_compliance_change_status(username, 'Approve', 'Approve', 'Approve', 'Approve', 'Approve')

    @allure.feature('IB Client')
    @allure.story('US12345: As an ib user, I should be able to register my clients')
    @allure.testcase('To verify if ib user is able to register his clients')
    def test_IB_Client_TC1_To_verify_if_ib_user_is_able_to_register_his_clients(self):
        client_type = ClientType.individual.value
        cs = ClientSteps
        ast = AdminSteps
        regulator_platform_tier = RegulatorPlatformTierType.mex_atlantic_mt4_standard.value
        ast.show_real_accounts()
        ast.switch_to_client_portal(window_tab_index=1)
        cs.ib_register_clients(client_email, client_type, regulator_platform_tier)

    def tearDown(self):
        ClientSteps.teardown("IB Registered Clients")
        AdminSteps.teardown("IB Approved Application")


if __name__ == "__main__":
    unittest.main()
