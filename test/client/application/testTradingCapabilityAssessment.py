from common.commonFunctions import CommonFunctions
import unittest
import allure

from common.steps.clientSteps import ClientSteps

username = ""


class TradingCapabilityAssessmentTest(unittest.TestCase):

    def setUp(self):
        global username
        username = CommonFunctions.generate_random_email()

    @allure.feature('Trading Assessment')
    @allure.testcase('To verify if IC user not able to proceed to next step until I fill trading assessment questions')
    def test_IC_TC1_To_verify_if_IC_user_not_able_to_proceed_unless_fill_trading_assessment_questions(self):
        cs = ClientSteps
        cs.validate_ic_trading_capability_assessment_error_message(username)

    def tearDown(self):
        ClientSteps.teardown("Capability Assessment")


if __name__ == "__main__":
    unittest.main()
