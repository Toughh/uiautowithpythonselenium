import unittest
import allure

from common.commonFunctions import CommonFunctions
from common.enum.client.clientType import ClientType
from common.steps.clientSteps import ClientSteps

username = ""


class ChangeMobileNumberTest(unittest.TestCase):

    def setUp(self):
        global username
        username = CommonFunctions.generate_random_email()

    @allure.feature('OTP')
    @allure.story('US12345: As an IC/IB/IC Campaign user, I should be able to change mobile number')
    @allure.testcase('To_verify_if_IC_user_able_to_change_his_mobile_number')
    def test_OTP_IC_TC1_To_verify_if_IC_user_able_to_change_his_mobile_number(self):
        client_type = ClientType.individual.value
        cs = ClientSteps
        cs.api_ic_registration_with_trading_accounts_settings(username)
        cs.validate_otp_under_change_mobile_number(client_type)

    @allure.feature('OTP')
    @allure.testcase('To_verify_if_IB_user_able_to_change_his_mobile_number')
    def test_OTP_IC_TC2_To_verify_if_IB_user_able_to_change_his_mobile_number(self):
        client_type = ClientType.corporate.value
        cs = ClientSteps
        cs.api_ib_registration(username)
        cs.validate_otp_under_change_mobile_number(client_type)

    @allure.feature('OTP')
    @allure.testcase('To_verify_if_IC_Campaign_user_able_to_change_his_mobile_number')
    def test_OTP_IC_Campaign_TC3_To_verify_if_IC_Campaign_user_able_to_change_his_mobile_number(self):
        client_type = ClientType.corporate.value
        cs = ClientSteps
        cs.api_ic_campaign_registration_with_trading_account_settings(username)
        cs.validate_otp_under_change_mobile_number(client_type)

    def tearDown(self):
        ClientSteps.teardown("Change Mobile Number")


if __name__ == "__main__":
    unittest.main()
