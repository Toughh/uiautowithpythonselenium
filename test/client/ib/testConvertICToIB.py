from common.commonFunctions import CommonFunctions
import unittest
import allure

from common.steps.adminSteps import AdminSteps
from common.steps.clientSteps import ClientSteps
from test.baseTest import BaseTest

username = ""
client_email = ""


class ConvertICtoIBTest(unittest.TestCase):

    def setUp(self):
        global username, client_email
        username = CommonFunctions.generate_random_email()
        client_email = CommonFunctions.generate_random_email()

    @allure.feature('Conversion IC to IB')
    @allure.story(
        'US12345: As an IC user, I should be able to convert to IB once admin convert me from IC to IB so that I can '
        'continue to trade as IB user')
    @allure.testcase('To verify if IC user can be converted to IB')
    def test_ICToIB_TC1_To_verify_if_ic_user_can_be_converted_to_ib(self):
        cs = ClientSteps
        bs = BaseTest
        bs.convert_ic_to_ib(username, "Approve", "Approve")
        ast = AdminSteps
        ast.switch_to_client_portal(window_tab_index=1)
        self.assertEqual('Introducing Broker Benefits', cs.is_ib_benefits_page_displayed(),
                         'IB Benefits Page not displayed')

    # @allure.feature('Conversion IB to IC')
    # @allure.story(
    #     'US12345: As an IB user, I should be able to convert to IC once admin convert me from IB to IC so that I can '
    #     'continue to trade as IC user')
    # @allure.testcase('To verify if IB user can be converted to IC')
    # def test_ICToIB_TC1_To_verify_if_ib_user_can_be_converted_to_ic(self):
    #     cs = ClientSteps
    #     bs = BaseTest
    #     bs.convert_ib_to_ic(username, "Approve", "Approve")
    #     ast = AdminSteps
    #     ast.switch_to_client_portal(window_tab_index=1)
    #     self.assertNotEqual('Introducing Broker Benefits', cs.is_ib_benefits_page_displayed(),
    #                         'IB Benefits Page is displayed')

    # def tearDown(self):
    #     ClientSteps.teardown("IC to IB")


if __name__ == "__main__":
    unittest.main()
