class RegisterNewAccountDAO:

    def __init__(self, username: str, account_type: str, ip_country: str, first_name: str, last_name: str,
                 real_account_type: str, mobile_number: str, phone: str, dob: str, next_step: str, country: str,
                 otp_checker: str, document_id: str, document_id_2: str, document_por: str, document_por_2: str):
        self._username = username
        self._account_type = account_type
        self._ip_country = ip_country
        self._first_name = first_name
        self._last_name = last_name
        self._real_account_type = real_account_type
        self._mobile_number = mobile_number
        self._phone = phone
        self._dob = dob
        self._next_step = next_step
        self._country = country
        self._otp_checker = otp_checker
        self._document_id = document_id
        self._document_id_2 = document_id_2
        self._document_por = document_por
        self._document_por_2 = document_por_2

    def get_username(self):
        return self._username

    def set_username(self, val):
        self._username = val

    def get_account_type(self):
        return self._account_type

    def set_account_type(self, val):
        self._account_type = val

    def get_ip_country(self):
        return self._ip_country

    def set_ip_country(self, val):
        self._ip_country = val

    def get_first_name(self):
        return self._first_name

    def set_first_name(self, val):
        self._first_name = val

    def get_last_name(self):
        return self._last_name

    def set_last_name(self, val):
        self._last_name = val

    def get_real_account_type(self):
        return self._real_account_type

    def set_real_account_type(self, val):
        self._real_account_type = val

    def get_mobile_number(self):
        return self._mobile_number

    def set_mobile_number(self, val):
        self._mobile_number = val

    def get_phone(self):
        return self._phone

    def set_phone(self, val):
        self._phone = val

    def get_dob(self):
        return self._dob

    def set_dob(self, val):
        self._dob = val

    def get_next_step(self):
        return self._next_step

    def set_next_step(self, val):
        self._next_step = val

    def get_country(self):
        return self._country

    def set_country(self, val):
        self._country = val

    def get_otp_checker(self):
        return self._otp_checker

    def set_otp_checker(self, val):
        self._otp_checker = val

    def get_document_id(self):
        return self._document_id

    def set_document_id(self, val):
        self._document_id = val

    def get_document_id_2(self):
        return self._document_id_2

    def set_document_id_2(self, val):
        self._document_id_2 = val

    def get_document_por(self):
        return self._document_por

    def set_document_por(self, val):
        self._document_por = val

    def get_document_por_2(self):
        return self._document_por_2

    def set_document_por_2(self, val):
        self._document_por_2 = val
