class CommissionAccountSettings:

    def __init__(self, login=None, company=None, platform=None, trading_group=None, trading_currency=None, leverage=None, ib_agreement=None):
        self.__login = login
        self.__company = company
        self.__platform = platform
        self.__trading_group = trading_group
        self.__trading_currency = trading_currency
        self.__leverage = leverage
        self.__ib_agreement = ib_agreement

    def set_login(self, login: str):
        self.__login = login

    def get_login(self) -> str:
        return self.__login

    def set_company(self, company: str):
        self.__company = company

    def get_company(self) -> str:
        return self.__company

    def set_platform(self, platform: str):
        self.__platform = platform

    def get_platform(self) -> str:
        return self.__platform

    def set_trading_group(self, trading_group: str):
        self.__trading_group = trading_group

    def get_trading_group(self) -> str:
        return self.__trading_group

    def set_trading_currency(self, trading_currency: str):
        self.__trading_currency = trading_currency

    def get_trading_currency(self) -> str:
        return self.__trading_currency

    def set_leverage(self, leverage: str):
        self.__leverage = leverage

    def get_leverage(self) -> str:
        return self.__leverage

    def set_ib_agreement(self, ib_agreement: str):
        self.__ib_agreement = ib_agreement

    def get_ib_agreement(self) -> str:
        return self.__ib_agreement
