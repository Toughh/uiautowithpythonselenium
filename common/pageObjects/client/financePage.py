import os.path
import yaml

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from common.commonFunctions import CommonFunctions


class FinancePage:

    def __init__(self, driver):
        self.driver = driver
        self.get_finance_page_loc = os.environ.get('FINANCE_PAGE')

        with open(self.get_finance_page_loc, 'r') as f:
            self.my_dict = yaml.safe_load(f)

    def funds(self):
        self.driver.find_element(By.CLASS_NAME, self.my_dict['lnkFunds']).click()

    def withdrawals(self):
        self.funds()
        withdrawals = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable([By.CLASS_NAME, self.my_dict['lnkWithdrawals']]))
        withdrawals.click()

    def select_trading_account(self, withdrawal_form):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located([By.ID, self.my_dict['ddTradingAccount']]))
        trading_account = self.driver.find_element(By.ID, self.my_dict['ddTradingAccount'])
        self.driver.execute_script(CommonFunctions.find_element('withdraw_TradingAccount'), trading_account)
        CommonFunctions.select_values(self.driver.find_element(By.ID, self.my_dict['ddSelectTradingAccount']),
                                      withdrawal_form.get_trading_account())

    def amount(self, withdrawal_form):
        self.driver.find_element(By.ID, self.my_dict['txtAmount']).send_keys(withdrawal_form.get_amount() + Keys.INSERT)

    def withdrawal_purpose(self, withdrawal_form):
        self.driver.find_element(By.ID, self.my_dict['txtWithdrawalPurpose']).send_keys(
            withdrawal_form.get_withdrawal_purpose() + Keys.INSERT)

    def select_withdrawal_type(self, withdrawal_form):
        withdrawal_type = self.driver.find_element(By.ID, self.my_dict['ddWithdrawalType'])
        self.driver.execute_script(CommonFunctions.find_element('withdraw_withdrawalType'), withdrawal_type)
        CommonFunctions.select_values(self.driver.find_element(By.ID, self.my_dict['ddSelectWithdrawalType']),
                                      withdrawal_form.get_withdrawal_type())

    def select_banking_information(self, withdrawal_form):
        banking_information = self.driver.find_element(By.ID, self.my_dict['ddBankingInformation'])
        self.driver.execute_script(CommonFunctions.find_element('withdraw_BankingInformation'), banking_information)
        CommonFunctions.select_values(self.driver.find_element(By.ID, self.my_dict['ddSelectBankingInformation']),
                                      withdrawal_form.get_banking_information())

    def bank_name(self, withdrawal_form):
        self.driver.find_element(By.ID, self.my_dict['txtBankName']).send_keys(withdrawal_form.get_bank_name() + Keys.INSERT)

    def beneficiary_name(self, withdrawal_form):
        self.driver.find_element(By.ID, self.my_dict['txtBeneficiaryName']).send_keys(withdrawal_form.get_beneficiary_name() + Keys.INSERT)

    def select_country(self, withdrawal_form):
        country = self.driver.find_element(By.ID, self.my_dict['ddCountry'])
        self.driver.execute_script(CommonFunctions.find_element('withdraw_BankingInformation2_bankCountry'), country)
        CommonFunctions.select_values(self.driver.find_element(By.ID, self.my_dict['ddSelectCountry']),
                                      withdrawal_form.get_country())

    def bank_address(self, withdrawal_form):
        self.driver.find_element(By.ID, self.my_dict['txtBankAddress']).send_keys(withdrawal_form.get_bank_address() + Keys.INSERT)

    def swift_bic(self, withdrawal_form):
        self.driver.find_element(By.ID, self.my_dict['txtSwiftBIC']).send_keys(withdrawal_form.get_swift_bic() + Keys.INSERT)

    def beneficiary_account_no_iban(self, withdrawal_form):
        self.driver.find_element(By.ID, self.my_dict['txtBeneficiaryAccountNumberIBAN']).\
            send_keys(withdrawal_form.get_beneficiary_account_no_iban() + Keys.INSERT)

    def account_currency(self, withdrawal_form):
        self.driver.find_element(By.ID, self.my_dict['txtAccountCurrency']).send_keys(withdrawal_form.get_account_currency() + Keys.INSERT)

    def sort_code_bsb(self, withdrawal_form):
        self.driver.find_element(By.ID, self.my_dict['txtAccountCurrency']).send_keys(withdrawal_form.get_sort_code_bsb() + Keys.INSERT)

    def online_payment_type(self, withdrawal_form):
        online_payment_gateway = self.driver.find_element(By.ID, self.my_dict['ddOnlinePaymentType'])
        self.driver.execute_script(CommonFunctions.find_element('withdraw_PaymentGateway'), online_payment_gateway)
        CommonFunctions.select_values(self.driver.find_element(By.ID, self.my_dict['ddSelectOnlinePaymentType']),
                                      withdrawal_form.get_online_payment_type())

    def send_otp(self):
        self.driver.find_element(By.CLASS_NAME, self.my_dict['btnSendOtp']).click()

    def processing_bar(self):
        process = WebDriverWait(self.driver, 60).until(
            EC.invisibility_of_element_located([By.CLASS_NAME, self.my_dict['lblProcessing']]))
        return process

    def email_verification_code(self, withdrawal_form):
        self.processing_bar()
        self.driver.find_element(By.CLASS_NAME, self.my_dict['txtEmailVerificationCode']).send_keys(
            withdrawal_form.email_verification_code() + Keys.INSERT)

    def submit_withdrawal_request(self):
        self.driver.find_element(By.CSS_SELECTOR, self.my_dict['btnSubmit']).click()

    def fill_withdrawal_request(self, withdrawal_form):
        self.set_withdrawal_request_form_details(withdrawal_form)
        self.submit_withdrawal_request()

    def set_withdrawal_request_form_details(self, withdrawal_form):
        self.select_trading_account(withdrawal_form)
        self.withdrawal_purpose(withdrawal_form)
        self.select_withdrawal_type(withdrawal_form)
        self.amount(withdrawal_form)
        self.send_otp()
        self.email_verification_code(withdrawal_form)
