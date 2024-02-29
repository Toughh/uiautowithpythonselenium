from common.commonFunctions import CommonFunctions
import unittest
import allure

from common.steps.adminSteps import AdminSteps
from common.steps.clientSteps import ClientSteps
from test.baseTest import BaseTest

username = ""


class UploadedDocumentsTest(unittest.TestCase):

    def setUp(self):
        global username
        username = CommonFunctions.generate_random_email()

    @allure.feature('Uploaded Documents')
    @allure.story('US12345: As an IC user, I should not be able to upload any other document once approved by admin')
    @allure.testcase('To verify if IC user not able to upload any other document once approved by admin')
    def test_IC_TC1_To_verify_if_user_not_able_to_upload_any_other_document_once_approved_by_admin(self):
        base_test = BaseTest
        base_test.change_bo_id_por_status(username, "Approve", "Approve")
        ast = AdminSteps
        ast.upload_bo_documents()
        cs = ClientSteps
        cs.login_client(username)
        cs.validate_if_user_able_to_upload_documents("Approve")

    @allure.feature('Uploaded Documents')
    @allure.story('US12345: As an IC user, I should be able to upload any other document if admin has not approved yet')
    @allure.testcase('To verify if IC user able to upload any other document if not approved by admin')
    def test_IC_TC2_To_verify_if_user_able_to_upload_any_other_document_if_not_approved_by_admin(self):
        cs = ClientSteps
        cs.navigate_to_dashboard_after_filling_application_details(username)
        cs.validate_if_user_able_to_upload_documents(None)

    def tearDown(self):
        ClientSteps.teardown("Uploaded Documents")


if __name__ == "__main__":
    unittest.main()
