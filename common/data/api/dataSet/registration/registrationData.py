from common.api.registration.postUploadFilesApi import UploadFilesApi
from common.commonFunctions import CommonFunctions
from common.data.api.dataSet.registration.uploadFilesData import UploadFilesData

ic_payload = {}
ib_payload = {}
ic_campaign_payload = {}
ic_campaign_with_no_trading_payload = {}
demo_payload = {}


class RegistrationData:

    @staticmethod
    def register_ic_user(username):
        global ic_payload
        country_code = CommonFunctions.generate_random_country_code()
        first_name = CommonFunctions.generate_random_first_name()
        last_name = CommonFunctions.generate_random_last_name()
        mob = CommonFunctions.mob_num_with_country_code('+97155')
        upload_data = UploadFilesData.upload_files_data(username)
        upload_files = UploadFilesData.upload_files()
        document_id = UploadFilesApi.get_file(upload_data, upload_files)
        ic_payload = {
            "account": {
                "username": username,
                "accountType": 1,
                "source": "[2021-12-30 16:59:39] https://multibankfx.com/institutional/signup[2022-01-04 19:54:29] "
                          "https://uat.multibankfx.com/live-account-2[2022-01-04 19:54:49] https://uat.multibankfx.com/"
                          "live-account-2[2022-01-04 19:54:54] https://uat.multibankfx.com/live-account-2  "
                          "uat.multibankfx.com/live-account-2?web=true posted From: uat.multibankfx.com/"
                          "live-account-2?web=true",
                "leadSource": "Live Account NJ 3.0 Step 1",
                "referer": "",
                "salias": "",
                "websiteMirror": "en",
                "browser": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                           "Chrome/96.0.4664.110 Safari/537.36",
                "IPAddress": "5.30.45.138",
                "ip_country": country_code,
                "communicationLanguage": "en",
                "firstName": first_name,
                "lastName": last_name,
                "realAccountType": "2",
                "mobileNumber": mob,
                "phone": mob,
                "dateOfBirth": "1980-09-12",
                "nextStep": "true",
                "country": country_code,
                "otpChecker": 1,
                "documentId": document_id,
                "documentId2": "",
                "documentPor": "",
                "documentPor2": ""
            }
        }
        return ic_payload

    @staticmethod
    def register_ib_user(username):
        global ib_payload
        country_code = CommonFunctions.generate_random_country_code()
        first_name = CommonFunctions.generate_random_first_name()
        last_name = CommonFunctions.generate_random_last_name()
        mob = CommonFunctions.mob_num_with_country_code('+97155')
        upload_data = UploadFilesData.upload_files_data(username)
        upload_files = UploadFilesData.upload_files()
        document_id = UploadFilesApi.get_file(upload_data, upload_files)
        ib_payload = {
            "account": {
                "username": username,
                "accountType": "2",
                "source": "[2021-12-30 16:59:39] https://multibankfx.com/institutional/signup[2022-01-04 19:54:29] https://uat.multibankfx.com/live-account-2[2022-01-04 19:54:49] https://uat.multibankfx.com/live-account-2[2022-01-04 19:54:54] https://uat.multibankfx.com/live-account-2 uat.multibankfx.com/live-account-2?web=true posted From: uat.multibankfx.com/live-account-2?web=true",
                "leadSource": "Live Account NJ 3.0 Step 1",
                "salias": "",
                "websiteMirror": "en",
                "browser": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
                "IPAddress": "5.30.45.138",
                "ip_country": country_code,
                "communicationLanguage": "en",
                "firstName": first_name,
                "lastName": last_name,
                "realAccountType": "2",
                "mobileNumber": mob,
                "phone": mob,
                "dateOfBirth": "1990-01-17",
                "country": country_code,
                "otpChecker": 1,
                "documentId": document_id,
                "documentId2": "",
                "documentPor": document_id,
                "documentPor2": "",
                "expectedFirstDeposit": 1
            }
        }
        return ib_payload

    @staticmethod
    def register_ic_campaign_user(username):
        global ic_campaign_payload
        country_code = CommonFunctions.generate_random_country_code()
        first_name = CommonFunctions.generate_random_first_name()
        last_name = CommonFunctions.generate_random_last_name()
        mob = CommonFunctions.mob_num_with_country_code('+97155')
        upload_data = UploadFilesData.upload_files_data(username)
        upload_files = UploadFilesData.upload_files()
        document_id = UploadFilesApi.get_file(upload_data, upload_files)
        ic_campaign_payload = {
            "account": {
                "username": username,
                "accountType": "1",
                "source": "[2022-03-02 21:07:18] https:\/\/multibankfx.com\/na\/amazon<br\/><br\/> <br\/><br\/> multibankfx.com\/na\/amazon?web=true <br> posted From: multibankfx.com\/na\/amazon?web=true",
                "leadSource": "Amazon Product Tactical V3.6",
                "referer": "",
                "salias": "",
                "wlid": "atlantic",
                "websiteMirror": "en",
                "browser": "Mozilla\/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/98.0.4758.102 Safari\/537.36",
                "IPAddress": "5.31.31.39",
                "ip_country": country_code,
                "communicationLanguage": "en",
                "firstName": first_name,
                "lastName": last_name,
                "realAccountType": "2",
                "mobileNumber": mob,
                "phone": mob,
                "country": country_code,
                "otpChecker": "1",
                "sourceType": "2",
                "documentId": document_id,
                "documentId2": "",
                "documentPor": "",
                "documentPor2": "",
                "trading_account_settings": {
                    "baseCurrency": 1,
                    "accountTier": 7,
                    "defaultLeverage": 1,
                    "regulatedEntity": 6,
                    "platformVersion": 4,
                    "sourceOfFunds": "Salary",
                    "employmentInformation": 1,
                    "leadSource": "Live Account NJ 3.0 Step 2"
                }
            }
        }
        return ic_campaign_payload

    @staticmethod
    def register_ic_campaign_user_without_trading_account_settings(username):
        global ic_campaign_with_no_trading_payload
        country_code = CommonFunctions.generate_random_country_code()
        first_name = CommonFunctions.generate_random_first_name()
        last_name = CommonFunctions.generate_random_last_name()
        mob = CommonFunctions.mob_num_with_country_code('+97155')
        upload_data = UploadFilesData.upload_files_data(username)
        upload_files = UploadFilesData.upload_files()
        document_id = UploadFilesApi.get_file(upload_data, upload_files)
        ic_campaign_with_no_trading_payload = {
            "account": {
                "username": username,
                "accountType": "1",
                "source": "[2022-03-02 21:07:18] https:\/\/multibankfx.com\/na\/amazon<br\/><br\/> <br\/><br\/> multibankfx.com\/na\/amazon?web=true <br> posted From: multibankfx.com\/na\/amazon?web=true",
                "leadSource": "Amazon Product Tactical V3.6",
                "referer": "",
                "salias": "",
                "wlid": "atlantic",
                "websiteMirror": "en",
                "browser": "Mozilla\/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/98.0.4758.102 Safari\/537.36",
                "IPAddress": "5.31.31.39",
                "ip_country": country_code,
                "communicationLanguage": "en",
                "firstName": first_name,
                "lastName": last_name,
                "realAccountType": "2",
                "mobileNumber": mob,
                "phone": mob,
                "country": country_code,
                "otpChecker": "1",
                "sourceType": "1",
                "documentId": document_id,
                "documentId2": "",
                "documentPor": "",
                "documentPor2": ""
            }
        }
        return ic_campaign_with_no_trading_payload

    @staticmethod
    def register_demo_user(username):
        global demo_payload
        country_code = CommonFunctions.generate_random_country_code()
        first_name = CommonFunctions.generate_random_first_name()
        last_name = CommonFunctions.generate_random_last_name()
        mob = CommonFunctions.mob_num_with_country_code('+97155')
        demo_payload = {
            "account": {
                "username": username,
                "accountType": "0",
                "source": "[2021-12-30 16:59:39] https://multibankfx.com/institutional/signup[2022-01-04 19:54:29] https://uat.multibankfx.com/live-account-2[2022-01-04 19:54:49] https://uat.multibankfx.com/live-account-2[2022-01-04 19:54:54] https://uat.multibankfx.com/live-account-2 uat.multibankfx.com/live-account-2?web=true posted From: uat.multibankfx.com/live-account-2?web=true",
                "leadSource": "Live Account NJ 3.0 Step 1",
                "salias": "",
                "websiteMirror": "en",
                "browser": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
                "IPAddress": "5.30.45.138",
                "ip_country": country_code,
                "communicationLanguage": "en",
                "firstName": first_name,
                "lastName": last_name,
                "referer": "",
                "realAccountType": "2",
                "mobileNumber": mob,
                "phone": mob,
                "dateOfBirth": "1990-01-17",
                "country": country_code,
                "wlid": 0,
                "platformVersion": 4,
                "accountTier": 3
            }
        }
        return demo_payload

    @staticmethod
    def ic_personal_information():
        account = ic_payload['account']
        client_type = account['realAccountType']
        first_name = account['firstName']
        last_name = account['lastName']
        country = account['country']
        # date_of_birth = account['dateOfBirth']
        mobile_number = account['mobileNumber']

        my_dict = {"client_type": client_type, "first_name": first_name, "last_name": last_name,
                   "country": country, 'date_of_birth': "", "mobile_number": mobile_number}
        return my_dict

    @staticmethod
    def ic_campaign_personal_information():
        account = ic_campaign_payload['account']
        client_type = account['realAccountType']
        first_name = account['firstName']
        last_name = account['lastName']
        country = account['country']
        # date_of_birth = account['dateOfBirth']
        mobile_number = account['mobileNumber']

        my_dict = {"client_type": client_type, "first_name": first_name, "last_name": last_name,
                   "country": country, 'date_of_birth': "", "mobile_number": mobile_number}
        return my_dict

    @staticmethod
    def ib_personal_information():
        account = ib_payload['account']
        client_type = account['realAccountType']
        first_name = account['firstName']
        last_name = account['lastName']
        country = account['country']
        mobile_number = account['mobileNumber']

        my_dict = {"client_type": client_type, "first_name": first_name, "last_name": last_name,
                   "country": country, "date_of_birth": "", "mobile_number": mobile_number}
        return my_dict

    @staticmethod
    def ic_campaign_trading_settings_data(username):
        account = RegistrationData.register_ic_campaign_user(username)['account']
        trading_account = account['trading_account_settings']
        default_leverage = trading_account['defaultLeverage']
        base_currency = trading_account['baseCurrency']
        platform_version = trading_account['platformVersion']
        regulated_entity = trading_account['regulatedEntity']
        account_tier = trading_account['accountTier']

        my_dict = {"default_leverage": default_leverage, "base_currency": base_currency,
                   "platform_version": platform_version,
                   "regulated_entity": regulated_entity, "account_tier": account_tier}
        return my_dict

    @staticmethod
    def demo_trading_settings_data(username):
        account = RegistrationData.register_demo_user(username)['account']
        default_leverage = '500'
        base_currency = 'USD'
        platform_version = account['platformVersion']
        regulated_entity = 'Demo'
        account_tier = account['accountTier']

        my_dict = {"default_leverage": default_leverage, "base_currency": base_currency,
                   "platform_version": platform_version,
                   "regulated_entity": regulated_entity, "account_tier": account_tier}
        return my_dict

    @staticmethod
    def ic_registration_personal_information_data(email_address):
        account = RegistrationData.register_ic_user(email_address)['account']
        first_name = account['firstName']
        last_name = account['lastName']
        mobile_number = account['phone']

        my_dict = {'first_name': first_name, 'last_name': last_name, 'email_address': email_address,
                   'mobile_number': mobile_number}
        return my_dict
