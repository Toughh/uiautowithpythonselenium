import requests
import os

from common.data.api.dataSet.registration.addTradingAccountSettingsData import AddTradingAccountSettingsData
from common.data.api.dataSet.registration.registrationData import RegistrationData
from common.api.registration.postRegisterNewAccountApi import RegisterNewAccountApi

trading_account_settings_endpoint = os.environ.get('REGISTER_NEW_ACCOUNT_IC_ENDPOINT')
content_type = os.environ.get('CONTENT_TYPE')
x_token = os.environ.get('X_TOKEN')
res = {}


class TradingAccountSettingsApi:

    @staticmethod
    def get_trading_account_settings(username):
        global res
        ic_registration_payload = RegistrationData.register_ic_user(username)
        RegisterNewAccountApi.get_register_new_account_res(ic_registration_payload)
        md5_key = RegisterNewAccountApi.get_md5_key()
        add_trading_account_data = AddTradingAccountSettingsData.add_trading_account()

        res = requests.post(
            url=trading_account_settings_endpoint + '/' + md5_key,
            json=add_trading_account_data,
            headers={'Content-type': content_type, 'x-token': x_token})

        assert res.status_code == 200, 'Get Trading Account Settings Api returns status_code as: ' + \
                                       str(res.status_code) + '\nResponse content:\n' + str(res.content)
        return res.json()

    @staticmethod
    def get_is_email_verified():
        return res.json['isEmailVerified']

    @staticmethod
    def get_status():
        return res.json['status']
