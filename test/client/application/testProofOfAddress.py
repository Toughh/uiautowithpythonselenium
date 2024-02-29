from common.commonFunctions import CommonFunctions
import unittest
import allure

from common.enum.client.clientType import ClientType
from common.steps.clientSteps import ClientSteps

username = ""


class ProofOfAddressTest(unittest.TestCase):

    def setUp(self):
        global username
        username = CommonFunctions.generate_random_email()

    @allure.feature('Application Submission')
    @allure.story('US12345: As an IB user, I should be able to submit my application with different client type')
    @allure.testcase('To verify if IB user is able to submit application without editing and land into dashboard page')
    def test_IB_TC1_To_verify_if_ib_user_is_able_to_submit_the_application_without_editing_any_details(self):
        cs = ClientSteps
        self.assertTrue(cs.is_success_mes_displayed_after_filling_ib_application(username),
                        'IB Success message is not displayed after filling the application')

    @allure.feature('Application Submission')
    @allure.testcase('To verify if IC corporate user is able to submit application with editing personal information '
                     'and land into dashboard page')
    def test_IB_TC2_To_verify_if_ib_corporate_user_is_able_to_submit_the_application_with_editing_personal_info(self):
        client_type = ClientType.corporate.value
        cs = ClientSteps
        self.assertTrue(cs.is_ib_success_mes_displayed_after_editing_personal_info(username, client_type),
                        'IB Success message is not displayed')

    @allure.feature('Application Submission')
    @allure.testcase('To verify if IC corporate user is able to submit application with editing personal information '
                     'and land into dashboard page')
    def test_IB_TC3_To_verify_if_ib_institutional_corporate_user_able_to_submit_the_application_with_editing_personal_info(self):
        client_type = ClientType.institutional_corporate.value
        cs = ClientSteps
        self.assertTrue(cs.is_ib_success_mes_displayed_after_editing_personal_info(username, client_type),
                        'IB Success message is not displayed')

    @allure.feature('Application Submission')
    @allure.testcase('To verify if IC user is able to submit application with editing personal information and land '
                     'into dashboard page')
    def test_IB_TC4_To_verify_if_ib_joint_account_is_able_to_submit_the_application_with_editing_personal_information(self):
        client_type = ClientType.joint_account.value
        cs = ClientSteps
        self.assertTrue(cs.is_ib_success_mes_displayed_after_editing_personal_info(username, client_type),
                        'IB Success message is not displayed')

    def tearDown(self):
        ClientSteps.teardown("IB Submitted Application")


if __name__ == "__main__":
    unittest.main()
