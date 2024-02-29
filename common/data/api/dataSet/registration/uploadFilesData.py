import os


class UploadFilesData:

    @staticmethod
    def upload_files_data(username):
        ufd = {'type': 'DOC', 'email': username}
        return ufd

    @staticmethod
    def upload_files():
        filename = 'actual.jpg'
        uf = {'filename': filename, 'file_format': 'jpeg'}
        return uf
