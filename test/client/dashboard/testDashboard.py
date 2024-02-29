from common.commonFunctions import CommonFunctions
import unittest
import allure

from common.enum.client.clientType import ClientType
from common.enum.client.regulatorPlatformTierType import RegulatorPlatformTierType
from common.steps.clientSteps import ClientSteps
# from test.baseTest import baseTest

username = ""
client_email = ""


class DashboardTest(unittest.TestCase):

    def setUp(self):
        global username, client_email
        username = CommonFunctions.generate_random_email()
        print(username)
        client_email = CommonFunctions.generate_random_email()

    # @allure.feature('Application Submission')
    # @allure.story(
    #     'US12345: As an IC user, I should be able to submit application with or without editing so that I can '
    #     'continue to land into dashboard page')
    # @allure.testcase('To verify if IC user is able to submit application without editing and land into dashboard page')
    # def test_IC_TC1_To_verify_if_ic_user_is_able_to_submit_the_application_without_editing_any_details(self):
    #     cs = ClientSteps
    #     self.assertEqual('Dashboard', cs.navigate_to_dashboard_after_filling_application_details(username),
    #                      'Dashboard Page not displayed')

    @allure.feature('Application Submission')
    @allure.testcase('To verify if IC user is able to submit application with editing personal information and land '
                     'into dashboard page')
    def test_IC_TC2_To_verify_if_ic_corporate_user_is_able_to_submit_the_application_with_editing_personal_information(
            self):
        client_type = ClientType.corporate.value
        cs = ClientSteps
        cs.api_ic_registration_with_trading_accounts_settings(username)
        self.assertEqual('Dashboard', cs.navigate_to_dashboard_editing_personal_info(client_type),
                         'Dashboard Page not displayed')

    # @allure.feature('Application Submission')
    # @allure.testcase('To verify if IC user is able to submit application with editing personal information and land '
    #                  'into dashboard page')
    # def test_IC_TC3_To_verify_if_ic_institutional_corporate_user_is_able_to_submit_the_application_with_editing_personal_information(
    #         self):
    #     client_type = ClientType.institutional_corporate.value
    #     cs = ClientSteps
    #     cs.api_ic_registration_with_trading_accounts_settings(username)
    #     self.assertEqual('Dashboard', cs.navigate_to_dashboard_editing_personal_info(client_type),
    #                      'Dashboard Page not displayed')
    #
    # @allure.feature('Application Submission')
    # @allure.testcase('To verify if IC user is able to submit application with editing personal information and land '
    #                  'into dashboard page')
    # def test_IC_TC4_To_verify_if_ic_joint_user_is_able_to_submit_the_application_with_editing_personal_information(
    #         self):
    #     client_type = ClientType.joint_account.value
    #     cs = ClientSteps
    #     cs.api_ic_registration_with_trading_accounts_settings(username)
    #     self.assertEqual('Dashboard', cs.navigate_to_dashboard_editing_personal_info(client_type),
    #                      'Dashboard Page not displayed')
    #
    # @allure.feature('Application Submission')
    # @allure.testcase('To verify if IC Campaign user is able to submit application with editing personal information and land '
    #                  'into dashboard page')
    # def test_IC_Campaign_TC5_To_verify_if_ic_individual_user_is_able_to_submit_the_application_with_editing_personal_information(self):
    #     client_type = ClientType.individual.value
    #     cs = ClientSteps
    #     cs.api_ic_campaign_registration_with_trading_account_settings(username)
    #     self.assertEqual('Dashboard', cs.navigate_to_dashboard_after_filling_ic_campaign_details(username, client_type, None),
    #                      'Dashboard Page not displayed')
    #
    # @allure.feature('Application Submission - CTrader')
    # @allure.testcase(
    #     'To verify if IC user is able to submit application with C-Trader editing personal information and land '
    #     'into dashboard page')
    # def test_IC_TC6_To_verify_if_ic_individual_user_is_able_to_submit_the_application_with_c_trader_editing_personal_information(
    #         self):
    #     client_type = ClientType.individual.value
    #     regulator_platform_tier_type = RegulatorPlatformTierType.mex_atlantic_c_trader_standard.value
    #     cs = ClientSteps
    #     cs.api_ic_registration_without_trading_accounts_settings(username)
    #     self.assertEqual('Dashboard',
    #                      cs.navigate_to_dashboard_after_filling_ic_details_with_c_trader(username, client_type, regulator_platform_tier_type),
    #                      'Dashboard Page not displayed')
    #
    # @allure.feature('Application Submission - CTrader')
    # @allure.testcase(
    #     'To verify if IC user is able to submit application with C-Trader editing personal information and land '
    #     'into dashboard page')
    # def test_IC_TC7_To_verify_if_ic_individual_user_is_able_to_submit_the_application_with_c_trader_editing_personal_information(
    #         self):
    #     client_type = ClientType.individual.value
    #     regulator_platform_tier_type = RegulatorPlatformTierType.mex_atlantic_c_trader_pro.value
    #     cs = ClientSteps
    #     cs.api_ic_registration_without_trading_accounts_settings(username)
    #     self.assertEqual('Dashboard',
    #                      cs.navigate_to_dashboard_after_filling_ic_details_with_c_trader(username, client_type,
    #                                                                                      regulator_platform_tier_type),
    #                      'Dashboard Page not displayed')

    # @allure.feature('Demo to Real')
    # @allure.testcase('To verify if demo user is able to open live accounts once getting converted from demo to real')
    # def test_IC_TC8_To_verify_if_demo_user_is_able_to_submit_the_application_once_converted_to_real(self):
    #     client_type = ClientType.individual.value
    #     regulator_platform_tier = RegulatorPlatformTierType.mex_atlantic_mt4_standard.value
    #     cs = ClientSteps
    #     cs.api_demo_registration(username)
    #     bt = BaseTest
    #     bt.submit_application_converting_demo_to_real_account(client_type, regulator_platform_tier)
    #     self.assertEqual('Dashboard', cs.navigate_to_dashboard(), 'Dashboard Page not displayed')
    #
    # def tearDown(self):
    #     ClientSteps.teardown("Dashboard")


if __name__ == "__main__":
    unittest.main()
