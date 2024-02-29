class UploadFilesDAO:

    def __init__(self, type_of_file: str, email: str, filename: str, file_format: str):
        self._type_of_file = type_of_file
        self._email = email
        self._filename = filename
        self._file_format = file_format

    def get_type_of_file(self):
        return self._type_of_file

    def set_type_of_file(self, val):
        self._type_of_file = val

    def get_email(self):
        return self._email

    def set_email(self, val):
        self._email = val

    def get_filename(self):
        return self._filename

    def set_filename(self, val):
        self._filename = val

    def get_file_format(self):
        return self._file_format

    def set_file_format(self, val):
        self._file_format = val
