from common.api.registration.postRegisterNewAccountApi import RegisterNewAccountApi
from common.commonFunctions import CommonFunctions
import unittest
import allure

from common.data.api.dataSet.registration.registrationData import RegistrationData


class RegisterNewAccountApiTest(unittest.TestCase):

    @allure.story('US12345: As a end user, I should be able to register new account so that I can login into Client UI '
                  'application')
    @allure.testcase('To_verify_able to create new user account through api')
    def test_TC1_To_verify_able_to_create_new_user_account_through_api(self):
        username = CommonFunctions.generate_random_email()
        ic_registration = RegistrationData.register_ic_user(username)
        RegisterNewAccountApi.get_md5_key(ic_registration)

    @allure.story('US12345: As a end user, I should be able to register ic campaign user account so that I can login '
                  'into Client UI application')
    @allure.testcase('To verify if able to create new ic campaign user account through api')
    def test_TC2_To_verify_able_to_create_ic_campaign_user_account_through_api(self):
        username = CommonFunctions.generate_random_email()
        ic_campaign_user = RegistrationData.register_ic_campaign_user(username)
        RegisterNewAccountApi.get_register_new_account_res(ic_campaign_user)

    @allure.testcase('To verify if able to create new ic campaign user account without trading account settings through'
                     ' api')
    def test_TC3_To_verify_able_to_create_ic_campaign_user_account_without_trading_account_settings_through_api(self):
        username = CommonFunctions.generate_random_email()
        ic_campaign_user = RegistrationData.register_ic_campaign_user_without_trading_account_settings(username)
        RegisterNewAccountApi.get_register_new_account_res(ic_campaign_user)


if __name__ == "__main__":
    unittest.main()
