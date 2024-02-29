# Not completed as switching to API now due to priority
from common.commonFunctions import CommonFunctions
from common.steps.adminSteps import AdminSteps
from common.steps.clientSteps import ClientSteps
import unittest
import allure

from test.baseTest import BaseTest

username = ""
client_email = CommonFunctions.generate_random_email()


class TestWithdrawalRequestTest(unittest.TestCase):

    def setUp(self):
        global username
        username = CommonFunctions.generate_random_email()

    @allure.story('US12345: As an admin user, I should be able to withdraw request for ic user')
    @allure.testcase('To verify if admin user able to withdraw request for ic user')
    def test_IC_TC1_To_verify_if_admin_user_is_able_to_withdraw_request_for_ic_user(self):
        base_test = BaseTest
        base_test.ic_compliance_change_status(username, "Approve", "Approve", "Approve", "Approve", "Approve")
        ast = AdminSteps
        trading_account_number = ast.trading_account_number()
        cs = ClientSteps
        cs.login_client(username)
        cs.fill_withdrawal_request(trading_account_number)

    # @allure.story('US12345: As an admin user, I should be able to withdraw request for ib user')
    # @allure.testcase('To verify if admin user able to withdraw request for ib user')
    # def test_IC_TC2_To_verify_if_admin_user_is_able_to_withdraw_request_for_ib_user(self):
    #     cs = ClientSteps
    #     cs.submit_ib_application(username)
    #     ast = AdminSteps
    #     ast.validate_withdrawal_request(username)

    # def tearDown(self):
    #     ClientSteps.teardown("User Submitted Application")
    #     AdminSteps.teardown("Withdrawal Request")


if __name__ == "__main__":
    unittest.main()
