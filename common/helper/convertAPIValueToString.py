class ConvertAPIValueToString:

    @staticmethod
    def convert_account_tier(account_tier_api_val):
        switch_account_tier = {
            7: 'STANDARD',
            5: 'PRO',
            3: 'ECN',
            8: 'MEX SPORTS'
        }
        return switch_account_tier.get(account_tier_api_val, 'Account Tier API integer value does not exist!!!')

    @staticmethod
    def convert_base_currency(base_currency_api_val):
        switch_base_currency = {
            1: 'USD',
            2: 'AUD',
            4: 'GBP',
            6: 'EUR',
            11: 'CAD',
            12: 'CHF'
        }
        return switch_base_currency.get(base_currency_api_val, 'Base Currency API integer value does not exist!!!')

    @staticmethod
    def convert_regulated_entity(regulated_entity_api_val):
        switch_regulated_entity = {
            6: 'MEX Atlantic',
            1: '',
            13: '',
            14: ''
        }
        return switch_regulated_entity.get(regulated_entity_api_val, 'Regulated Entity API integer value does not exist!!!')

    @staticmethod
    def convert_platform_version(platform_version_api_val):
        switch_platform_version = {
            4: 'MT4',
            5: 'MT5'
        }
        return switch_platform_version.get(platform_version_api_val, 'Platform Version API integer value does not exist!!!')

    @staticmethod
    def convert_default_leverage(default_leverage_api_val):
        switch_default_leverage = {
            1: '100',
            2: '200',
            3: '300',
            4: '400',
            5: '500',
            6: '600',
            7: '700',
            8: '800',
            9: '900'
        }
        return switch_default_leverage.get(default_leverage_api_val, 'Default Leverage API integer value does not exist!!!')

    @staticmethod
    def convert_real_account_type(real_account_type_api_val):
        switch_real_account_type = {
            'Corporate': 1,
            'Individual': 2,
            'Joint Account': 3,
            'Institutional/Corporate': 7
        }
        return switch_real_account_type.get(real_account_type_api_val, 'Real Account Type API integer value does not exist!!!')






