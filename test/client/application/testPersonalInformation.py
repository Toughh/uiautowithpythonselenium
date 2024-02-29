import unittest
import allure

from common.commonFunctions import CommonFunctions
from common.enum.client.clientType import ClientType
from common.steps.clientSteps import ClientSteps
from test.baseTest import BaseTest

username = ""
client_email = CommonFunctions.generate_random_email()


class PersonalInformationTest(unittest.TestCase):

    def setUp(self):
        global username
        username = CommonFunctions.generate_random_email()

    @allure.feature('Personal Information')
    @allure.testcase('To_verify_db_records_when_IC_user_edit_personal_information_with_individual_client_type')
    def test_IC_TC1_To_verify_db_records_when_IC_user_edit_personal_information_with_individual_client_type(self):
        client_type = ClientType.individual.value
        cs = ClientSteps
        cs.api_ic_registration_with_trading_accounts_settings(username)
        cs.validate_ic_personal_info_records_in_db(client_type, None)

    # @allure.feature('Personal Information')
    # @allure.testcase('To_verify_db_records_when_IC_user_edit_personal_information_with_corporate_client_type')
    # def test_IC_TC2_To_verify_db_records_when_IC_user_edit_personal_information_with_corporate_client_type(self):
    #     client_type = ClientType.corporate.value
    #     cs = ClientSteps
    #     cs.api_ic_registration_with_trading_accounts_settings(username)
    #     cs.validate_ic_personal_info_records_in_db(client_type, None)
    #
    # @allure.feature('Personal Information')
    # @allure.testcase('To_verify_db_records_when_IC_user_edit_personal_information_with_joint_client_type')
    # def test_IC_TC3_To_verify_db_records_when_IC_user_edit_personal_information_with_joint_client_type(self):
    #     client_type = ClientType.joint_account.value
    #     cs = ClientSteps
    #     cs.api_ic_registration_with_trading_accounts_settings(username)
    #     cs.validate_ic_personal_info_records_in_db(client_type, None)
    #
    # @allure.feature('Personal Information')
    # @allure.testcase('To_verify_db_records_when_IC_user_edit_personal_information_with_institutional_corporate_client_type')
    # def test_IC_TC4_To_verify_db_records_when_IC_user_edit_personal_information_with_institutional_corporate_client_type(self):
    #     client_type = ClientType.institutional_corporate.value
    #     cs = ClientSteps
    #     cs.api_ic_registration_with_trading_accounts_settings(username)
    #     cs.validate_ic_personal_info_records_in_db(client_type, None)
    #
    # @allure.feature('Personal Information')
    # @allure.testcase('To verify if IC user not able to proceed to next step until fill the mandatory fields under '
    #                  'Personal Information')
    # def test_IC_TC5_To_verify_if_IC_user_not_able_to_proceed_unless_fill_personal_information(self):
    #     cs = ClientSteps
    #     cs.validate_ic_personal_info_error_message(username)
    #
    # @allure.feature('Personal Information')
    # @allure.testcase('To_verify_db_records_when_IC_campaign_user_edit_personal_information_with_individual_client_type')
    # def test_IC_Campaign_TC6_To_verify_db_records_when_IC_campaign_user_edit_personal_information_with_individual_client_type(self):
    #     client_type = ClientType.individual.value
    #     cs = ClientSteps
    #     cs.api_ic_campaign_registration_with_trading_account_settings(username)
    #     cs.validate_ic_campaign_personal_info_records_in_db(client_type, None)
    #
    # @allure.feature('Personal Information')
    # @allure.testcase('To_verify_db_records_when_IC_campaign_user_edit_personal_information_with_corporate_client_type')
    # def test_IC_Campaign_TC7_To_verify_db_records_when_IC_campaign_user_edit_personal_information_with_corporate_client_type(self):
    #     client_type = ClientType.corporate.value
    #     cs = ClientSteps
    #     cs.api_ic_campaign_registration_with_trading_account_settings(username)
    #     cs.validate_ic_campaign_personal_info_records_in_db(client_type, None)
    #
    # @allure.feature('Personal Information')
    # @allure.testcase('To_verify_db_records_when_IC_campaign_user_edit_personal_information_with_joint_client_type')
    # def test_IC_Campaign_TC8_To_verify_db_records_when_IC_campaign_user_edit_personal_information_with_joint_client_type(self):
    #     client_type = ClientType.joint_account.value
    #     cs = ClientSteps
    #     cs.api_ic_campaign_registration_with_trading_account_settings(username)
    #     cs.validate_ic_campaign_personal_info_records_in_db(client_type, None)
    #
    # @allure.feature('Personal Information')
    # @allure.testcase('To_verify_db_records_when_IC_campaign_user_edit_personal_information_with_institutional_corporate_client_type')
    # def test_IC_Campaign_TC9_To_verify_db_records_when_IC_campaign_user_edit_personal_information_with_institutional_client_type(self):
    #     client_type = ClientType.institutional_corporate.value
    #     cs = ClientSteps
    #     cs.api_ic_campaign_registration_with_trading_account_settings(username)
    #     cs.validate_ic_campaign_personal_info_records_in_db(client_type, None)
    #
    # @allure.feature('OTP')
    # @allure.testcase('To_verify_if_IC_user_is_able_to_validate_otp_under_Personal_Information')
    # def test_IC_OTP_TC10_To_verify_if_IC_user_is_able_to_validate_otp_under_Personal_Information(self):
    #     client_type = ClientType.individual.value
    #     cs = ClientSteps
    #     cs.api_ic_registration_with_trading_accounts_settings(username)
    #     cs.validate_otp_under_personal_information(client_type)
    #
    # @allure.feature('OTP')
    # @allure.testcase('To_verify_if_IB_user_is_able_to_validate_otp_under_Personal_Information')
    # def test_IB_OTP_TC11_To_verify_if_IB_user_is_able_to_validate_otp_under_Personal_Information(self):
    #     client_type = ClientType.individual.value
    #     cs = ClientSteps
    #     cs.api_ib_registration(username)
    #     cs.validate_otp_under_personal_information(client_type)
    #
    # @allure.feature('OTP')
    # @allure.testcase('To_verify_if_IC_Campaign_user_is_able_to_validate_otp_under_Personal_Information')
    # def test_IC_Campaign_OTP_TC12_To_verify_if_IC_Campaign_user_is_able_to_validate_otp_under_Personal_Information(self):
    #     client_type = ClientType.individual.value
    #     cs = ClientSteps
    #     cs.api_ic_campaign_registration_with_trading_account_settings(username)
    #     cs.validate_otp_under_personal_information(client_type)
    #
    # @allure.feature('OTP')
    # @allure.testcase('To_verify_if_IB_Client_user_is_able_to_validate_otp_under_Personal_Information')
    # def test_IB_Client_OTP_TC13_To_verify_if_IB_Client_user_is_able_to_validate_otp_under_Personal_Information(
    #         self):
    #     base_test = BaseTest
    #     base_test.ib_compliance_change_status(username, 'Approve', 'Approve', 'Approve', 'Approve', 'Approve')
    #     client_type = ClientType.individual.value
    #     cs = ClientSteps
    #     cs.validate_otp_for_ib_registered_clients(client_type, client_email)
    #
    # @allure.feature('Duplicate Registration')
    # @allure.story('US12345: As a Client, I should be able to duplicate my registration so that I can edit my personal Information')
    # @allure.testcase('To_verify_if_IC_user_with_trading_account_is_able_to_re_register')
    # def test_IC_Duplicate_Registration_TC14_To_verify_if_IC_user_with_trading_account_is_able_to_re_register(self):
    #     base_test = BaseTest
    #     base_test.ic_re_register_after_admin_approval(username, 'Approve', 'Approve', 'Approve', 'Approve', 'Approve', 'Approve')
    #     cs = ClientSteps
    #     cs.validate_personal_information_under_logged_in_user(username)
    #
    # @allure.feature('Duplicate Registration')
    # @allure.story('US12345: As a Client, I should be able to reset my personal information after re-register')
    # @allure.testcase('To_verify_if_IC_user_able_to_reset_personal_information')
    # def test_IC_Duplicate_Registration_TC15_To_verify_if_IC_user_without_trading_account_is_able_to_re_register(self):
    #     client_type = ClientType.individual.value
    #     cs = ClientSteps
    #     cs.api_ic_registration_without_trading_accounts_settings(username)
    #     cs.api_ic_duplicate_registration_without_trading_account_settings(username)
    #     cs.validate_ic_personal_info_records_in_db(client_type, None)

    def tearDown(self):
        ClientSteps.teardown("Personal Information")


if __name__ == "__main__":
    unittest.main()
