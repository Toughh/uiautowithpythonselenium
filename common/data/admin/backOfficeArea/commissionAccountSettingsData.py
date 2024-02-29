from common.pojo.admin.commissionAccountSettings import CommissionAccountSettings
from common.enum.admin.backOfficeArea.realAccounts.commissionAccountSettings.ibCompanyType import IBCompanyType
from common.enum.admin.backOfficeArea.realAccounts.commissionAccountSettings.ibLeverageType import IBLeverageType
from common.enum.admin.backOfficeArea.realAccounts.commissionAccountSettings.ibLoginType import IBLoginType
from common.enum.admin.backOfficeArea.realAccounts.commissionAccountSettings.ibPlatformType import IBPlatformType
from common.enum.admin.backOfficeArea.realAccounts.commissionAccountSettings.ibTradingCurrencyType import \
    IBTradingCurrencyType
from common.enum.admin.backOfficeArea.realAccounts.commissionAccountSettings.ibTradingGroupType import \
    IBTradingGroupType


class CommissionAccountSettingsData:

    @staticmethod
    def commission_account_settings():
        login = IBLoginType
        company = IBCompanyType
        platform = IBPlatformType
        trading_group = IBTradingGroupType
        trading_currency = IBTradingCurrencyType
        leverage = IBLeverageType

        return CommissionAccountSettings(login.auto.value, company.pacific.value, platform.mx.value,
                                         trading_group.test_1231.value, trading_currency.CAD.value,
                                         leverage.leverage_2.value, "a2N267278929299389")
