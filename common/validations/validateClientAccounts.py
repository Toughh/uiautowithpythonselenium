import yaml
import os

from selenium.webdriver.common.by import By
from common.api.registration.postRegisterNewAccountApi import RegisterNewAccountApi
from common.data.api.dataSet.registration.registrationData import RegistrationData
from common.helper.convertAPIValueToString import ConvertAPIValueToString
from common.utility.db.onlineMexGroupDB import DatabaseUtility


class ClientAccountsValidation:

    def __init__(self, driver):
        self.driver = driver
        self.get_accounts_page_loc = os.environ.get('ACCOUNTS_PAGE')
        with open(self.get_accounts_page_loc, 'r') as f:
            self.my_dict = yaml.safe_load(f)

    # def validate_live_accounts_trading_card(self, username, trading_account_index):
    #     boa = BackOfficeAreaPage(self.driver)
    #     admin_trading_account = boa.get_trading_account_detailed_info(username, trading_account_index)
    #     ad_trading_account_number = admin_trading_account.get('Login')
    #     # ad_balance = admin_trading_account.get('Known Balance')
    #     # ad_entity = admin_trading_account.get('User Platform')
    #     ad_currency = admin_trading_account.get('Currency')
    #     # ad_leverage = admin_trading_account.get('Leverage')
    #     # ad_platform = admin_trading_account.get('Platform Version')
    #
    #     boa.switch_to_client_portal()
    #     acc = AccountsPage(self.driver)
    #     client_trading_account = acc.get_trading_card_info()
    #     cl_trading_account_number = client_trading_account['cl_trading_account_number']
    #     print(cl_trading_account_number)
    #     cl_currency = client_trading_account['cl_currency']
    #     if ad_trading_account_number != cl_trading_account_number and ad_currency != cl_currency:
    #         assert False
    #     else:
    #         assert True

    def validate_live_accounts_trading_card_details_in_db(self, username):
        rd = RegistrationData()
        rd.ic_campaign_trading_settings_data(username)
        id = RegisterNewAccountApi.get_id()

        trading_account_number = self.driver.find_element(By.CLASS_NAME,
                                                          self.my_dict['lblTradingAccountNumber']).text.replace(
            "(Read-Only)", "")
        trading_account_number_actual =
        account_tier = self.driver.find_element(By.XPATH, self.my_dict['lblTradingAccountTier']).text
        platform = self.driver.find_element(By.CLASS_NAME, self.my_dict['lblTradingAccountNumberPlatform']).text
        regulator = self.driver.find_element(By.CLASS_NAME, self.my_dict['lblTradingAccountNumberRegulatorName']).text
        leverage = self.driver.find_element(By.CLASS_NAME, self.my_dict['lblTradingAccountNumberLeverage']).text
        currency = self.driver.find_element(By.CLASS_NAME, self.my_dict['lblTradingAccountCurrency']).text

        live_account_app_data = {'trading_account_number': int(trading_account_number), 'account_tier': account_tier,
                                 'platform': platform, 'regulator': regulator, 'leverage': int(leverage),
                                 'currency': currency}

        forex_trading_account = os.environ.get('FOREX_TRADING_ACCOUNT')

        db = DatabaseUtility
        records = db.db_connection(forex_trading_account + str(id) + ";")
        account_tier_db = records['accountTier']
        account_tier_string_val = ConvertAPIValueToString.convert_account_tier(account_tier_db)
        platform_db = records['platform_version']
        platform_string_val = ConvertAPIValueToString.convert_platform_version(platform_db)
        regulator_db = records['regulatedEntity']
        regulator_string_val = ConvertAPIValueToString.convert_regulated_entity(regulator_db)
        currency_db = records['currency_id']
        currency_string_val = ConvertAPIValueToString.convert_base_currency(currency_db)

        db_record = {'trading_account_number': records['login'], 'account_tier': account_tier_string_val,
                     'platform': platform_string_val,
                     'regulator': regulator_string_val, 'leverage': records['leverage'],
                     'currency': currency_string_val}

        try:
            if live_account_app_data != db_record:
                print("Data Mismatch in api and db!!!")
                assert False
            else:
                assert True
        except TypeError:
            print("DB connection error!!!")

    def validate_demo_accounts_trading_card_details_in_db(self, username):
        rd = RegistrationData()
        rd.demo_trading_settings_data(username)
        id = RegisterNewAccountApi.get_id()

        trading_account_number = self.driver.find_element(By.CLASS_NAME,
                                                          self.my_dict['lblTradingAccountNumber']).text
        account_tier = self.driver.find_element(By.XPATH, self.my_dict['lblTradingAccountTier']).text
        platform = self.driver.find_element(By.CLASS_NAME, self.my_dict['lblTradingAccountNumberPlatform']).text
        regulator = self.driver.find_element(By.CLASS_NAME, self.my_dict['lblTradingAccountNumberRegulatorName']).text
        leverage = self.driver.find_element(By.CLASS_NAME, self.my_dict['lblTradingAccountNumberLeverage']).text
        currency = self.driver.find_element(By.CLASS_NAME, self.my_dict['lblTradingAccountCurrency']).text

        demo_account_app_data = {'trading_account_number': int(trading_account_number), 'account_tier': account_tier,
                                 'platform': platform, 'regulator': regulator, 'leverage': int(leverage),
                                 'currency': currency}

        forex_trading_account = os.environ.get('FOREX_TRADING_ACCOUNT')

        db = DatabaseUtility
        records = db.db_connection(forex_trading_account + str(id) + ";")
        account_tier_db = records['accountTier']
        account_tier_string_val = ConvertAPIValueToString.convert_account_tier(account_tier_db)
        platform_db = records['platform_version']
        platform_string_val = ConvertAPIValueToString.convert_platform_version(platform_db)
        regulator_db = records['regulatedEntity']
        regulator_string_val = ConvertAPIValueToString.convert_regulated_entity(regulator_db)
        currency_db = records['currency_id']
        currency_string_val = ConvertAPIValueToString.convert_base_currency(currency_db)

        db_record = {'trading_account_number': records['login'], 'account_tier': account_tier_string_val,
                     'platform': platform_string_val,
                     'regulator': regulator_string_val, 'leverage': records['leverage'],
                     'currency': currency_string_val}

        try:
            if demo_account_app_data != db_record:
                print("Data Mismatch in api and db!!!")
                assert False
            else:
                assert True
        except TypeError:
            print("DB connection error!!!")
