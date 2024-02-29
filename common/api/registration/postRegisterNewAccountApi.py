import requests
import os

from common.data.api.dataSet.registration.addTradingAccountSettingsData import AddTradingAccountSettingsData
from common.data.api.dataSet.registration.registrationData import RegistrationData

register_new_account_ic_endpoint = os.environ.get('REGISTER_NEW_ACCOUNT_IC_ENDPOINT')
register_new_account_ib_endpoint = os.environ.get('REGISTER_NEW_ACCOUNT_IB_ENDPOINT')
trading_account_settings_endpoint = os.environ.get('TRADING_ACCOUNT_SETTINGS_ENDPOINT')
content_type = os.environ.get('CONTENT_TYPE')
x_token = os.environ.get('X_TOKEN')
res = {"json": []}


class RegisterNewAccountApi:

    @staticmethod
    def get_register_new_account_res(data):
        global res
        r = requests.post(
            url=register_new_account_ic_endpoint,
            json=data,
            headers={'Content-type': content_type, 'x-token': x_token})
        assert r.status_code == 200, 'Register New Account Api returns status_code as: ' + str(r.status_code) + \
                                     '\nResponse content:\n' + str(r.content)
        return res['json'].append(r.json())

    @staticmethod
    def get_register_new_ib_account_res(data):
        global res
        r = requests.post(
            url=register_new_account_ib_endpoint,
            json=data,
            headers={'Content-type': content_type, 'x-token': x_token})

        assert r.status_code == 200, 'Register New IB Account Api returns status_code as: ' + str(r.status_code) + \
                                     '\nResponse content:\n' + str(r.content)
        return res['json'].append(r.json())

    @staticmethod
    def add_trading_account():
        global res
        md5_key = RegisterNewAccountApi.get_md5_key()
        add_trading_account_data = AddTradingAccountSettingsData.add_trading_account()
        r = requests.post(
            url=trading_account_settings_endpoint + '/' + md5_key,
            json=add_trading_account_data,
            headers={'Content-type': content_type, 'x-token': x_token})

        assert r.status_code == 200, 'Post Trading Account Settings Api returns status code as: ' + \
                                     str(r.status_code) + '\nResponse content:\n' + str(r.content)
        return res['json'].append(r.json())

    @staticmethod
    def get_id():
        id = res['json'][0]['id']
        assert id != 0, 'Register New Account Api returns id as: ' + str(id)
        return id

    @staticmethod
    def get_set_password_url():
        set_password_url = res['json'][0]['setPasswordUrl']
        return set_password_url

    @staticmethod
    def get_md5_key():
        md5_key = res['json'][0]['md5Key']
        return md5_key

    @staticmethod
    def get_verification_dev():
        verification_dev = res['json'][0]['verification_dev']
        return verification_dev

    @staticmethod
    def get_status():
        status = res['json'][0]['status']
        return status

    @staticmethod
    def get_ib_set_password_url():
        ib_set_password_url = res['json'][0]['setPasswordUrl_dev']
        return ib_set_password_url

    @staticmethod
    def register_ic_user(username):
        ic_registration = RegistrationData.register_ic_user(username)
        RegisterNewAccountApi.get_register_new_account_res(ic_registration)

    @staticmethod
    def register_ib_user(username):
        ib_registration = RegistrationData.register_ib_user(username)
        RegisterNewAccountApi.get_register_new_ib_account_res(ib_registration)

    @staticmethod
    def register_ic_campaign_user(username):
        ic_campaign_registration = RegistrationData.register_ic_campaign_user(username)
        RegisterNewAccountApi.get_register_new_account_res(ic_campaign_registration)

    @staticmethod
    def register_ic_campaign_user_without_trading_account_settings(username):
        ic_campaign_registration = RegistrationData.register_ic_campaign_user_without_trading_account_settings(username)
        RegisterNewAccountApi.get_register_new_account_res(ic_campaign_registration)

    @staticmethod
    def register_demo_user(username):
        demo_registration = RegistrationData.register_demo_user(username)
        RegisterNewAccountApi.get_register_new_account_res(demo_registration)

    @staticmethod
    def get_ic_campaign_md5_key():
        md5_key = res['json'][0]['setPasswordUrl']
        try:
            if "http://my.test" in md5_key:
                return md5_key.replace("http://my.test/en/account-registration-auto-login/", "")
            else:
                return md5_key.replace("https://mystaging.mexatlantic.com/en/account-registration-auto-login/", "")
        except TypeError:
            print(md5_key + " not found!!!")
