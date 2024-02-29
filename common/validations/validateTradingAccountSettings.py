import os
import yaml

from selenium.webdriver.common.by import By

from common.api.registration.postRegisterNewAccountApi import RegisterNewAccountApi
from common.data.api.dataSet.registration.registrationData import RegistrationData
from common.enum.client.currency import Currency
from common.enum.client.defaultLeverageType import DefaultLeverageType
from common.enum.client.employmentInformationType import EmploymentInformationType
from common.enum.client.sourceOfFundsType import SourceOfFundsType
from common.utility.db.onlineMexGroupDB import DatabaseUtility
from common.commonFunctions import CommonFunctions


class TradingAccountSettingsValidation:

    def __init__(self, driver):
        self.driver = driver
        self.get_app_page_loc = os.environ.get('APPLICATION_PAGE')

        with open(self.get_app_page_loc, 'r') as f:
            self.my_dict = yaml.safe_load(f)

    @staticmethod
    def validate_trading_account_settings_data(username):
        rd = RegistrationData()
        data = rd.ic_campaign_trading_settings_data(username)
        id = RegisterNewAccountApi.get_id()

        db = DatabaseUtility
        records = db.db_connection(os.environ.get('FOREX_TRADING_ACCOUNT') + str(id) + ";")
        # db_record = {'default_leverage': int(str(records['leverage']).replace('00', '')), "base_currency": records['currency_id'],
        #              "platform_version": records['platform_version'], "regulated_entity": records['regulatedEntity'],
        #              "account_tier": records['accountTier']}
        # try:
        #     if data != db_record:
        #         print("Data Mismatch in api and db!!!")
        #         assert False
        #     else:
        #         assert True
        # except TypeError:
        #     print("DB connection error!!!")

    def validate_trading_account_dropdown_list(self, regulator_platform_tier_type):
        self.validate_default_leverage_dropdown_list(regulator_platform_tier_type)
        self.validate_base_currency_dropdown_list(regulator_platform_tier_type)
        self.validate_employment_information_dropdown_list(regulator_platform_tier_type)
        self.source_of_funds_dropdown_list(regulator_platform_tier_type)

    def validate_default_leverage_dropdown_list(self, regulator_platform_tier_type):
        try:
            if regulator_platform_tier_type == "mex_atlantic_mt4_standard" or regulator_platform_tier_type == "mex_exchange_mt4_standard" or \
                    regulator_platform_tier_type == "mex_singapore_mt4_standard" or regulator_platform_tier_type == "mex_atlantic_mt5_standard" or \
                    regulator_platform_tier_type == "mex_exchange_mt5_standard" or regulator_platform_tier_type == "mex_singapore_mt5_standard":
                default_leverage = self.driver.find_element(By.ID, self.my_dict['ddSelectDefaultLeverage'])
                leverage_options = CommonFunctions.list_all_options(default_leverage)
                assert leverage_options == [DefaultLeverageType.leverage_100.value,
                                            DefaultLeverageType.leverage_200.value,
                                            DefaultLeverageType.leverage_300.value,
                                            DefaultLeverageType.leverage_400.value,
                                            DefaultLeverageType.leverage_500.value]
        except TypeError:
            print("Default Leverage options not found!!!")

    def validate_base_currency_dropdown_list(self, regulator_platform_tier_type):
        try:
            if regulator_platform_tier_type == "mex_atlantic_mt4_standard" or regulator_platform_tier_type == "mex_exchange_mt4_standard" or \
                    regulator_platform_tier_type == "mex_singapore_mt4_standard" or regulator_platform_tier_type == "mex_atlantic_mt5_standard" or \
                    regulator_platform_tier_type == "mex_exchange_mt5_standard" or regulator_platform_tier_type == "mex_singapore_mt5_standard":
                base_currency = self.driver.find_element(By.ID, self.my_dict['ddSelectBaseCurrency'])
                currency_options = CommonFunctions.list_all_options(base_currency)
                assert currency_options == [Currency.USD.value, Currency.EUR.value, Currency.GBP.value,
                                            Currency.AUD.value, Currency.CAD.value, Currency.CHF.value]
        except TypeError:
            print("Base Currency options not found!!!")

    def validate_employment_information_dropdown_list(self, regulator_platform_tier_type):
        try:
            if regulator_platform_tier_type == "mex_atlantic_mt4_standard" or regulator_platform_tier_type == "mex_exchange_mt4_standard" or \
                    regulator_platform_tier_type == "mex_singapore_mt4_standard" or regulator_platform_tier_type == "mex_atlantic_mt5_standard" or \
                    regulator_platform_tier_type == "mex_exchange_mt5_standard" or regulator_platform_tier_type == "mex_singapore_mt5_standard":
                emp_info = self.driver.find_element(By.ID, self.my_dict['ddSelectEmploymentInformation'])
                emp_info_options = CommonFunctions.list_all_options(emp_info)
                assert emp_info_options == [EmploymentInformationType.employed.value,
                                            EmploymentInformationType.retired.value,
                                            EmploymentInformationType.self_employed.value,
                                            EmploymentInformationType.student.value,
                                            EmploymentInformationType.unemployed.value]
        except TypeError:
            print("Employment Information options not found!!!")

    def source_of_funds_dropdown_list(self, regulator_platform_tier_type):
        try:
            if regulator_platform_tier_type == "mex_atlantic_mt4_standard" or regulator_platform_tier_type == "mex_exchange_mt4_standard" or \
                    regulator_platform_tier_type == "mex_singapore_mt4_standard" or regulator_platform_tier_type == "mex_atlantic_mt5_standard" or \
                    regulator_platform_tier_type == "mex_exchange_mt5_standard" or regulator_platform_tier_type == "mex_singapore_mt5_standard":
                source_of_funds = self.driver.find_element(By.ID, self.my_dict['ddSelectSourceOfFunds'])
                source_of_funds_options = CommonFunctions.list_all_options(source_of_funds)
                assert source_of_funds_options == [SourceOfFundsType.salary.value, SourceOfFundsType.savings.value,
                                                   SourceOfFundsType.investments.value, SourceOfFundsType.property_sale.value,
                                                   SourceOfFundsType.dividends.value, SourceOfFundsType.inheritance_gift.value]
        except TypeError:
            print("Source Of Funds options not found!!!")
