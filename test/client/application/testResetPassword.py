import unittest
import allure

from common.commonFunctions import CommonFunctions
from common.steps.clientSteps import ClientSteps

username = ""


class ResetPasswordTest(unittest.TestCase):

    def setUp(self):
        global username
        username = CommonFunctions.generate_random_email()

    @allure.feature('Reset Password')
    @allure.story('US12345: As an IC/IB/IC Campaign user, I should be able to reset my password and re-login')
    @allure.testcase('To_verify_if_ic_user_is_able_to_change_password_and_re_login')
    def test_IC_TC1_To_verify_if_user_is_able_to_change_password_and_re_login(self):
        cs = ClientSteps
        cs.api_ic_registration_with_trading_accounts_settings(username)
        cs.validate_if_user_able_to_reset_password(username)

    @allure.feature('Reset Password')
    @allure.story('US12345: As an IC/IB/IC Campaign user, I should be able to reset my trading password and re-login')
    @allure.testcase('To_verify_if_ic_user_is_able_to_change_trading_password_and_re_login')
    def test_IC_TC2_To_verify_if_user_is_able_to_change_trading_password_and_re_login(self):
        cs = ClientSteps
        cs.api_ic_registration_with_trading_accounts_settings(username)
        cs.validate_if_user_able_to_reset_trading_password()

    def tearDown(self):
        ClientSteps.teardown("Reset Password")


if __name__ == "__main__":
    unittest.main()
