class AddTradingAccountSettingsData:

    @staticmethod
    def add_trading_account():
        my_dict = {
            "trading_account_settings": {
                "baseCurrency": 1,
                "accountTier": 7,
                "defaultLeverage": 1,
                "regulatedEntity": 6,
                "platformVersion": 4,
                "sourceOfFunds": "Salary",
                "employmentInformation": 1,
                "taxIdentificationNumber": 1231,
                "IPAddress": "",
                "leadSource": "Live Account NJ 3.0 Step 2"
            }
        }
        return my_dict
