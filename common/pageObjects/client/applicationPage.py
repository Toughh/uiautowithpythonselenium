import os.path
import time
import yaml

from selenium.common.exceptions import NoSuchElementException, InvalidSelectorException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.commonFunctions import CommonFunctions
from common.data.application.personalInformationData import PersonalInformationData
from common.validations.validateClientApplication import ClientPageValidation
from common.validations.validateLogin import LoginValidation
from common.validations.validateTradingAccountSettings import TradingAccountSettingsValidation


class ApplicationPage:

    def __init__(self, driver):
        self.driver = driver
        self.get_app_page_loc = os.environ.get('APPLICATION_PAGE')

        with open(self.get_app_page_loc, 'r') as f:
            self.my_dict = yaml.safe_load(f)

    def edit_personal_info(self):
        try:
            time.sleep(8)
            self.processing_bar()
            edit = self.driver.find_element(By.CLASS_NAME, self.my_dict['btnEditPersonalInfo'])
            edit.click()
            self.processing_bar()
        except NoSuchElementException:
            pass

    def processing_bar(self):
        process = WebDriverWait(self.driver, 60).until(
            EC.invisibility_of_element_located([By.CLASS_NAME, self.my_dict['lblProcessing']]))
        return process

    def check_if_next_is_displayed(self, index):
        try:
            next_btn = self.driver.find_element(By.XPATH, '(//*[@id="submit"])[' + str(index) + ']')
            if next_btn.is_displayed():
                next_btn.click()
        except NoSuchElementException as e:
            print("Next button element not found or DOM not loaded!!!", e)

    def click_on_application(self):
        application = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable([By.CLASS_NAME, self.my_dict['lnkApplication']]))
        application.click()

    def clear_personal_info_fields(self):
        self.driver.find_element(By.CLASS_NAME, self.my_dict['lnkApplication']).click()
        self.edit_personal_info()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located([
            By.ID, self.my_dict['ddClientType']]))
        self.driver.find_element(By.CLASS_NAME, self.my_dict['txtFirstName']).clear()
        self.driver.find_element(By.CLASS_NAME, self.my_dict['txtLastName']).clear()
        self.driver.find_element(By.CLASS_NAME, self.my_dict['dpDateOfBirth']).clear()
        self.driver.find_element(By.CLASS_NAME, self.my_dict['txtMobileNumber']).clear()

    def navigate_to_personal_information_page(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located([
            By.CLASS_NAME, self.my_dict['lnkApplication']]))
        self.driver.find_element(By.CLASS_NAME, self.my_dict['lnkApplication']).click()
        self.edit_personal_info()

    def validate_personal_info_ic_user_with_api(self):
        self.navigate_to_personal_information_page()
        ap = ClientPageValidation(self.driver)
        ap.validate_ic_personal_information_contents_with_api()

    def validate_personal_info_ic_campaign_user_with_api(self):
        self.navigate_to_personal_information_page()
        ap = ClientPageValidation(self.driver)
        ap.validate_ic_campaign_personal_information_contents_with_api()

    def validate_personal_info_ib_user_with_api(self):
        self.navigate_to_personal_information_page()
        ap = ClientPageValidation(self.driver)
        ap.validate_ib_personal_information_contents_with_api()

    def validate_personal_info_ic_error_message(self):
        self.clear_personal_info_fields()
        self.submit_personal_info()
        ap = ClientPageValidation(self.driver)
        ap.validate_personal_information_error_mes()

    def validate_trading_capability_assessment_ic_error_message(self):
        self.driver.find_element(By.CLASS_NAME, self.my_dict['lnkApplication']).click()
        self.check_if_next_is_displayed(1)
        ap = ClientPageValidation(self.driver)
        ap.validate_trading_assessment_error_mes()

    def click_application(self):
        try:
            application = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable([By.CLASS_NAME, self.my_dict['lnkApplication']]))
            application.click()
        except NoSuchElementException:
            print("Application link not found!!!")

    def select_client_type(self, personal_info):
        self.edit_personal_info()
        client_type = self.driver.find_element(By.ID, self.my_dict['ddSelectClientType'])
        self.driver.execute_script(CommonFunctions.set_element_attribute('realType'), client_type)
        CommonFunctions.select_values(client_type, personal_info.get_client_type())

    def first_name(self, personal_info):
        first_name = self.driver.find_element(By.CLASS_NAME, self.my_dict['txtFirstName'])
        first_name.clear()
        first_name.send_keys(personal_info.get_first_name() + Keys.INSERT)

    def last_name(self, personal_info):
        last_name = self.driver.find_element(By.CLASS_NAME, self.my_dict['txtLastName'])
        last_name.clear()
        last_name.send_keys(personal_info.get_last_name() + Keys.INSERT)

    def select_country_of_residence(self, personal_info):
        country_residence = self.driver.find_element(By.ID, self.my_dict['ddSelectCountryOfResidence'])
        self.driver.execute_script(CommonFunctions.set_element_attribute('country'), country_residence)
        CommonFunctions.select_values(country_residence, personal_info.get_country_of_residence())

    def date_of_birth(self, personal_info):
        date_of_birth = self.driver.find_element(By.CLASS_NAME, self.my_dict['dpDateOfBirth'])
        date_of_birth.clear()
        date_of_birth.click()
        date_of_birth.send_keys(personal_info.get_date_of_birth() + Keys.TAB)

    def mobile_number(self, personal_info):
        try:
            mobile_number = self.driver.find_element(By.CLASS_NAME, self.my_dict['txtMobileNumber'])
            mobile_number.clear()
            mobile_number.send_keys(personal_info.get_mobile_number() + Keys.INSERT)
            check = self.driver.find_element(By.ID, self.my_dict['cbOtp'])
            if check.is_displayed():
                check.click()
        except NoSuchElementException:
            print(NoSuchElementException)

    def send_otp(self, personal_info):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located([By.CLASS_NAME, self.my_dict['btnSendOtp']]))
        send_otp = self.driver.find_element(By.CLASS_NAME, self.my_dict['btnSendOtp'])
        self.driver.execute_script("arguments[0].click();", send_otp)
        self.processing_bar()
        self.driver.find_element(By.ID, self.my_dict['txtOtp']).send_keys(
            personal_info.get_send_otp() + Keys.INSERT)

    def select_expected_deposit(self, personal_info):
        expected_deposit = self.driver.find_element(By.ID, self.my_dict['ddSelectExpectedDeposit'])
        self.driver.execute_script(CommonFunctions.set_element_attribute('expectedFirstDeposit'), expected_deposit)
        CommonFunctions.select_values(expected_deposit, personal_info.get_expected_deposit())

    def select_expected_client_deposit(self, personal_info):
        expected_client_deposit = self.driver.find_element(By.ID, self.my_dict['ddSelectExpectedClientDeposit'])
        self.driver.execute_script(CommonFunctions.set_element_attribute('expectedClientDeposit'),
                                   expected_client_deposit)
        CommonFunctions.select_values(expected_client_deposit, personal_info.get_expected_client_deposit())

    def select_expected_no_of_clients(self, personal_info):
        expected_no_of_client = self.driver.find_element(By.ID, self.my_dict['ddSelectExpectedNoOfClients'])
        self.driver.execute_script(CommonFunctions.set_element_attribute('expectedNumberOfClients'),
                                   expected_no_of_client)
        CommonFunctions.select_values(expected_no_of_client, personal_info.get_expected_no_of_client())

    def ja_second_applicant_first_name(self, personal_info):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located([By.CLASS_NAME, self.my_dict['txtJAFirstName']]))
        ja_first_name = self.driver.find_element(By.CLASS_NAME, self.my_dict['txtJAFirstName'])
        ja_first_name.clear()
        ja_first_name.send_keys(personal_info.get_second_applicant_first_name() + Keys.INSERT)

    def ja_second_applicant_last_name(self, personal_info):
        ja_last_name = self.driver.find_element(By.CLASS_NAME, self.my_dict['txtJALastName'])
        ja_last_name.clear()
        ja_last_name.send_keys(personal_info.get_second_applicant_last_name() + Keys.INSERT)

    def select_ja_country_of_residence(self, personal_info):
        joint_country_residence = self.driver.find_element(By.ID, self.my_dict['ddSelectJACountryOfResidence'])
        self.driver.execute_script(CommonFunctions.set_element_attribute('jointCountry'), joint_country_residence)
        CommonFunctions.select_values(joint_country_residence, personal_info.get_joint_country_of_residence())

    def ja_date_of_birth(self, personal_info):
        ja_dob = self.driver.find_element(By.CLASS_NAME, self.my_dict['txtJADateOfBirth'])
        ja_dob.clear()
        ja_dob.click()
        ja_dob.send_keys(personal_info.get_date_of_birth() + Keys.TAB)

    def corporate_name(self, personal_info):
        corp_name = self.driver.find_element(By.CLASS_NAME, self.my_dict['txtCorporateName'])
        corp_name.clear()
        corp_name.send_keys(personal_info.get_first_name() + Keys.INSERT)

    def legal_entity_identifier(self, personal_info):
        legal_identifier = self.driver.find_element(By.CLASS_NAME, self.my_dict['txtLegalEntityIdentifier'])
        legal_identifier.clear()
        legal_identifier.send_keys(personal_info.get_first_name() + Keys.INSERT)

    def set_personal_info_common_details(self, personal_info):
        self.select_client_type(personal_info)
        self.first_name(personal_info)
        self.last_name(personal_info)
        self.select_country_of_residence(personal_info)
        self.date_of_birth(personal_info)
        # self.mobile_number(personal_info)
        # self.send_otp(personal_info)

    def set_ic_individual_institutional_corporate_personal_info_details(self, personal_info):
        self.set_personal_info_common_details(personal_info)
        self.select_expected_deposit(personal_info)

    def set_ic_joint_account_personal_info_details(self, personal_info):
        self.first_name(personal_info)
        self.last_name(personal_info)
        self.select_country_of_residence(personal_info)
        self.date_of_birth(personal_info)
        # self.mobile_number(personal_info)
        # self.send_otp(personal_info)
        self.select_expected_deposit(personal_info)
        self.select_client_type(personal_info)
        self.ja_second_applicant_first_name(personal_info)
        self.ja_second_applicant_last_name(personal_info)
        self.ja_date_of_birth(personal_info)
        self.select_ja_country_of_residence(personal_info)

    def set_ic_corporate_personal_info_details(self, personal_info):
        self.select_client_type(personal_info)
        self.corporate_name(personal_info)
        self.legal_entity_identifier(personal_info)
        self.select_expected_deposit(personal_info)
        self.date_of_birth(personal_info)
        self.select_country_of_residence(personal_info)
        # self.mobile_number(personal_info)
        # self.send_otp(personal_info)

    def set_ib_individual_institutional_corporate_personal_info_details(self, personal_info):
        self.set_personal_info_common_details(personal_info)
        self.select_expected_client_deposit(personal_info)
        self.select_expected_no_of_clients(personal_info)

    def set_ib_joint_account_personal_info_details(self, personal_info):
        self.set_ib_individual_institutional_corporate_personal_info_details(personal_info)
        self.ja_second_applicant_first_name(personal_info)
        self.ja_second_applicant_last_name(personal_info)
        self.select_ja_country_of_residence(personal_info)
        self.ja_date_of_birth(personal_info)

    def set_ib_corporate_personal_info_details(self, personal_info):
        self.select_client_type(personal_info)
        self.corporate_name(personal_info)
        self.legal_entity_identifier(personal_info)
        self.select_country_of_residence(personal_info)
        self.date_of_birth(personal_info)
        # self.mobile_number(personal_info)
        # self.send_otp(personal_info)
        self.select_expected_client_deposit(personal_info)
        self.select_expected_no_of_clients(personal_info)

    def fill_ic_personal_info_with_individual_institutional_corporate(self, personal_info):
        self.set_ic_individual_institutional_corporate_personal_info_details(personal_info)
        self.submit_personal_info()

    def fill_ic_personal_info_with_corporate(self, personal_info):
        self.set_ic_corporate_personal_info_details(personal_info)
        self.submit_personal_info()

    def fill_ic_personal_info_details_with_joint_account(self, personal_info):
        self.set_ic_joint_account_personal_info_details(personal_info)
        self.submit_personal_info()

    def fill_ib_personal_info_with_individual_institutional_corporate(self, personal_info):
        self.set_ib_individual_institutional_corporate_personal_info_details(personal_info)
        self.submit_personal_info()

    def fill_ib_personal_info_with_corporate(self, personal_info):
        self.set_ib_corporate_personal_info_details(personal_info)
        self.submit_personal_info()

    def fill_ib_personal_info_details_with_joint_account(self, personal_info):
        self.set_ib_joint_account_personal_info_details(personal_info)
        self.submit_personal_info()

    def click_next(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable([By.CLASS_NAME, self.my_dict['btnFinish']]))
        self.driver.find_element(By.CLASS_NAME, self.my_dict['btnFinish']).click()

    def submit_personal_info(self):
        self.processing_bar()
        # time.sleep(20)
        # self.driver.execute_script("arguments[0].click();", self.driver.find_element(self.driver.find_element(By.CLASS_NAME, "text-container webchat-sneak-peek__message text-container--bot")))
        # self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div").click()
        WebDriverWait(self.driver, 40).until(
            EC.visibility_of_element_located([By.CLASS_NAME, self.my_dict['btnPINext']]))
        time.sleep(5)
        submit = ActionChains(self.driver).move_to_element(self.driver.find_element(By.CLASS_NAME, self.my_dict['btnPINext'])).click().perform()
        self.processing_bar()
        return submit

    def submit_trading_account_settings(self):
        click_next = WebDriverWait(self.driver, 40).until(
            EC.element_to_be_clickable([By.ID, self.my_dict['btnNextTradingAccount']]))
        self.driver.execute_script("arguments[0].click();", click_next)
        self.processing_bar()

    def mex_atlantic(self):
        try:
            self.processing_bar()
            mex_atlantic = self.driver.find_element(By.XPATH, self.my_dict['btnMexAtlantic'])
            if mex_atlantic.is_displayed():
                mex_atlantic.click()
        except TypeError:
            print('mex_atlantic is not displayed')

    def mex_exchange(self):
        self.driver.find_element(By.ID, self.my_dict['btnMexExchange']).click()

    def mex_pacific(self):
        self.driver.find_element(By.ID, self.my_dict['btnMexPacific']).click()

    def mex_singapore(self):
        self.driver.find_element(By.ID, self.my_dict['btnMexSingapore']).click()

    def mt4(self):
        mt4 = self.driver.find_element(By.ID, self.my_dict['btnMt4'])
        mt4.click()

    def mt5(self):
        try:
            mt5 = self.driver.find_element(By.ID, self.my_dict['btnMt5'])
            if mt5.is_displayed():
                mt5.click()
        except TypeError:
            print('mt5 is not displayed')

    def c_trader(self):
        c_trader = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located([By.CSS_SELECTOR, self.my_dict['btnCTrader']]))
        # c_trader = self.driver.find_element(By.ID, self.my_dict['btnCTrader'])
        c_trader.click()

    def standard(self):
        try:
            standard = self.driver.find_element(By.CSS_SELECTOR, self.my_dict['btnStandard'])
            if standard.is_displayed():
                standard.click()
        except TypeError:
            print('standard is not displayed')

    def pro(self):
        try:
            pro = self.driver.find_element(By.ID, self.my_dict['btnPro'])
            if pro.is_displayed():
                pro.click()
        except TypeError:
            print('pro is not displayed')

    def ecn(self):
        try:
            ecn = self.driver.find_element(By.ID, self.my_dict['btnEcn'])
            if ecn.is_displayed():
                ecn.click()
        except TypeError:
            print('ecn is not displayed')

    def mex_sports(self):
        try:
            mex_sports = self.driver.find_element(By.ID, self.my_dict['btnMexSports'])
            if mex_sports.is_displayed():
                mex_sports.click()
        except TypeError:
            print('mex sports is not displayed')

    def regulated_entity_mt4_standard(self, regulator_platform_tier_type, trading_account_settings):
        try:
            if regulator_platform_tier_type == "mex_atlantic_mt4_standard":
                self.mex_atlantic()
            elif regulator_platform_tier_type == "mex_exchange_mt4_standard":
                self.mex_exchange()
            elif regulator_platform_tier_type == "mex_singapore_mt4_standard":
                self.mex_singapore()
        except TypeError:
            print(regulator_platform_tier_type + " does not exist!!!")
        self.mt4()
        self.standard()
        self.select_default_leverage(trading_account_settings)
        self.select_source_of_funds(trading_account_settings)
        self.select_employment_information(trading_account_settings)
        self.select_base_currency(trading_account_settings)

    def regulated_entity_mt4_pro(self, regulator_entity, trading_account_settings):
        if regulator_entity == 'mex_atlantic_mt4_pro':
            self.mex_atlantic()
        elif regulator_entity == 'mex_exchange_mt4_pro':
            self.mex_exchange()
        elif regulator_entity == 'mex_singapore_mt4_pro':
            self.mex_singapore()
        self.mt4()
        self.pro()
        self.select_default_leverage(trading_account_settings)
        self.select_base_currency(trading_account_settings)
        self.select_employment_information(trading_account_settings)
        self.select_source_of_funds(trading_account_settings)

    def regulated_entity_mt4_ecn(self, regulator_entity, trading_account_settings):
        if regulator_entity == 'mex_atlantic_mt4_ecn':
            self.mex_atlantic()
        elif regulator_entity == 'mex_exchange_mt4_ecn':
            self.mex_exchange()
        elif regulator_entity == 'mex_singapore_mt4_ecn':
            self.mex_singapore()
        self.mt4()
        self.ecn()
        self.select_default_leverage(trading_account_settings)
        self.select_base_currency(trading_account_settings)
        self.select_employment_information(trading_account_settings)
        self.select_source_of_funds(trading_account_settings)

    def regulated_entity_mt5_standard(self, regulator_entity, trading_account_settings):
        if regulator_entity == 'mex_atlantic_mt5_standard':
            self.mex_atlantic()
        elif regulator_entity == 'mex_exchange_mt5_standard':
            self.mex_exchange()
        elif regulator_entity == 'mex_singapore_mt5_standard':
            self.mex_singapore()
        self.mt5()
        self.standard()
        self.select_default_leverage(trading_account_settings)
        self.select_base_currency(trading_account_settings)
        self.select_employment_information(trading_account_settings)
        self.select_source_of_funds(trading_account_settings)

    def regulated_entity_mt5_pro(self, regulator_entity, trading_account_settings):
        if regulator_entity == 'mex_atlantic_mt5_pro':
            self.mex_atlantic()
        elif regulator_entity == 'mex_exchange_mt5_pro':
            self.mex_exchange()
        elif regulator_entity == 'mex_singapore_mt5_pro':
            self.mex_singapore()
        self.mt5()
        self.pro()
        self.select_default_leverage(trading_account_settings)
        self.select_base_currency(trading_account_settings)
        self.select_employment_information(trading_account_settings)
        self.select_source_of_funds(trading_account_settings)

    def regulated_entity_mt5_ecn(self, regulator_entity, trading_account_settings):
        if regulator_entity == 'mex_atlantic_mt5_ecn':
            self.mex_atlantic()
        elif regulator_entity == 'mex_exchange_mt5_ecn':
            self.mex_exchange()
        elif regulator_entity == 'mex_singapore_mt5_ecn':
            self.mex_singapore()
        self.mt5()
        self.ecn()
        self.select_default_leverage(trading_account_settings)
        self.select_base_currency(trading_account_settings)
        self.select_employment_information(trading_account_settings)
        self.select_source_of_funds(trading_account_settings)

    def regulated_entity_mt5_mex_sports(self, regulator_entity, trading_account_settings):
        if regulator_entity == 'mex_pacific_mt5_mex_sports':
            self.mex_pacific()
        self.mt5()
        self.mex_sports()
        self.select_default_leverage(trading_account_settings)
        self.select_base_currency(trading_account_settings)
        self.select_employment_information(trading_account_settings)
        self.select_source_of_funds(trading_account_settings)

    def regulated_entity_c_trader_standard_or_pro(self, regulator_entity, trading_account_settings):
        if regulator_entity == 'mex_atlantic_c_trader_standard':
            self.mex_atlantic()
            self.c_trader()
            self.standard()
        elif regulator_entity == 'mex_atlantic_c_trader_pro':
            self.mex_atlantic()
            self.c_trader()
            self.pro()
        self.select_default_leverage(trading_account_settings)
        self.select_base_currency(trading_account_settings)
        self.select_employment_information(trading_account_settings)
        self.select_source_of_funds(trading_account_settings)

    def fill_trading_account_settings(self, regulator_platform_tier_type, trading_account_settings):
        try:
            if regulator_platform_tier_type == "mex_atlantic_mt4_standard" or regulator_platform_tier_type == "mex_exchange_mt4_standard" or \
                    regulator_platform_tier_type == "mex_singapore_mt4_standard":
                self.regulated_entity_mt4_standard(regulator_platform_tier_type, trading_account_settings)
            elif regulator_platform_tier_type == 'mex_atlantic_mt5_standard' or regulator_platform_tier_type == 'mex_exchange_mt5_standard' or \
                    regulator_platform_tier_type == 'mex_singapore_mt5_standard':
                self.regulated_entity_mt5_standard(regulator_platform_tier_type, trading_account_settings)
            elif regulator_platform_tier_type == 'mex_atlantic_mt4_pro' or regulator_platform_tier_type == 'mex_exchange_mt4_pro' or \
                    regulator_platform_tier_type == 'mex_singapore_mt4_pro':
                self.regulated_entity_mt4_pro(regulator_platform_tier_type, trading_account_settings)
            elif regulator_platform_tier_type == 'mex_atlantic_mt5_pro' or regulator_platform_tier_type == 'mex_exchange_mt5_pro' or \
                    regulator_platform_tier_type == 'mex_singapore_mt5_pro':
                self.regulated_entity_mt5_pro(regulator_platform_tier_type, trading_account_settings)
            elif regulator_platform_tier_type == 'mex_atlantic_mt4_ecn' or regulator_platform_tier_type == 'mex_exchange_mt4_ecn' or \
                    regulator_platform_tier_type == 'mex_singapore_mt4_ecn':
                self.regulated_entity_mt4_ecn(regulator_platform_tier_type, trading_account_settings)
            elif regulator_platform_tier_type == 'mex_atlantic_mt5_ecn' or regulator_platform_tier_type == 'mex_exchange_mt5_ecn' or \
                    regulator_platform_tier_type == 'mex_singapore_mt5_ecn':
                self.regulated_entity_mt5_ecn(regulator_platform_tier_type, trading_account_settings)
            elif regulator_platform_tier_type == 'mex_atlantic_c_trader_standard':
                self.regulated_entity_c_trader_standard_or_pro(regulator_platform_tier_type, trading_account_settings)
            elif regulator_platform_tier_type == 'mex_atlantic_c_trader_pro':
                self.regulated_entity_c_trader_standard_or_pro(regulator_platform_tier_type, trading_account_settings)
            elif regulator_platform_tier_type == 'mex_pacific_mt5_mex_sports':
                self.regulated_entity_mt5_mex_sports(regulator_platform_tier_type, trading_account_settings)
            else:
                return 'regulated_entity: ' + regulator_platform_tier_type + 'does not exist.'
        except TypeError:
            print(regulator_platform_tier_type + " does not exist!!!")

    def fill_trading_account_settings_and_submit(self, regulator_platform_tier_type, trading_account_settings):
        self.processing_bar()
        self.fill_trading_account_settings(regulator_platform_tier_type, trading_account_settings)
        self.submit_trading_account_settings()

    def validate_db_for_trading_account_settings(self, username):
        trading_acc_validation = TradingAccountSettingsValidation(self.driver)
        trading_acc_validation.validate_trading_account_settings_data(username)

    def select_default_leverage(self, trading_account_settings):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located([By.ID, self.my_dict['ddDefaultLeverage']]))
        default_leverage = self.driver.find_element(By.ID, self.my_dict['ddDefaultLeverage'])
        self.driver.execute_script(CommonFunctions.set_element_attribute('trading_account_settings_defaultLeverage'),
                                   default_leverage)
        CommonFunctions.select_values(self.driver.find_element(By.ID, self.my_dict['ddSelectDefaultLeverage']),
                                      trading_account_settings.get_default_leverage())

    def select_base_currency(self, trading_account_settings):
        try:
            base_currency = self.driver.find_element(By.ID, self.my_dict['ddBaseCurrency'])
            if base_currency.is_displayed():
                self.driver.execute_script(CommonFunctions.set_element_attribute('trading_account_settings_baseCurrency'),
                                           base_currency)
                CommonFunctions.select_values(self.driver.find_element(By.ID, self.my_dict['ddSelectBaseCurrency']),
                                              trading_account_settings.get_base_currency())
        except TypeError:
            print('base currency is not displayed')

    def select_employment_information(self, trading_account_settings):
        employment_information = self.driver.find_element(By.ID, self.my_dict['ddEmploymentInformation'])
        self.driver.execute_script(CommonFunctions.set_element_attribute('trading_account_settings_employmentInformation'),
                                   employment_information)
        CommonFunctions.select_values(self.driver.find_element(By.ID, self.my_dict['ddSelectEmploymentInformation']),
                                      trading_account_settings.get_employment_information())

    def select_source_of_funds(self, trading_account_settings):
        source_of_funds = self.driver.find_element(By.ID, self.my_dict['ddSourceOfFunds'])
        self.driver.execute_script(CommonFunctions.set_element_attribute('trading_account_settings_sourceOfFunds'),
                                   source_of_funds)
        CommonFunctions.select_values(self.driver.find_element(By.ID, self.my_dict['ddSelectSourceOfFunds']),
                                      trading_account_settings.get_source_of_funds())

    def fill_trading_capability_questions_on_already_email_verified(self):
        try:
            time.sleep(8)
            pid = PersonalInformationData()
            size = pid.trading_capability_assessment()
            for i in range(1, size):
                self.driver.execute_script("arguments[0].click();",
                                           self.driver.find_element(By.ID, self.my_dict['asq' + str(i)]))
                self.driver.execute_script("arguments[0].click();",
                                           self.driver.find_element(By.CLASS_NAME, self.my_dict['btnNext']))
        except TypeError as e:
            print("DOM not loaded!!!", e)
        self.processing_bar()

    def fill_trading_capability_assessment(self):
        self.fill_trading_capability_questions_on_already_email_verified()

    def pick_a_country(self, proof_of_identity):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located([By.ID, self.my_dict['ddPickACountry']]))
        country = self.driver.find_element(By.ID, self.my_dict['ddPickACountry'])
        self.driver.execute_script(CommonFunctions.set_element_attribute('proofOfIdentityCountries'), country)
        CommonFunctions.select_values(self.driver.find_element(By.ID, self.my_dict['ddSelectPickACountry']),
                                      proof_of_identity.get_pick_a_country())

    def identity_type(self, proof_of_identity):
        self.processing_bar()
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located([By.ID, self.my_dict['ddIdentityType']]))
        identity_type = self.driver.find_element(By.ID, self.my_dict['ddIdentityType'])
        self.driver.execute_script(CommonFunctions.set_element_attribute('documentTypeSelect'), identity_type)
        CommonFunctions.select_values(self.driver.find_element(By.ID, self.my_dict['ddSelectIdentityType']),
                                      proof_of_identity.get_identity_type())

    def upload_documents(self):
        filepath = os.environ.get('UPLOAD_FILE')
        filename = filepath + str('fakePassport.jpg')
        try:
            self.driver.find_element(By.XPATH, self.my_dict['btnProofOfIdentityUpload1']).click()
            CommonFunctions.upload_files(filename)
            ok = WebDriverWait(self.driver, 60).until(
                EC.visibility_of_element_located([By.CLASS_NAME, self.my_dict['btnOk']]))
            ok.click()
            upload2 = self.driver.find_element(By.XPATH, self.my_dict['btnProofOfIdentityUpload2'])
            if upload2.is_displayed():
                upload2.click()
                CommonFunctions.upload_files(filename)
                ok = WebDriverWait(self.driver, 60).until(
                    EC.visibility_of_element_located([By.CLASS_NAME, self.my_dict['btnOk']]))
                ok.click()
        except FileNotFoundError:
            print("File not found!!!")

    def submit_proof_of_identity(self):
        proof_of_identity_next = WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable([By.XPATH, self.my_dict['btnProofOfIdentity']]))
        self.driver.execute_script("arguments[0].click();", proof_of_identity_next)
        self.processing_bar()

    def upload_proof_of_identity_and_submit(self, proof_of_identity):
        self.pick_a_country(proof_of_identity)
        self.identity_type(proof_of_identity)
        self.upload_documents()
        self.submit_proof_of_identity()

    def upload_proof_of_address(self):
        filename = os.environ.get('UPLOAD_FILE') + str('fakePassport.jpg')
        print(filename)
        upload_docs = WebDriverWait(self.driver, 80).until(
            EC.element_to_be_clickable([By.XPATH, self.my_dict['btnUtilityBillUpload']]))
        upload_docs.click()
        CommonFunctions.upload_files(filename)
        ok = WebDriverWait(self.driver, 80).until(
            EC.visibility_of_element_located([By.CLASS_NAME, self.my_dict['btnOk']]))
        ok.click()
        ApplicationPage.click_finish(self)

    def click_finish(self):
        self.driver.execute_script("arguments[0].click();",
                                   self.driver.find_element(By.CLASS_NAME, self.my_dict['btnFinish']))

    def if_upload_address_is_displayed(self):
        WebDriverWait(self.driver, 25).until(
            EC.visibility_of_element_located([By.XPATH, self.my_dict['btnUtilityBillUpload']]))
        return self.driver.find_element(By.XPATH, self.my_dict['btnUtilityBillUpload']).is_displayed()

    def ib_success_mes(self):
        mes = WebDriverWait(self.driver, 25).until(
            EC.presence_of_element_located([By.CSS_SELECTOR, self.my_dict['lblIbSuccessMes']]))
        return mes

    def validate_personal_info_records_in_db_based_on_client_type(self, client_type, client_email):
        vca = ClientPageValidation(self.driver)
        vca.validate_personal_info_records_in_db(client_type, client_email)

    def validate_otp(self, client_type):
        ic_personal_info_data = PersonalInformationData.personal_info(client_type)
        self.date_of_birth(ic_personal_info_data)
        self.mobile_number(ic_personal_info_data)
        vca = ClientPageValidation(self.driver)
        vca.validate_otp()

    def click_logged_in_user(self):
        logged_in_user = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable([By.CLASS_NAME, self.my_dict['lblUsername']]))
        logged_in_user.click()

    def navigate_to_change_mobile_number(self, client_type):
        self.click_logged_in_user()
        change_mobile_number = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable([By.CLASS_NAME, self.my_dict['lnkChangeMobileNumber']]))
        change_mobile_number.click()
        ic_personal_info_data = PersonalInformationData.personal_info(client_type)
        self.mobile_number(ic_personal_info_data)
        vca = ClientPageValidation(self.driver)
        vca.validate_otp()

    def click_logout(self):
        self.click_logged_in_user()
        logout = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable([By.CLASS_NAME, self.my_dict['lnkLogout']]))
        logout.click()
        validate_login = LoginValidation(self.driver)
        validate_login.validate_if_user_able_to_logout()

    def click_change_email(self):
        self.click_logged_in_user()
        change_email = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable([By.CLASS_NAME, self.my_dict['lnkChangeEmail']]))
        result = change_email.click()
        return result

    def click_reset_password(self):
        self.click_logged_in_user()
        reset_password = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable([By.CLASS_NAME, self.my_dict['lnkResetPassword']]))
        result = reset_password.click()
        return result

    def click_change_account_password(self):
        self.click_logged_in_user()
        change_account_password = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable([By.CLASS_NAME, self.my_dict['lnkChangeAccountPassword']]))
        result = change_account_password.click()
        return result

    def click_personal_information(self):
        self.click_logged_in_user()
        personal_information = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable([By.CLASS_NAME, self.my_dict['lnkPersonalInformation']]))
        result = personal_information.click()
        return result

    def click_uploaded_documents(self):
        self.click_logged_in_user()
        uploaded_documents = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable([By.CLASS_NAME, self.my_dict['lnkUploadedDocuments']]))
        result = uploaded_documents.click()
        return result

    def validate_personal_information_under_logged_in_user(self, username):
        cpv = ClientPageValidation(self.driver)
        cpv.validate_personal_information_under_logged_in_user(username)

    def validate_trading_account_dropdown_values(self, regulator_platform_tier_type):
        try:
            if regulator_platform_tier_type == "mex_atlantic_mt4_standard" or regulator_platform_tier_type == "mex_exchange_mt4_standard" or \
                    regulator_platform_tier_type == "mex_singapore_mt4_standard":
                self.mex_atlantic()
                self.mt4()
                self.standard()
            elif regulator_platform_tier_type == 'mex_atlantic_mt5_standard' or regulator_platform_tier_type == 'mex_exchange_mt5_standard' or \
                    regulator_platform_tier_type == 'mex_singapore_mt5_standard':
                self.mt5()
                self.standard()
            elif regulator_platform_tier_type == 'mex_atlantic_mt4_pro' or regulator_platform_tier_type == 'mex_exchange_mt4_pro' or \
                    regulator_platform_tier_type == 'mex_singapore_mt4_pro':
                self.mex_atlantic()
                self.mt4()
                self.pro()
            elif regulator_platform_tier_type == 'mex_atlantic_mt5_pro' or regulator_platform_tier_type == 'mex_exchange_mt5_pro' or \
                    regulator_platform_tier_type == 'mex_singapore_mt5_pro':
                self.mex_atlantic()
                self.mt5()
                self.pro()
            elif regulator_platform_tier_type == 'mex_atlantic_mt4_ecn' or regulator_platform_tier_type == 'mex_exchange_mt4_ecn' or \
                    regulator_platform_tier_type == 'mex_singapore_mt4_ecn':
                self.mex_atlantic()
                self.mt4()
                self.ecn()
            elif regulator_platform_tier_type == 'mex_atlantic_mt5_ecn' or regulator_platform_tier_type == 'mex_exchange_mt5_ecn' or \
                    regulator_platform_tier_type == 'mex_singapore_mt5_ecn':
                self.mex_atlantic()
                self.mt5()
                self.ecn()
            elif regulator_platform_tier_type == 'mex_pacific_mt5_mex_sports':
                self.mex_pacific()
                self.mt5()
                self.mex_sports()
            else:
                return 'regulated_entity: ' + regulator_platform_tier_type + 'does not exist.'
            tav = TradingAccountSettingsValidation(self.driver)
            tav.validate_trading_account_dropdown_list(regulator_platform_tier_type)
        except TypeError:
            print(regulator_platform_tier_type + " does not exist!!!")
