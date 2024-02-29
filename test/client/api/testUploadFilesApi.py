from common.api.registration.postUploadFilesApi import UploadFilesApi
from common.commonFunctions import CommonFunctions
from common.data.api.dataSet.registration.uploadFilesData import UploadFilesData
import unittest
import allure


class UploadFilesApiTest(unittest.TestCase):

    @allure.story('US12345: As a end user, I should be able to upload files and post the api request')
    @allure.testcase('To_verify_if_user_is_able_to_upload_files_through_api')
    def test_To_verify_if_user_is_able_to_upload_files_through_api(self):
        upload_data = UploadFilesData.upload_files_data(CommonFunctions.generate_random_email())
        upload_files = UploadFilesData.upload_files()
        UploadFilesApi.get_file(upload_data, upload_files)


if __name__ == "__main__":
    unittest.main()
