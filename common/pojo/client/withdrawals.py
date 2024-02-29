class Withdrawals:

    def __init__(self, trading_account=None, amount=None, withdrawal_purpose=None, withdrawal_type=None,
                 banking_information=None, bank_name=None, beneficiary_name=None, country=None, bank_address=None,
                 swift_bic=None, beneficiary_account_no_iban=None, account_currency=None, sort_code_bsb=None,
                 online_payment_type=None, email_verification_code=None):

        self.__trading_account = trading_account
        self.__amount = amount
        self.__withdrawal_purpose = withdrawal_purpose
        self.__withdrawal_type = withdrawal_type
        self.__banking_information = banking_information
        self.__bank_name = bank_name
        self.__beneficiary_name = beneficiary_name
        self.__country = country
        self.__bank_address = bank_address
        self.__swift_bic = swift_bic
        self.__beneficiary_account_no_iban = beneficiary_account_no_iban
        self.__account_currency = account_currency
        self.__sort_code_bsb = sort_code_bsb
        self.__online_payment_type = online_payment_type
        self.__email_verification_code = email_verification_code

    def set_trading_account(self, trading_account: str):
        self.__trading_account = trading_account

    def get_trading_account(self):
        return self.__trading_account

    def set_amount(self, amount: str):
        self.__amount = amount

    def get_amount(self) -> str:
        return self.__amount

    def set_withdrawal_purpose(self, withdrawal_purpose: str):
        self.__withdrawal_purpose = withdrawal_purpose

    def get_withdrawal_purpose(self) -> str:
        return self.__withdrawal_purpose

    def set_withdrawal_type(self, withdrawal_type: str):
        self.__withdrawal_type = withdrawal_type

    def get_withdrawal_type(self) -> str:
        return self.__withdrawal_type

    def set_banking_information(self, banking_information: str):
        self.__banking_information = banking_information

    def get_banking_information(self) -> str:
        return self.__banking_information

    def set_bank_name(self, bank_name: str):
        self.__bank_name = bank_name

    def get_bank_name(self) -> str:
        return self.__bank_name

    def set_beneficiary_name(self, beneficiary_name: str):
        self.__beneficiary_name = beneficiary_name

    def get_beneficiary_name(self) -> str:
        return self.__beneficiary_name

    def set_country(self, country: str):
        self.__country = country

    def get_country(self) -> str:
        return self.__country

    def set_bank_address(self, bank_address: str):
        self.__bank_address = bank_address

    def get_bank_address(self) -> str:
        return self.__bank_address

    def set_swift_bic(self, swift_bic: str):
        self.__swift_bic = swift_bic

    def get_swift_bic(self) -> str:
        return self.__swift_bic

    def set_beneficiary_account_no_iban(self, beneficiary_account_no_iban: str):
        self.__beneficiary_account_no_iban = beneficiary_account_no_iban

    def get_beneficiary_account_no_iban(self) -> str:
        return self.__beneficiary_account_no_iban

    def set_account_currency(self, account_currency: str):
        self.__account_currency = account_currency

    def get_account_currency(self) -> str:
        return self.__account_currency

    def set_sort_code_bsb(self, sort_code_bsb: str):
        self.__sort_code_bsb = sort_code_bsb

    def get_sort_code_bsb(self) -> str:
        return self.__sort_code_bsb

    def set_online_payment_type(self, online_payment_type: str):
        self.__online_payment_type = online_payment_type

    def get_online_payment_type(self) -> str:
        return self.__online_payment_type

    def set_email_verification_code(self, email_verification_code: str):
        self.__email_verification_code = email_verification_code

    def get_email_verification_code(self) -> str:
        return self.__email_verification_code
