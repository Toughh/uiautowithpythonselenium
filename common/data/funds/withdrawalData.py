import os

from common.commonFunctions import CommonFunctions
from common.enum.client.country import Country
from common.enum.client.withdrawalType import WithdrawalType
from common.pojo.client.withdrawals import Withdrawals


class WithdrawalData:

    @staticmethod
    def withdrawal_form(trading_account_number):
        cf = CommonFunctions
        wt = WithdrawalType
        country = Country.AE.value
        beneficiary_name = cf.generate_random_first_name()

        return Withdrawals(trading_account_number, cf.generate_random_number(100, 1000), "Testing Purpose",
                           wt.bank_wire_transfer.value, "", "ADCB", beneficiary_name, country, "Dubai", "12345",
                           "123456789", "AED", "COD123", os.environ.get('OTP'))
