import time

from common.data.application.personalInformationData import PersonalInformationData
from common.data.funds.withdrawalData import WithdrawalData
from common.pageObjects.basePage import BasePage
from common.pageObjects.client.accountsPage import AccountsPage
from common.pageObjects.client.applicationPage import ApplicationPage
from common.pageObjects.client.changeEmailPage import ChangeEmailPage
from common.pageObjects.client.dashboardPage import DashboardPage
from common.pageObjects.client.financePage import FinancePage
from common.pageObjects.client.ibBenefitsPage import IBBenefitsPage
from common.pageObjects.client.ibPage import IBPage
from common.pageObjects.client.loginPage import LoginPage
from common.pageObjects.client.resetPasswordPage import ResetPasswordPage
from common.pageObjects.client.uploadedDocumentsPage import UploadedDocumentsPage
from common.setup.setup import SetupPage

driver = ''


class ClientSteps:

    @staticmethod
    def login_client(username):
        global driver
        cs = SetupPage(driver)
        driver = cs.client_setup()
        lp = LoginPage(driver)
        result = lp.client_login(username)
        return result

    @staticmethod
    def login_client_with_new_password(username):
        global driver
        cs = SetupPage(driver)
        driver = cs.client_setup()
        lp = LoginPage(driver)
        result = lp.client_re_login_with_changed_password(username)
        return result

    @staticmethod
    def api_ic_registration_with_trading_accounts_settings(username):
        global driver
        sp = SetupPage(username)
        driver = sp.ic_setup_with_trading_accounts_settings(username)
        title = driver.title
        return title

    @staticmethod
    def api_ic_registration_without_trading_accounts_settings(username):
        global driver
        sp = SetupPage(username)
        driver = sp.ic_setup_without_trading_accounts_settings(username)
        title = driver.title
        return title

    @staticmethod
    def api_ic_duplicate_registration_without_trading_account_settings(username):
        global driver
        sp = SetupPage(username)
        driver = sp.ic_duplicate_setup_without_trading_account_settings(username)
        title = driver.title
        return title

    @staticmethod
    def api_ic_campaign_registration_with_trading_account_settings(username):
        global driver
        sp = SetupPage(username)
        driver = sp.ic_campaign_setup_with_trading_account_settings(username)
        title = driver.title
        return title

    @staticmethod
    def api_ic_campaign_registration_without_trading_account_settings(username):
        global driver
        sp = SetupPage(username)
        driver = sp.ic_campaign_setup_without_trading_account_settings(username)
        return driver

    @staticmethod
    def api_ib_registration(username):
        global driver
        sp = SetupPage(username)
        driver = sp.ib_setup(username)
        title = driver.title
        return title

    @staticmethod
    def api_demo_registration(username):
        global driver
        sp = SetupPage(username)
        driver = sp.demo_setup(username)
        title = driver.title
        return title

    @staticmethod
    def validate_ic_personal_info_error_message(username):
        ClientSteps.api_ic_registration_with_trading_accounts_settings(username)
        ap = ApplicationPage(driver)
        return ap.validate_personal_info_ic_error_message()

    @staticmethod
    def navigate_to_live_accounts():
        global driver
        ap = AccountsPage(driver)
        return ap.navigate_to_live_accounts()

    @staticmethod
    def navigate_to_demo_accounts():
        global driver
        ap = AccountsPage(driver)
        return ap.navigate_to_demo_accounts()

    @staticmethod
    def validate_ic_trading_capability_assessment_error_message(username):
        ClientSteps.api_ic_registration_with_trading_accounts_settings(username)
        ap = ApplicationPage(driver)
        return ap.validate_trading_capability_assessment_ic_error_message()

    @staticmethod
    def update_and_submit_ic_application(client_type):
        cs = ClientSteps
        cs.validate_ic_personal_info_records_in_db(client_type, None)
        ap = ApplicationPage(driver)
        ap.submit_personal_info()
        ap.fill_trading_capability_questions_on_already_email_verified()
        ap.upload_proof_of_address()
        return ap.click_finish()

    @staticmethod
    def update_and_submit_ib_application(username, client_type):
        ClientSteps.api_ib_registration(username)
        ap = ApplicationPage(driver)
        ap.navigate_to_personal_information_page()
        # ap.validate_personal_info_ib_user_with_api()
        try:
            if client_type == "Individual" or client_type == "Institutional/Corporate":
                ib_personal_info_data = PersonalInformationData.personal_info(client_type)
                ap.fill_ib_personal_info_with_individual_institutional_corporate(ib_personal_info_data)
            elif client_type == "Corporate":
                ib_personal_info_data = PersonalInformationData.personal_info(client_type)
                ap.fill_ib_personal_info_with_corporate(ib_personal_info_data)
            else:
                ib_personal_info_data = PersonalInformationData.personal_info(client_type)
                ap.fill_ib_personal_info_details_with_joint_account(ib_personal_info_data)
        except TypeError:
            print("client_type doesn't exist. Please check !!!")
        ap.upload_proof_of_address()
        return ap.click_finish()

    @staticmethod
    def validate_ic_submitted_trading_assessment_questions(username):
        ClientSteps.api_ic_registration_with_trading_accounts_settings(username)
        ap = ApplicationPage(driver)
        ap.click_on_application()
        ap.edit_personal_info()
        ic_date_of_birth_data = PersonalInformationData.personal_info("1990-03-02")
        ap.date_of_birth(ic_date_of_birth_data)
        ap.submit_personal_info()
        trading_assessment_ques = ap.fill_trading_capability_questions_on_already_email_verified()
        return trading_assessment_ques

    @staticmethod
    def validate_ib_submitted_personal_info(username):
        ClientSteps.api_ib_registration(username)
        ap = ApplicationPage(driver)
        ap.click_on_application()
        ap.submit_personal_info()

    @staticmethod
    def submit_ic_application(username):
        ClientSteps.validate_ic_submitted_trading_assessment_questions(username)
        ap = ApplicationPage(driver)
        ap.upload_proof_of_address()
        return ap.click_finish()

    @staticmethod
    def submit_ib_application(username):
        ClientSteps.validate_ib_submitted_personal_info(username)

    @staticmethod
    def submit_ic_campaign_application(username, client_type, client_email):
        ClientSteps.update_and_submit_ic_campaign_user(username, client_type, client_email)
        ap = ApplicationPage(driver)
        ap.fill_trading_capability_questions_on_already_email_verified()
        ap.upload_proof_of_address()
        result = ap.click_finish()
        return result

    @staticmethod
    def navigate_to_dashboard_after_filling_ic_campaign_details(username, client_type, client_email):
        ClientSteps.submit_ic_campaign_application(username, client_type, client_email)
        db = DashboardPage(driver)
        result = db.is_dashboard_page_displayed()
        return result

    @staticmethod
    def navigate_to_dashboard_after_filling_ic_details_with_c_trader(username, client_type, regulator_platform_tier):
        ClientSteps.validate_ic_personal_info_records_in_db(client_type, None)
        ap = ApplicationPage(driver)
        ap.submit_personal_info()
        ClientSteps.validate_trading_account_settings(username, regulator_platform_tier)
        ap.fill_trading_capability_assessment()
        ap.upload_proof_of_address()
        db = DashboardPage(driver)
        result = db.is_dashboard_page_displayed()
        return result

    @staticmethod
    def navigate_to_dashboard_once_converted_demo_to_real(username, client_type, client_email):
        ClientSteps.submit_ic_campaign_application(username, client_type, client_email)
        db = DashboardPage(driver)
        result = db.is_dashboard_page_displayed()
        return result

    @staticmethod
    def navigate_to_dashboard_after_filling_application_details(username):
        ClientSteps.submit_ic_application(username)
        db = DashboardPage(driver)
        result = db.is_dashboard_page_displayed()
        return result

    @staticmethod
    def validate_ic_personal_info_records_in_db(client_type, client_email):
        ap = ApplicationPage(driver)
        ap.navigate_to_personal_information_page()
        # ap.validate_personal_info_ic_user_with_api()
        try:
            if client_type == "Individual" or client_type == "Institutional/Corporate":
                ic_personal_info_data = PersonalInformationData.personal_info(client_type)
                ap.fill_ic_personal_info_with_individual_institutional_corporate(ic_personal_info_data)
            elif client_type == "Corporate":
                ic_personal_info_data = PersonalInformationData.personal_info(client_type)
                ap.fill_ic_personal_info_with_corporate(ic_personal_info_data)
            elif client_type == "Joint Account":
                ic_personal_info_data = PersonalInformationData.personal_info(client_type)
                ap.fill_ic_personal_info_details_with_joint_account(ic_personal_info_data)
            else:
                print("client_type doesn't exist. Please check !!!")
        except TypeError:
            print("Client Type Error.. Please check!!!")
        return ap.edit_personal_info()
        # result = ap.validate_personal_info_records_in_db_based_on_client_type(client_type, client_email)
        # return result

    @staticmethod
    def validate_ic_campaign_personal_info_records_in_db(client_type, client_email):
        ap = ApplicationPage(driver)
        ap.validate_personal_info_ic_campaign_user_with_api()
        try:
            if client_type == "Individual" or client_type == "Institutional/Corporate":
                ic_personal_info_data = PersonalInformationData.personal_info(client_type)
                ap.fill_ic_personal_info_with_individual_institutional_corporate(ic_personal_info_data)
            elif client_type == "Corporate":
                ic_personal_info_data = PersonalInformationData.personal_info(client_type)
                ap.fill_ic_personal_info_with_corporate(ic_personal_info_data)
            elif client_type == "Joint Account":
                ic_personal_info_data = PersonalInformationData.personal_info(client_type)
                ap.fill_ic_personal_info_details_with_joint_account(ic_personal_info_data)
            else:
                print("client_type doesn't exist. Please check !!!")
        except TypeError:
            print("Client Type Error.. Please check!!!")
        ap.edit_personal_info()
        result = ap.validate_personal_info_records_in_db_based_on_client_type(client_type, client_email)
        return result

    # @staticmethod
    # def validate_ib_personal_info_records_in_db(username, client_type, client_email):
    #     ap = ApplicationPage(driver)
    #     ap.validate_personal_info_ib_user_with_api()
    #     try:
    #         if client_type == "Individual" or client_type == "Institutional/Corporate":
    #             ib_personal_info_data = PersonalInformationData.personal_info(client_type)
    #             ap.fill_ib_personal_info_with_individual_institutional_corporate(ib_personal_info_data)
    #         elif client_type == "Corporate":
    #             ib_personal_info_data = PersonalInformationData.personal_info(client_type)
    #             ap.fill_ib_personal_info_with_corporate(ib_personal_info_data)
    #         elif client_type == "Joint Account":
    #             ib_personal_info_data = PersonalInformationData.personal_info(client_type)
    #             ap.fill_ib_personal_info_details_with_joint_account(ib_personal_info_data)
    #         else:
    #             print("client_type doesn't exist. Please check !!!")
    #     except TypeError:
    #         print("Client Type Error.. Please check!!!")
    #     cs = ClientSteps
    #     result = cs.validate_personal_information_under_logged_in_user(username)
    #     return result

    @staticmethod
    def is_success_mes_displayed_after_filling_ib_application(username):
        ClientSteps.submit_ib_application(username)
        ap = ApplicationPage(driver)
        result = ap.ib_success_mes()
        return result

    @staticmethod
    def navigate_to_dashboard_editing_personal_info(client_type):
        ClientSteps.update_and_submit_ic_application(client_type)
        db = DashboardPage(driver)
        result = db.is_dashboard_page_displayed()
        return result

    @staticmethod
    def is_ib_success_mes_displayed_after_editing_personal_info(username, client_type):
        ClientSteps.update_and_submit_ib_application(username, client_type)
        ap = ApplicationPage(driver)
        result = ap.ib_success_mes()
        return result

    @staticmethod
    def get_live_accounts_data():
        acc = AccountsPage(driver)
        client_trading_account = acc.get_trading_card_info()
        return client_trading_account

    @staticmethod
    def is_ib_benefits_page_displayed():
        ib = IBBenefitsPage(driver)
        ib.is_ib_benefits_page_displayed()

    @staticmethod
    def update_and_submit_ic_campaign_user_personal_info(username, client_type, client_email):
        ClientSteps.api_ic_campaign_registration_with_trading_account_settings(username)
        fetch_db_records = ClientSteps.validate_ic_personal_info_records_in_db(client_type, client_email)
        return fetch_db_records

    @staticmethod
    def update_and_submit_ic_campaign_user(username, client_type, client_email):
        ClientSteps.update_and_submit_ic_campaign_user_personal_info(username, client_type, client_email)
        ap = ApplicationPage(driver)
        ap.submit_personal_info()

    @staticmethod
    def validate_otp_under_personal_information(client_type):
        ap = ApplicationPage(driver)
        ap.navigate_to_personal_information_page()
        ap.validate_otp(client_type)

    @staticmethod
    def validate_otp_under_change_mobile_number(client_type):
        ap = ApplicationPage(driver)
        ap.navigate_to_change_mobile_number(client_type)

    @staticmethod
    def validate_live_accounts_data_in_db(username):
        accounts_page = AccountsPage(driver)
        accounts_page.validate_live_accounts_records_in_db(username)

    @staticmethod
    def validate_demo_accounts_data_in_db(username):
        accounts_page = AccountsPage(driver)
        accounts_page.validate_demo_accounts_records_in_db(username)

    @staticmethod
    def validate_if_user_able_to_logout():
        ap = ApplicationPage(driver)
        ap.click_logout()

    @staticmethod
    def validate_if_user_able_to_change_email(changed_email):
        ap = ApplicationPage(driver)
        ap.click_change_email()
        cep = ChangeEmailPage(driver)
        result = cep.validate_if_user_able_to_change_email(changed_email)
        return result

    @staticmethod
    def validate_if_user_able_to_reset_password(username):
        ap = ApplicationPage(driver)
        ap.click_reset_password()
        rp = ResetPasswordPage(driver)
        rp.validate_if_able_to_reset_password()
        result = ClientSteps.login_client_with_new_password(username)
        return result

    @staticmethod
    def validate_if_user_able_to_reset_trading_password():
        ap = ApplicationPage(driver)
        ap.click_change_account_password()
        rp = ResetPasswordPage(driver)
        result = rp.validate_if_able_to_reset_trading_password()
        return result

    @staticmethod
    def validate_if_user_able_to_upload_documents(status):
        ap = ApplicationPage(driver)
        ap.click_uploaded_documents()
        rp = UploadedDocumentsPage(driver)
        rp.validate_user_able_to_see_admin_uploaded_documents()
        result = rp.validate_if_able_to_upload_documents(status)
        return result

    @staticmethod
    def validate_trading_account_settings(regulator_platform_tier):
        ap = ApplicationPage(driver)
        trading_account_settings_data = PersonalInformationData.trading_account_settings()
        ap.fill_trading_account_settings_and_submit(regulator_platform_tier, trading_account_settings_data)
        # ap.validate_db_for_trading_account_settings(username)

    @staticmethod
    def validate_proof_of_identity():
        ap = ApplicationPage(driver)
        proof_of_identity_data = PersonalInformationData.proof_of_identity()
        ap.upload_proof_of_identity_and_submit(proof_of_identity_data)

    # @staticmethod
    # def navigate_to_ib_clients(client_type, client_email):
    #     ib_page = IBPage(driver)
    #     ib_page.switch_to_client_window_and_refresh()
    #     ib_page.submit_register_clients(client_email)
    #     ClientSteps.validate_ic_personal_info_records_in_db(client_type, client_email)

    @staticmethod
    def validate_personal_information_for_ib_registered_clients(client_type, client_email):
        ib_page = IBPage(driver)
        ib_page.submit_register_clients(client_email)
        ClientSteps.validate_ic_personal_info_records_in_db(client_type, client_email)

    @staticmethod
    def validate_otp_for_ib_registered_clients(client_type, client_email):
        ClientSteps.validate_personal_information_for_ib_registered_clients(client_type, client_email)
        ap = ApplicationPage(driver)
        ap.validate_otp(client_type)

    @staticmethod
    def ib_register_clients(client_email, client_type, regulator_platform_tier):
        ClientSteps.validate_personal_information_for_ib_registered_clients(client_type, client_email)
        ap = ApplicationPage(driver)
        ap.submit_personal_info()
        ClientSteps.validate_trading_account_settings(regulator_platform_tier)
        ap.fill_trading_capability_questions_on_already_email_verified()
        ClientSteps.validate_proof_of_identity()
        ap.upload_proof_of_address()

    @staticmethod
    def submit_application_with_trading_accounts(client_type, regulator_platform_tier):
        ap = ApplicationPage(driver)
        personal_info_data = PersonalInformationData.personal_info(client_type)
        ap.date_of_birth(personal_info_data)
        ap.submit_personal_info()
        # ClientSteps.validate_trading_account_settings(regulator_platform_tier)
        ap.submit_trading_account_settings()
        ap.fill_trading_capability_questions_on_already_email_verified()
        ClientSteps.validate_proof_of_identity()
        ap.upload_proof_of_address()

    @staticmethod
    def validate_personal_information_under_logged_in_user(username):
        ClientSteps.login_client(username)
        ap = ApplicationPage(driver)
        ap.click_personal_information()
        result = ap.validate_personal_information_under_logged_in_user(username)
        return result

    @staticmethod
    def validate_trading_account_settings_dropdown_list(regulator_platform_tier_type):
        ap = ApplicationPage(driver)
        ap.validate_trading_account_dropdown_values(regulator_platform_tier_type)

    @staticmethod
    def open_live_account():
        ap = AccountsPage(driver)
        ap.open_live_account()

    @staticmethod
    def navigate_to_dashboard():
        db = DashboardPage(driver)
        result = db.is_dashboard_page_displayed()
        return result

    @staticmethod
    def fill_withdrawal_request(trading_account_number):
        fp = FinancePage(driver)
        fp.withdrawals()
        withdrawal_data = WithdrawalData.withdrawal_form(trading_account_number)
        print(trading_account_number)
        result = fp.fill_withdrawal_request(withdrawal_data)
        return result

    @staticmethod
    def teardown(test):
        bp = BasePage(driver)
        bp.attach_screenshot(test)
        sp = SetupPage(driver)
        return sp.teardown()
