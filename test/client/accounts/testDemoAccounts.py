from common.commonFunctions import CommonFunctions
from common.steps.clientSteps import ClientSteps
import unittest
import allure

username = ""


class TestDemoAccounts(unittest.TestCase):

    def setUp(self):
        global username
        username = CommonFunctions.generate_random_email()

    @allure.story('US12345: As a demo user, I should be able to see demo accounts')
    @allure.testcase('To verify if demo user is able to see demo accounts after registration')
    def test_IC_TC1_To_verify_if_demo_user_is_able_to_see_demo_account_after_successful_registration(self):
        cs = ClientSteps
        cs.api_demo_registration(username)
        cs.navigate_to_demo_accounts()
        cs.validate_demo_accounts_data_in_db(username)

    def tearDown(self):
        ClientSteps.teardown('Demo Accounts')


if __name__ == "__main__":
    unittest.main()
