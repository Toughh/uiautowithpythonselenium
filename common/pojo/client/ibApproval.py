class IBApproval:

    def __init__(self, platform: str, trading_group: str, trading_currency: str, ib_agreement: str):
        self._platform = platform
        self._trading_group = trading_group
        self._trading_currency = trading_currency
        self._ib_agreement = ib_agreement

    def get_platform(self):
        return self._platform

    def set_platform(self, val):
        self._platform = val

    def get_trading_group(self):
        return self._trading_group

    def set_trading_group(self, val):
        self._trading_group = val

    def get_trading_currency(self):
        return self._trading_currency

    def set_trading_currency(self, val):
        self._trading_currency = val

    def get_ib_agreement(self):
        return self._ib_agreement

    def set_ib_agreement(self, val):
        self._ib_agreement = val
