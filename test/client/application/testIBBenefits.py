from common.commonFunctions import CommonFunctions
import unittest
import allure

from common.steps.clientSteps import ClientSteps

username = ""


class IBBenefitsTest(unittest.TestCase):

    def setUp(self):
        global username
        username = CommonFunctions.generate_random_email()

    @allure.feature('IB Benefits Page')
    @allure.story('US12345: As a end user, I should be able to login as an IB user so that I can continue to '
                  'register myself as an IB User')
    @allure.testcase('To verify if user is able to login as an IB user and land into IB Benefits page')
    def test_IB_TC1_To_verify_if_user_is_able_to_login_as_an_IB_user_and_land_into_IB_Benefits_page(self):
        cs = ClientSteps()
        cs.api_ib_registration(username)
        self.assertEqual('Introducing Broker Benefits', cs.is_ib_benefits_page_displayed(),
                         'IB Benefits Page not displayed')

    def tearDown(self):
        ClientSteps.teardown("IB Benefits Page")


if __name__ == "__main__":
    unittest.main()
