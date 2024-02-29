import unittest
import allure

from common.commonFunctions import CommonFunctions
from common.enum.client.regulatorPlatformTierType import RegulatorPlatformTierType
from common.steps.clientSteps import ClientSteps

username = ""
client_email = CommonFunctions.generate_random_email()


class TradingAccountSettingsTest(unittest.TestCase):

    def setUp(self):
        global username
        username = CommonFunctions.generate_random_email()
        cs = ClientSteps
        cs.api_ic_registration_without_trading_accounts_settings(username)

    @allure.feature('Trading Account Settings')
    @allure.story('US12345: As an IC/IB/IC Campaign user, I should be able to view the trading account settings dropdown')
    @allure.testcase('To verify if user is able to view the trading account settings dropdown on selecting mex atlantic, mt4 and standard')
    def test_IC_TC1_To_verify_if_user_is_able_to_view_the_trading_account_settings_dropdown_on_selecting_mex_atlantic_mt4_standard(self):
        regulator_platform_tier_type = RegulatorPlatformTierType.mex_atlantic_mt4_standard.value
        cs = ClientSteps
        cs.validate_trading_account_settings_dropdown_list(regulator_platform_tier_type)

    @allure.feature('Trading Account Settings')
    @allure.story('US12345: As an IC/IB/IC Campaign user, I should be able to view the trading account settings dropdown')
    @allure.testcase('To verify if user is able to view the trading account settings dropdown on selecting mex atlantic, mt5 and standard')
    def test_IC_TC2_To_verify_if_user_is_able_to_view_the_trading_account_settings_dropdown_on_selecting_mex_atlantic_mt5_standard(self):
        regulator_platform_tier_type = RegulatorPlatformTierType.mex_atlantic_mt5_standard.value
        cs = ClientSteps
        cs.validate_trading_account_settings_dropdown_list(regulator_platform_tier_type)

    def tearDown(self):
        ClientSteps.teardown("Trading Account Settings")


if __name__ == "__main__":
    unittest.main()
