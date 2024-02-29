import os
import sys
import unittest

import test.client.application.testChangeEmail

from dotenv import load_dotenv
from pathlib import Path

import test

test_path = "C:/MyPortalUIAutomation/myportal_ui_automation/test"
# test_single_test = "test_IC_TC1_To_verify_if_user_is_able_to_change_username_and_re_login"


class StagingRun:
    print("Started")


class Child(StagingRun):

    # @staticmethod
    # def run_single_test():
    #     n = sys.argv
    #     print("Hello")
    #     print(n)
        # env = sys.argv[n - 1]
        # if env == 'test':
        #     dotenv_path = Path('/home/ubuntu/MyPortalUIAutomation/myportal_ui_automation/test/test.env')
        #     load_dotenv(dotenv_path=dotenv_path)
        #     print(os.environ.get('TRADING_ACCOUNT_SETTINGS_ENDPOINT'))
        # elif env == 'staging':
        #     dotenv_path = Path('/home/ubuntu/MyPortalUIAutomation/myportal_ui_automation/test/staging.env')
        #     load_dotenv(dotenv_path=dotenv_path)
        #     print(os.environ.get('TRADING_ACCOUNT_SETTINGS_ENDPOINT'))
        # test_change_email = test.client.application.testChangeEmail.ChangeEmailTest(test_single_test)
        # test_change_email.run()

    @staticmethod
    def run_test_suite():
        global test_path
        loader = unittest.TestLoader()
        test_path = test_path
        suite = loader.discover(test_path)
        runner = unittest.TextTestRunner()
        runner.run(suite)


def main():
    test_run = Child
    test_run.run_test_suite()


main()
