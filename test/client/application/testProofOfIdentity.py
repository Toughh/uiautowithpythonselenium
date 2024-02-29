# Cannot be tested at the moment because we cannot see Proof Of Identity field as per latest requirement

# from common.api.registration.postUploadFilesApi import UploadFilesApi
# from common.pojo.client.proofOfIdentity import ProofOfIdentity
# from common.setup.setup import SetupPage
# from common.commonFunctions import CommonFunctions
# from common.pageObjects.client.applicationPage import ApplicationPage
# import unittest
# import allure
#
#
# class ProofOfIdentityTest(unittest.TestCase):
#     username = CommonFunctions.generate_random_email()
#     clientType = 'Individual'
#     firstName = CommonFunctions.generate_random_first_name()
#     lastName = CommonFunctions.generate_random_last_name()
#     countryOfResidence = 'United Arab Emirates'
#     dateOfBirth = '1987-05-12'
#     email = CommonFunctions.generate_random_email()
#     mobileNumber = CommonFunctions.mob_num_with_country_code('+97155')
#     documentId = UploadFilesApi.get_file('DOC', CommonFunctions.generate_random_email(), 'actual.jpg', 'jpeg')
#
#     @allure.story('US12345: As a end user, I should be able to pick a country and select the identity type so that I am'
#                   ' able to upload the documents')
#     @allure.testcase('To verify if user is able to pick a country and select the identity type to upload the documents')
#     def test_To_verify_if_user_is_able_to_pick_a_country_and_select_the_identity_type_to_upload_documents(self):
#         self.initialize = SetupPage(self)
#         driver = self.initialize.setup(ProofOfIdentityTest.username, '1', 'AE', ProofOfIdentityTest.firstName,
#                                        ProofOfIdentityTest.lastName, '2', ProofOfIdentityTest.mobileNumber,
#                                        ProofOfIdentityTest.mobileNumber, ProofOfIdentityTest.dateOfBirth, 'true', 'AE',
#                                        '1', ProofOfIdentityTest.documentId, '', '', '', 1, 7, 1, 6, 4, 'Salary', 1,
#                                        1231, 'Live Account NJ 3.0 Step 2')
#         self.ap = ApplicationPage(driver)
#         self.ap.fill_trading_capability_questions_on_already_email_verified()
#         self.ap.fill_proof_of_identity(ProofOfIdentity('United Arab Emirates', 'Passport'))
#
#
# if __name__ == "__main__":
#     unittest.main()
