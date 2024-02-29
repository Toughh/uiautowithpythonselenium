import os

from common.commonFunctions import CommonFunctions
from common.enum.client.currency import Currency
from common.enum.client.defaultLeverageType import DefaultLeverageType
from common.enum.client.employmentInformationType import EmploymentInformationType
from common.enum.client.identityType import IdentityType
from common.enum.client.sourceOfFundsType import SourceOfFundsType
from common.pojo.client.personalInformation import PersonalInfo
from common.enum.client.country import Country
from common.enum.client.expectedClientDeposit import ExpectedClientDeposit
from common.enum.client.expectedDeposit import ExpectedDeposit
from common.enum.client.expectedNoOfClient import ExpectedNoOfClient
from common.pojo.client.proofOfIdentity import ProofOfIdentity
from common.pojo.client.tradingAccountSettings import TradingAccountSettings


class PersonalInformationData:

    @staticmethod
    def personal_info(client_type):
        cf = CommonFunctions
        ed = ExpectedDeposit
        ecd = ExpectedClientDeposit
        enoc = ExpectedNoOfClient
        country = Country
        otp = os.environ.get('OTP')

        return PersonalInfo(client_type, cf.generate_random_first_name(), cf.generate_random_last_name(), "1987-03-02",
                            country.AE.value, cf.mob_num_with_country_code('+97155'), otp, ed.deposit4.value,
                            ecd.client_deposit3.value, enoc.no_of_client2.value, cf.generate_random_first_name(),
                            cf.generate_random_last_name(), country.AF.value, "1987-04-04",
                            cf.generate_random_first_name(), cf.generate_random_number(11111, 99999))

    @staticmethod
    def trading_capability_assessment():
        assessment_questions_count = 6
        return assessment_questions_count

    @staticmethod
    def trading_account_settings():
        dl = DefaultLeverageType
        ei = EmploymentInformationType
        ct = Currency
        sof = SourceOfFundsType

        return TradingAccountSettings(dl.leverage_100.value, sof.salary.value, ei.employed.value, ct.USD.value)

    @staticmethod
    def proof_of_identity():
        country = Country
        identity_type = IdentityType

        return ProofOfIdentity(country.AF.value, identity_type.passport.value)
