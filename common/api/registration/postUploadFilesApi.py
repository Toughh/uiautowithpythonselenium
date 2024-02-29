import os
import requests
# from dotenv import load_dotenv
upload_files_endpoint = os.getenv('UPLOAD_FILES_ENDPOINT')
print("Hello")
print(upload_files_endpoint)
x_token = os.environ.get('X_TOKEN')
upload_file_path = os.environ.get('UPLOAD_FILE')
res = {}


class UploadFilesApi:
    @staticmethod
    def get_upload_files_res(data, files):
        global res
        res = requests.post(
            url=upload_files_endpoint,
            headers={'x-token': x_token},
            data=data,
            files=[('file', (files['filename'], open(upload_file_path + str(files['filename']), 'rb'), 'image/' + str(files['file_format'])))])
        assert res.status_code == 200, 'Upload Api returns status_code as: ' + str(res.status_code) + \
                                       '\nResponse content:\n' + str(res.content)
        return res.json()

    @staticmethod
    def get_status(data, files):
        status = UploadFilesApi.get_upload_files_res(data, files)['status']
        return status

    @staticmethod
    def get_file(data, files):
        file = UploadFilesApi.get_upload_files_res(data, files)['file']
        return file

    @staticmethod
    def get_data_file(data, files):
        file = UploadFilesApi.get_upload_files_res(data, files)['data']['file']
        return file
