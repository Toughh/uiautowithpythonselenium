import unittest
import allure

from common.commonFunctions import CommonFunctions
from common.steps.clientSteps import ClientSteps

username = ""


class LoginTest(unittest.TestCase):

    def setUp(self):
        global username
        username = CommonFunctions.generate_random_email()

    @allure.feature('Login')
    @allure.story('US12345: As an IC/IB/IC Campaign user, I should be able to login and logout client portal')
    @allure.testcase('To_verify_if_ic_user_is_able_to_login')
    def test_IC_TC1_To_verify_if_able_to_login(self):
        cs = ClientSteps
        assert cs.api_ic_registration_with_trading_accounts_settings(username) == 'Web Trading - MEX Atlantic'

    @allure.feature('Login')
    @allure.testcase('To_verify_if_ib_user_is_able_to_login')
    def test_IB_TC2_To_verify_if_able_to_login(self):
        cs = ClientSteps
        assert cs.api_ib_registration(username) == 'Application - My MultiBank'

    @allure.feature('Login')
    @allure.testcase('To_verify_if_ic_campaign_user_is_able_to_login')
    def test_IC_Campaign_TC3_To_verify_if_able_to_login(self):
        cs = ClientSteps
        assert cs.api_ic_campaign_registration_with_trading_account_settings(username) == 'Application - MEX Atlantic'

    @allure.feature('Login')
    @allure.testcase('To_verify_if_ic_user_is_able_to_logout')
    def test_IC_TC4_To_verify_if_able_to_logout(self):
        cs = ClientSteps
        cs.api_ic_registration_with_trading_accounts_settings(username)
        cs.validate_if_user_able_to_logout()

    @allure.feature('Login')
    @allure.testcase('To_verify_if_ib_user_is_able_to_logout')
    def test_IB_TC5_To_verify_if_able_to_logout(self):
        cs = ClientSteps
        cs.api_ib_registration(username)
        cs.validate_if_user_able_to_logout()

    @allure.feature('Login')
    @allure.testcase('To_verify_if_ic_campaign_user_is_able_to_logout')
    def test_IC_Campaign_TC6_To_verify_if_able_to_logout(self):
        cs = ClientSteps
        cs.api_ic_campaign_registration_with_trading_account_settings(username)
        cs.validate_if_user_able_to_logout()

    def tearDown(self):
        ClientSteps.teardown("Login")


if __name__ == "__main__":
    unittest.main()
