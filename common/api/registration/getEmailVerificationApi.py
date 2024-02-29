import os

import requests

from common.data.api.dataSet.registration.addTradingAccountSettingsData import AddTradingAccountSettingsData
from common.data.api.dataSet.registration.registrationData import RegistrationData
from common.api.registration.postRegisterNewAccountApi import RegisterNewAccountApi

trading_account_settings_endpoint = os.environ.get('TRADING_ACCOUNT_SETTINGS_ENDPOINT')
email_verify_endpoint = os.environ.get('EMAIL_VERIFY_ENDPOINT')
confirm_email_verify_endpoint = os.environ.get('CONFIRM_EMAIL_VERIFY_ENDPOINT')
content_type = os.environ.get('CONTENT_TYPE')
x_token = os.environ.get('X_TOKEN')


class EmailVerificationApi:

    @staticmethod
    def get_email_verified_for_ic_user(username):
        ic_registration_payload = RegistrationData.register_ic_user(username)
        RegisterNewAccountApi.get_register_new_account_res(ic_registration_payload)
        md5_key = RegisterNewAccountApi.get_md5_key()
        add_trading_account_data = AddTradingAccountSettingsData.add_trading_account()
        res = requests.post(
            url=trading_account_settings_endpoint + '/' + md5_key,
            json=add_trading_account_data,
            headers={'Content-type': content_type, 'x-token': x_token})
        if res.status_code == 200:
            res = requests.get(url=email_verify_endpoint + '/' + md5_key)
            assert res.status_code == 200, 'Get Email Verification Api returns status_code as: ' + str(
                res.status_code) + '\nResponse content:\n' + str(res.content)
            assert res.json()['status'] == "success", 'Get Email Verification Api returns status as: ' + \
                                                      res.json()['status']
        else:
            print('Post Trading Account Settings Api returns status code as: ' + str(res.status_code) +
                  '\nResponse content:\n' + str(res.content))

    @staticmethod
    def get_email_verified_for_ib_user(username):
        ib_registration_payload = RegistrationData.register_ib_user(username)
        RegisterNewAccountApi.get_register_new_ib_account_res(ib_registration_payload)
        md5_key = RegisterNewAccountApi.get_md5_key()
        res = requests.get(url=email_verify_endpoint + '/' + md5_key)
        assert res.status_code == 200, 'Get Email Verification Api returns status_code as: ' + str(
            res.status_code) + '\nResponse content:\n' + str(res.content)
        assert res.json()['status'] == "success", 'Get Email Verification Api returns status as: ' + \
                                                  res.json()['status']

    @staticmethod
    def get_email_verified_for_ic_campaign_user(username):
        RegisterNewAccountApi.register_ic_campaign_user(username)
        md5_key = RegisterNewAccountApi.get_ic_campaign_md5_key()
        res = requests.get(url=email_verify_endpoint + '/' + str(md5_key))
        assert res.status_code == 200, 'Get Email Verification Api returns status_code as: ' + str(
            res.status_code) + '\nResponse content:\n' + str(res.content)
        assert res.json()['status'] == "success", 'Get Email Verification Api returns status as: ' + \
                                                  res.json()['status']

    @staticmethod
    def get_email_verified_for_ic_campaign_user_without_trading_account(username):
        RegisterNewAccountApi.register_ic_campaign_user_without_trading_account_settings(username)
        md5_key = RegisterNewAccountApi.get_ic_campaign_md5_key()
        res = requests.get(url=email_verify_endpoint + '/' + str(md5_key))
        assert res.status_code == 200, 'Get Email Verification Api returns status_code as: ' + str(
            res.status_code) + '\nResponse content:\n' + str(res.content)
        assert res.json()['status'] == "success", 'Get Email Verification Api returns status as: ' + \
                                                  res.json()['status']

    @staticmethod
    def confirm_email():
        md5_key = RegisterNewAccountApi.get_ic_campaign_md5_key()
        res = requests.get(url=str(f'{confirm_email_verify_endpoint}/{md5_key}').format(confirm_email_verify_endpoint=confirm_email_verify_endpoint, md5_key=md5_key))
        assert res.status_code == 200, 'Get Email Verification Api returns status_code as: ' + str(
            res.status_code) + '\nResponse content:\n' + str(res.content)
