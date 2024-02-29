#  Currently not using email validation api. So skipping test
# from common.api.registration.getEmailVerificationApi import EmailVerificationApi
# from common.commonFunctions import CommonFunctions
# import unittest
# import allure
#
#
# class EmailVerificationApiTest(unittest.TestCase):
#
#     @allure.story('US12345: As a end user, I should be able to verify email from api after posting trading account '
#                   'settings so that I can continue to register myself into an application')
#     @allure.testcase('To verify if able to verify email through api')
#     def test_TC1_To_verify_if_able_to_verify_email_through_api(self):
#         username = CommonFunctions.generate_random_email()
#         EmailVerificationApi.register_ic_user(username)
#
#
# if __name__ == "__main__":
#     unittest.main()
