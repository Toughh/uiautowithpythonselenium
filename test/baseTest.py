import unittest

from common.enum.client.clientType import ClientType
from common.enum.client.regulatorPlatformTierType import RegulatorPlatformTierType
from common.steps.adminSteps import AdminSteps
from common.steps.clientSteps import ClientSteps


class BaseTest(unittest.TestCase):
    @staticmethod
    def submit_application_converting_demo_to_real_account(client_type, regulator_platform_tier):
        cs = ClientSteps
        cs.open_live_account()
        cs.submit_application_with_trading_accounts(client_type, regulator_platform_tier)

    @staticmethod
    def change_bo_id_por_status_ic(username, bo_id_status, bo_por_status):
        # cs = ClientSteps
        # cs.submit_ic_application(username)
        ast = AdminSteps
        ast.validate_bo_id_por_change_status_for_ic_or_ib(username, bo_id_status, bo_por_status)

    @staticmethod
    def change_bo_id_por_status_ib(username, bo_id_status, bo_por_status):
        cs = ClientSteps
        cs.submit_ib_application(username)
        cs.validate_if_user_able_to_logout()
        ast = AdminSteps
        ast.validate_bo_id_por_change_status_for_ic_or_ib(username, bo_id_status, bo_por_status)

    @staticmethod
    def convert_ic_to_ib(username, bo_id_status, bo_por_status):
        BaseTest.change_bo_id_por_status_ic(username, bo_id_status, bo_por_status)
        ast = AdminSteps
        ast.ic_to_ib()

    @staticmethod
    def convert_ib_to_ic(username, bo_id_status, bo_por_status):
        BaseTest.change_bo_id_por_status_ib(username, bo_id_status, bo_por_status)
        ast = AdminSteps
        ast.ib_to_ic()

    @staticmethod
    def ib_application_change_status(username, bo_id_status, bo_por_status):
        cs = ClientSteps
        cs.submit_ib_application(username)
        ast = AdminSteps
        ast.validate_bo_ib_application_status(username, bo_id_status, bo_por_status)

    @staticmethod
    def ib_compliance_change_status(username, bo_id_status, bo_por_status, compliance_id_status, comp_id_status,
                                    comp_por_status):
        cs = ClientSteps
        cs.submit_ib_application(username)
        ast = AdminSteps
        ast.validate_compliance_change_status_for_ib(username, bo_id_status, bo_por_status, compliance_id_status,
                                                     comp_id_status, comp_por_status)

    @staticmethod
    def ic_compliance_change_status(username, bo_id_status, bo_por_status, compliance_id_status, comp_id_status,
                                    comp_por_status):
        cs = ClientSteps
        cs.submit_ic_application(username)
        ast = AdminSteps
        ast.validate_compliance_change_status_for_ic(username, bo_id_status, bo_por_status, compliance_id_status,
                                                     comp_id_status, comp_por_status)

    @staticmethod
    def ib_registered_clients(username, client_email, bo_id_status, bo_por_status, compliance_id_status, comp_id_status,
                              comp_por_status):
        client_type = ClientType.individual.value
        regulator_platform_tier = RegulatorPlatformTierType.mex_atlantic_mt4_standard.value
        BaseTest.ib_compliance_change_status(username, bo_id_status, bo_por_status, compliance_id_status,
                                             comp_id_status, comp_por_status)
        cs = ClientSteps
        cs.ib_register_clients(client_email, username, client_type, regulator_platform_tier)

    @staticmethod
    def ic_re_register_after_admin_approval(username, bo_id_status, bo_por_status, compliance_id_status, comp_id_status,
                                            comp_por_status,
                                            edit_info_status):
        BaseTest.ic_compliance_change_status(username, bo_id_status, bo_por_status, compliance_id_status,
                                             comp_id_status, comp_por_status)
        cs = ClientSteps
        cs.api_ic_duplicate_registration_without_trading_account_settings(username)
        ast = AdminSteps
        ast.edit_info_requests_change_status(username, edit_info_status)
