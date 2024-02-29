from common.api.registration.postAddTradingAccountSettingsApi import TradingAccountSettingsApi
from common.commonFunctions import CommonFunctions
import unittest
import allure


class AddTradingAccountSettingsApiTest(unittest.TestCase):

    @allure.story('US12345: As a end user, I should be able to register new account so that I can login into Client UI '
                  'application')
    @allure.testcase('To_verify_able to create new user account through api')
    def test_TC1_To_verify_able_to_create_new_user_account_through_api(self):
        username = CommonFunctions.generate_random_email()
        TradingAccountSettingsApi.get_trading_account_settings(username)


if __name__ == "__main__":
    unittest.main()
