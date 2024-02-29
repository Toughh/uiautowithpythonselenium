class TradingAccountSettings:

    def __init__(self, default_leverage=None, source_of_funds=None, employment_information=None, base_currency=None):

        self.__default_leverage = default_leverage
        self.__base_currency = base_currency
        self.__employment_information = employment_information
        self.__source_of_funds = source_of_funds

    def set_default_leverage(self, default_leverage):
        self.__default_leverage = default_leverage

    def get_default_leverage(self):
        return self.__default_leverage

    def set_base_currency(self, base_currency: str):
        self.__base_currency = base_currency

    def get_base_currency(self) -> str:
        return self.__base_currency

    def set_employment_information(self, employment_information: str):
        self.__employment_information = employment_information

    def get_employment_information(self) -> str:
        return self.__employment_information

    def set_source_of_funds(self, source_of_funds: str):
        self.__source_of_funds = source_of_funds

    def get_source_of_funds(self) -> str:
        return self.__source_of_funds
