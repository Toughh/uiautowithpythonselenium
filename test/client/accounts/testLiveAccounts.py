from common.commonFunctions import CommonFunctions
from common.steps.clientSteps import ClientSteps
import unittest
import allure

from test.baseTest import BaseTest

username = ""


class TestLiveAccounts(unittest.TestCase):

    def setUp(self):
        global username
        username = CommonFunctions.generate_random_email()

    @allure.story('US12345: As an ic/ib or ic campaign user, I should be able to see live account Trading Account Details once '
                  'register with trading account settings')
    @allure.testcase('To verify if ic user is able to see live account trading account details once register through API')
    def test_IC_TC1_To_verify_if_ic_user_is_able_to_see_live_account_trading_account_details(self):
        cs = ClientSteps
        cs.api_ic_registration_with_trading_accounts_settings(username)
        cs.navigate_to_live_accounts()
        cs.validate_live_accounts_data_in_db(username)

    @allure.testcase('To verify if ic user is able to see live account trading account details once register through API')
    def test_IB_TC2_To_verify_if_ic_user_is_able_to_see_live_account_trading_account_details(self):
        base_test = BaseTest
        base_test.ib_application_change_status(username, "Approve", "Approve")
        cs = ClientSteps
        cs.login_client(username)
        cs.navigate_to_live_accounts()
        cs.validate_live_accounts_data_in_db(username)

    @allure.testcase('To verify if ic campaign user is able to see live account trading account details once register through API')
    def test_IC_Campaign_TC3_To_verify_if_user_is_able_to_see_live_account_trading_account_details(self):
        cs = ClientSteps
        cs.api_ic_campaign_registration_with_trading_account_settings(username)
        cs.navigate_to_live_accounts()
        cs.validate_live_accounts_data_in_db(username)

    @allure.testcase('To verify if ic campaign user is able to see live account trading account details even without passing trading account settings '
                     'through API')
    def test_IC_Campaign_TC4_To_verify_if_user_is_able_to_see_live_account_trading_account_details_even_without_passing_trading_account_settings(self):
        cs = ClientSteps
        cs.api_ic_campaign_registration_without_trading_account_settings(username)
        cs.navigate_to_live_accounts()
        cs.validate_live_accounts_data_in_db(username)

    def tearDown(self):
        ClientSteps.teardown('Live Accounts')


if __name__ == "__main__":
    unittest.main()
