import time
import yaml
import os

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from common.api.registration.postRegisterNewAccountApi import RegisterNewAccountApi
from common.commonFunctions import CommonFunctions
from common.data.api.dataSet.registration.registrationData import RegistrationData
from common.data.application.personalInformationData import PersonalInformationData
from mysql.connector import Error

from common.utility.db.onlineMexGroupDB import DatabaseUtility


class ClientPageValidation:

    def __init__(self, driver):
        self.driver = driver
        self.get_app_page_loc = os.environ.get('APPLICATION_PAGE')
        self.get_accounts_page_loc = os.environ.get('ACCOUNTS_PAGE')

        with open(self.get_app_page_loc, 'r') as f:
            self.my_dict = yaml.safe_load(f)

        with open(self.get_accounts_page_loc, 'r') as f:
            self.my_dict1 = yaml.safe_load(f)

        self.application_header = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located([By.CLASS_NAME, self.my_dict['lblApplicationHeader']]))

    def validate_ic_personal_information_contents_with_api(self):
        pass
        # rd = RegistrationData()
        # data = rd.ic_personal_information()
        #
        # client_type = self.driver.find_element(By.ID, self.my_dict['ddSelectClientType']).get_attribute("value")
        # first_name = self.driver.find_element(By.CLASS_NAME, self.my_dict['txtFirstName']).get_attribute("value")
        # last_name = self.driver.find_element(By.CLASS_NAME, self.my_dict['txtLastName']).get_attribute("value")
        # country = self.driver.find_element(By.ID, self.my_dict['ddSelectCountryOfResidence']).get_attribute("value")
        # date_of_birth = self.driver.find_element(By.CLASS_NAME, self.my_dict['dpDateOfBirth']).get_attribute("value")
        # mobile_number = self.driver.find_element(By.CLASS_NAME, self.my_dict['txtMobileNumber']).get_attribute("value")
        #
        # personal_info_data = {'client_type': client_type, 'first_name': first_name, 'last_name': last_name,
        #                       'country': country, 'date_of_birth': date_of_birth, 'mobile_number': mobile_number}
        #
        # if personal_info_data != data:
        #     assert False
        # else:
        #     assert True

    def validate_ic_campaign_personal_information_contents_with_api(self):
        rd = RegistrationData()
        data = rd.ic_campaign_personal_information()

        client_type = self.driver.find_element(By.ID, self.my_dict['ddSelectClientType']).get_attribute("value")
        first_name = self.driver.find_element(By.CLASS_NAME, self.my_dict['txtFirstName']).get_attribute("value")
        last_name = self.driver.find_element(By.CLASS_NAME, self.my_dict['txtLastName']).get_attribute("value")
        country = self.driver.find_element(By.ID, self.my_dict['ddSelectCountryOfResidence']).get_attribute("value")
        date_of_birth = self.driver.find_element(By.CLASS_NAME, self.my_dict['dpDateOfBirth']).get_attribute("value")
        mobile_number = self.driver.find_element(By.CLASS_NAME, self.my_dict['txtMobileNumber']).get_attribute("value")

        personal_info_data = {'client_type': client_type, 'first_name': first_name, 'last_name': last_name,
                              'country': country, 'date_of_birth': date_of_birth, 'mobile_number': mobile_number}

        if personal_info_data != data:
            assert False
        else:
            assert True

    def validate_ib_personal_information_contents_with_api(self):
        rd = RegistrationData()
        data = rd.ib_personal_information()
        selected_client_type = CommonFunctions.select_first_option(
            self.driver.find_element(By.ID, self.my_dict['ddSelectClientType']))
        selected_country_of_residence = CommonFunctions.select_first_option(
            self.driver.find_element(By.ID, self.my_dict['ddSelectCountryOfResidence']))

        if (selected_client_type != data['client_type'] and
                self.driver.find_element(By.CLASS_NAME, self.my_dict['txtFirstName']).get_attribute("value") !=
                data['first_name'] and
                self.driver.find_element(By.CLASS_NAME, self.my_dict['txtLastName']).get_attribute("value") !=
                data['last_name'] and
                selected_country_of_residence != data['country_of_res'] and
                self.driver.find_element(By.CLASS_NAME, self.my_dict['dpDateOfBirth']).get_attribute("value") !=
                data['dob'] and
                self.driver.find_element(By.CLASS_NAME, self.my_dict['txtMobileNumber']).get_attribute("value") !=
                data['phone']):
            assert False
        else:
            assert True

    def validate_personal_information_error_mes(self):
        error_mes = "This field is required."
        if ((self.driver.find_element(By.ID, self.my_dict['lblFirstNameError'])).text != error_mes and
                (self.driver.find_element(By.ID, self.my_dict['lblLastNameError'])).text != error_mes and
                (self.driver.find_element(By.ID, self.my_dict['lblDateOfBirthError'])).text != error_mes and
                (self.driver.find_element(By.ID, self.my_dict['lblMobileNumberError'])).text != error_mes and
                (self.driver.find_element(By.CLASS_NAME, self.my_dict['lblOtpError'])).text != error_mes):
            assert False
        else:
            assert True

    def validate_trading_assessment_error_mes(self):
        error_mes = "Please Select an answer"
        pid = PersonalInformationData()
        size = pid.trading_capability_assessment()
        try:
            for i in range(1, size):
                self.driver.execute_script("arguments[0].click();",
                                           self.driver.find_element(By.CLASS_NAME, self.my_dict['btnNext']))
                error = self.driver.find_element(By.XPATH, '//label[contains(.,"Please Select an answer")]')
                if error.text != error_mes:
                    assert False
                self.driver.execute_script("arguments[0].click();", self.driver.find_element(
                    By.ID, self.my_dict['asq' + str(i)]))
                self.driver.execute_script("arguments[0].click();", self.driver.find_element(
                    By.CLASS_NAME, self.my_dict['btnNext']))
            assert True
        except TypeError as e:
            print("Trading Account Settings content not found!!!", e)

    def validate_live_trading_accounts(self, trading_account_number, currency, account_tier, platform, regulator,
                                       leverage, currency_amount):
        if (self.driver.find_element(By.XPATH, self.my_dict1['lblTradingAccountNumberVal']).text !=
                trading_account_number and
                self.driver.find_element(By.XPATH, self.my_dict1['lblTradingAccountCurrencyAmount']).text != currency
                and self.driver.find_element(By.XPATH, self.my_dict1['lblTradingAccountAccountTier']).text !=
                account_tier and self.driver.find_element(By.XPATH, self.my_dict1['lblTradingAccountPlatform']).text !=
                platform and self.driver.find_element(By.XPATH, self.my_dict1['lblTradingAccountRegulator']).text !=
                regulator and self.driver.find_element(By.XPATH, self.my_dict1['lblTradingAccountLeverage']).text !=
                leverage and self.driver.find_element(By.XPATH, self.my_dict1['lblTradingAccountCurrency']).text !=
                currency_amount):
            assert False
        else:
            assert True

    def validate_personal_info_records_in_db(self, client_type, client_email):
        try:
            if client_type == "Individual" or client_type == "Institutional/Corporate":
                self.validate_db_personal_info_individual_or_institutional_client_type(client_email)
            elif client_type == "Corporate":
                self.validate_db_personal_info_corporate_client_type(client_email)
            elif client_type == "Joint Account":
                self.validate_db_personal_info_joint_account_client_type(client_email)
            else:
                raise Exception(client_type, " not found!!!")
        except NoSuchElementException:
            print("No Such Element found in the web page!!!")

    def validate_db_personal_info_individual_or_institutional_client_type(self, client_email):
        time.sleep(5)
        first_name = self.driver.find_element(By.CLASS_NAME, self.my_dict['txtFirstName']).get_attribute("value")
        last_name = self.driver.find_element(By.CLASS_NAME, self.my_dict['txtLastName']).get_attribute("value")
        date_of_birth = self.driver.find_element(By.CLASS_NAME, self.my_dict['dpDateOfBirth']).get_attribute("value")
        mobile_number = self.driver.find_element(By.CLASS_NAME, self.my_dict['txtMobileNumber']).get_attribute("value")

        id = RegisterNewAccountApi.get_id()
        db = DatabaseUtility
        if client_email is None:
            records = db.db_connection(os.environ.get('FOREX_PORTAL_USER') + str(id) + ";")
        else:
            id = id + 1
            records = db.db_connection(os.environ.get('FOREX_PORTAL_USER') + str(id) + ";")
        if mobile_number != records['mobile_number'] and date_of_birth != records["dateOfBirth"] and first_name != records["first_name"] and last_name != records["last_name"]:
            assert False
        else:
            assert True

    def validate_db_personal_info_corporate_client_type(self, client_email):
        time.sleep(5)
        try:
            corporate_name = self.driver.find_element(By.CLASS_NAME, self.my_dict['txtCorporateName']).get_attribute(
                "value")
            legal_entity_identifier = self.driver.find_element(By.CLASS_NAME,
                                                               self.my_dict['txtLegalEntityIdentifier']).get_attribute(
                "value")
            date_of_birth = self.driver.find_element(By.CLASS_NAME, self.my_dict['dpDateOfBirth']).get_attribute(
                "value")
            mobile_number = self.driver.find_element(By.CLASS_NAME, self.my_dict['txtMobileNumber']).get_attribute(
                "value")

            id = RegisterNewAccountApi.get_id()
            db = DatabaseUtility
            if client_email is None:
                records = db.db_connection(os.environ.get('FOREX_REAL_PROFILE_CORPORATION') + str(id) + ";")
            else:
                id = id + 1
                records = db.db_connection(os.environ.get('FOREX_REAL_PROFILE_CORPORATION') + str(id) + ";")
            try:
                if corporate_name != records[
                    "corporate_name"] and legal_entity_identifier != records[
                    "corporate_id"] and \
                        mobile_number != records['mobile_number'] and date_of_birth != records["dateOfBirth"]:
                    assert False
                else:
                    assert True
            except Error as e:
                print("Database Record Mismatch!!!", e)
        except Error as e:
            print("Error reading data from MySQL table", e)

    def validate_db_personal_info_joint_account_client_type(self, client_email):
        time.sleep(5)
        try:
            first_name = self.driver.find_element(By.CLASS_NAME, self.my_dict['txtFirstName']).get_attribute("value")
            last_name = self.driver.find_element(By.CLASS_NAME, self.my_dict['txtLastName']).get_attribute("value")
            date_of_birth = self.driver.find_element(By.CLASS_NAME, self.my_dict['dpDateOfBirth']).get_attribute(
                "value")
            mobile_number = self.driver.find_element(By.CLASS_NAME, self.my_dict['txtMobileNumber']).get_attribute(
                "value")
            joint_first_name = self.driver.find_element(By.CLASS_NAME, self.my_dict['txtJAFirstName']).get_attribute(
                "value")
            joint_last_name = self.driver.find_element(By.CLASS_NAME, self.my_dict['txtJALastName']).get_attribute(
                "value")
            joint_date_of_birth = self.driver.find_element(By.CLASS_NAME,
                                                           self.my_dict['txtJADateOfBirth']).get_attribute("value")

            id = RegisterNewAccountApi.get_id()
            db = DatabaseUtility
            if client_email is None:
                portal_user_records = db.db_connection(os.environ.get('FOREX_PORTAL_USER') + str(id))
                joint_account_records = db.db_connection(os.environ.get('FOREX_JOINT_ACCOUNT') + str(id))
            else:
                id = id + 1
                portal_user_records = db.db_connection(os.environ.get('FOREX_PORTAL_USER') + str(id))
                joint_account_records = db.db_connection(os.environ.get('FOREX_JOINT_ACCOUNT') + str(id))
            try:
                if mobile_number != portal_user_records['mobile_number'] and \
                        date_of_birth != portal_user_records["dateOfBirth"] and first_name != portal_user_records[
                    "first_name"] and last_name != \
                        portal_user_records["last_name"] and \
                        joint_first_name != joint_account_records["firstName"] and joint_last_name != \
                        joint_account_records["lastName"] and joint_date_of_birth != \
                        joint_account_records["dateOfBirth"]:
                    assert False
                else:
                    assert True
            except Error as e:
                print("Database Record Mismatch!!!", e)
        except Error as e:
            print("Error reading data from MySQL table", e)

    def validate_otp(self):
        self.verify_error_message_on_not_entering_otp_and_submit()
        self.verify_error_message_on_incorrect_otp()
        self.verify_success_mes_on_correct_otp()

    def verify_error_message_on_incorrect_otp(self):
        self.driver.find_element(By.ID, self.my_dict['txtOtp']).send_keys('111111' + Keys.INSERT)
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.CLASS_NAME, self.my_dict['txtVerificationError'])))
        error_mes1 = self.driver.find_element(By.CLASS_NAME, self.my_dict['txtVerificationError']).text
        if error_mes1 != "Verification code is incorrect":
            assert False
        else:
            ok = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located([By.XPATH, self.my_dict['btnVerificationErrorOk']]))
            ok.click()
            error_mes2 = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located([By.CLASS_NAME, self.my_dict['lblVerifyOtpMes']]))
            error_mes2 = error_mes2.text
            if error_mes2 != "Verification code is incorrect":
                assert False

    def verify_error_message_on_not_entering_otp_and_submit(self):
        send_otp = self.driver.find_element(By.CLASS_NAME, self.my_dict['btnSendOtp'])
        self.driver.execute_script("arguments[0].click();", send_otp)
        next_btn = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable([By.CLASS_NAME, self.my_dict['btnPINext']]))
        self.driver.execute_script("arguments[0].click();", next_btn)
        error_mes1 = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located([By.CLASS_NAME, self.my_dict['lblVerifyOtpMes']]))
        error_mes1 = error_mes1.text
        if error_mes1 != "Please verify your number":
            assert False

    def verify_success_mes_on_correct_otp(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID, self.my_dict['txtOtp'])))
        self.driver.find_element(By.ID, self.my_dict['txtOtp']).send_keys('119911' + Keys.INSERT)
        success_mes = WebDriverWait(self.driver, 20).until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, self.my_dict['lblVerifyOtpMes']),
                                             "validation code is correct"))
        if success_mes is True:
            assert True
        else:
            assert False

    def validate_personal_information_under_logged_in_user(self, username):
        rd = RegistrationData()
        api_data = rd.ic_registration_personal_information_data(username)
        id = RegisterNewAccountApi.get_id()

        first_name = self.driver.find_element(By.ID, self.my_dict['lblFirstName']).get_attribute("value")
        last_name = self.driver.find_element(By.ID, self.my_dict['lblLastName']).get_attribute("value")
        email_address = self.driver.find_element(By.ID, self.my_dict['lblEmailAddress']).get_attribute("value")
        mobile_number = self.driver.find_element(By.ID, self.my_dict['lblMobileNumber']).get_attribute("value")
        date_of_birth = self.driver.find_element(By.ID, self.my_dict['lblDateOfBirth']).get_attribute("value")

        personal_info_data = {'first_name': first_name, 'last_name': last_name, 'email_address': email_address,
                              'mobile_number': mobile_number}

        portal_user_records = os.environ.get('FOREX_PORTAL_USER')

        db = DatabaseUtility
        records = db.db_connection(portal_user_records + str(id) + ";")
        db_date_of_birth = records['dateOfBirth']
        db_record = {'first_name': records['first_name'], 'last_name': records['last_name'],
                     'email_address': records['username'],
                     'mobile_number': records['mobile_number']}

        try:
            if personal_info_data != db_record and date_of_birth != db_date_of_birth:
                print("Data Mismatch in ui and db!!!")
                assert False
            else:
                assert True
        except TypeError:
            print("DB connection error!!!")
