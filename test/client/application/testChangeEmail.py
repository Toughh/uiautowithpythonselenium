import unittest
import allure

from common.commonFunctions import CommonFunctions
from common.steps.clientSteps import ClientSteps

username = ""
changed_email = ""


class ChangeEmailTest(unittest.TestCase):

    def setUp(self):
        global username, changed_email
        username = CommonFunctions.generate_random_email()
        changed_email = CommonFunctions.generate_random_email()

    @allure.feature('Change Email')
    @allure.story('US12345: As an IC/IB/IC Campaign user, I should be able to change email')
    @allure.testcase('To_verify_if_ic_user_is_able_to_change_username_and_re_login')
    def test_IC_TC1_To_verify_if_user_is_able_to_change_username_and_re_login(self):
        cs = ClientSteps
        cs.api_ic_registration_with_trading_accounts_settings(username)
        cs.validate_if_user_able_to_change_email(changed_email)
        cs.validate_personal_information_under_logged_in_user(changed_email)

    def tearDown(self):
        ClientSteps.teardown("Change Email")


if __name__ == "__main__":
    unittest.main()
