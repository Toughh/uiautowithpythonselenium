import os
import unittest
from pathlib import Path

from dotenv import load_dotenv

from test.client.application.testPersonalInformation import PersonalInformationTest

test_path = "../test"
test_single_test = "test_IC_TC1_To_verify_db_records_when_IC_user_edit_personal_information_with_individual_client_type"
global dotenv_path


class TestRun(unittest.TestCase):
    dotenv_path = Path('D:/MyPortalUIAutomation/myportal_ui_automation/test/staging.env')
    load_dotenv(dotenv_path=dotenv_path)

    def test_run_single_test(self):
        print(os.environ.get('TRADING_ACCOUNT_SETTINGS_ENDPOINT'))
        # test_personal_information = PersonalInformationTest.run(self)
        test_personal_information = PersonalInformationTest(test_single_test).run()
        return test_personal_information

    @unittest.SkipTest
    def test_run_test_suite(self):
        global test_path
        loader = unittest.TestLoader()
        test_path = test_path
        suite = loader.discover(test_path)
        runner = unittest.TextTestRunner()
        runner.run(suite)


if __name__ == "__main__":
    unittest.main()
# import argparse
# import os
# import sys
# import unittest
#
# import dotenv
#
# from test.client.application.testChangeEmail import ChangeEmailTest
#
# from dotenv import load_dotenv
# from pathlib import Path
#
# test_path = "D:/MyPortalUIAutomation/myportal_ui_automation/test"
# test_single_test = "test_IC_TC1_To_verify_if_user_is_able_to_change_username_and_re_login"
#
#
# class TestRun(unittest.TestCase):
#
#     def test_run_single_test(self):
#         parser = argparse.ArgumentParser(description='Select env:')
#         parser.add_argument('num', help='checking')
#         args = parser.parse_args()
#         print(args)
#         n = len(sys.argv)
#         env = sys.argv[n - 1]
#         print(sys.argv)
#         # report = sys.argv[n-4] + sys.argv[n-3]
#         print("Hello")
#         dotenv_path = Path('D:/MyPortalUIAutomation/myportal_ui_automation/test/staging.env')
#         load_dotenv(dotenv_path=dotenv_path)
#         print(dotenv.get_key(dotenv_path, 'TRADING_ACCOUNT_SETTINGS_ENDPOINT'))
#         # elif env == 'staging':
#         #     dotenv_path = Path('D:/MyPortalUIAutomation/myportal_ui_automation/test/staging.env')
#         #     load_dotenv(dotenv_path=dotenv_path)
#         #     print(os.environ.get('TRADING_ACCOUNT_SETTINGS_ENDPOINT'))
#         # global test_path
#         # loader = unittest.TestLoader()
#         # test_path = test_path
#         # suite = loader.discover(test_path)
#         # runner = unittest.TextTestRunner()
#         # runner.run(suite)
#
#
# if __name__ == "__main__":
#     unittest.main()
