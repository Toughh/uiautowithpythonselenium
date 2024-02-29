class PersonalInfo:

    def __init__(self, client_type=None, first_name=None, last_name=None, date_of_birth=None, country_of_residence=None,
                 mobile_number=None, otp=None, expected_deposit=None, expected_client_deposit=None,
                 expected_no_of_client=None, second_applicant_first_name=None, second_applicant_last_name=None,
                 joint_country_of_residence=None, joint_date_of_birth=None, corporate_name=None,
                 legal_entity_identifier=None):

        self.__client_type = client_type
        self.__first_name = first_name
        self.__last_name = last_name
        self.__date_of_birth = date_of_birth
        self.__country_of_residence = country_of_residence
        self.__mobile_number = mobile_number
        self.__otp = otp
        self.__expected_deposit = expected_deposit
        self.__expected_client_deposit = expected_client_deposit
        self.__expected_no_of_client = expected_no_of_client
        self.__second_applicant_first_name = second_applicant_first_name
        self.__second_applicant_last_name = second_applicant_last_name
        self.__joint_country_of_residence = joint_country_of_residence
        self.__joint_date_of_birth = joint_date_of_birth
        self.__corporate_name = corporate_name
        self.__legal_entity_identifier = legal_entity_identifier

    def set_client_type(self, client_type: str):
        self.__client_type = client_type

    def get_client_type(self) -> str:
        return self.__client_type

    def set_first_name(self, first_name: str):
        self.__first_name = first_name

    def get_first_name(self) -> str:
        return self.__first_name

    def set_last_name(self, last_name: str):
        self.__last_name = last_name

    def get_last_name(self):
        return self.__last_name

    def set_country_of_residence(self, country_of_residence):
        self.__country_of_residence = country_of_residence

    def get_country_of_residence(self):
        return self.__country_of_residence

    def set_date_of_birth(self, date_of_birth: str):
        self.__date_of_birth = date_of_birth

    def get_date_of_birth(self) -> str:
        return self.__date_of_birth

    def set_mobile_number(self, mobile_number: str):
        self.__mobile_number = mobile_number

    def get_mobile_number(self) -> str:
        return self.__mobile_number

    def set_send_otp(self, otp: str):
        self.__otp = otp

    def get_send_otp(self) -> str:
        return self.__otp

    def set_expected_deposit(self, expected_deposit):
        self.__expected_deposit = expected_deposit

    def get_expected_deposit(self):
        return self.__expected_deposit

    def set_expected_client_deposit(self, expected_client_deposit: str):
        self.__expected_client_deposit = expected_client_deposit

    def get_expected_client_deposit(self) -> str:
        return self.__expected_client_deposit

    def set_expected_no_of_client(self, expected_no_of_client: str):
        self.__expected_no_of_client = expected_no_of_client

    def get_expected_no_of_client(self) -> str:
        return self.__expected_no_of_client

    def set_second_applicant_first_name(self, second_applicant_first_name: str):
        self.__second_applicant_first_name = second_applicant_first_name

    def get_second_applicant_first_name(self) -> str:
        return self.__second_applicant_first_name

    def set_second_applicant_last_name(self, second_applicant_last_name: str):
        self.__second_applicant_last_name = second_applicant_last_name

    def get_second_applicant_last_name(self) -> str:
        return self.__second_applicant_last_name

    def set_joint_country_of_residence(self, joint_country_of_residence: str):
        self.__joint_country_of_residence = joint_country_of_residence

    def get_joint_country_of_residence(self) -> str:
        return self.__joint_country_of_residence

    def set_joint_date_of_birth(self, joint_date_of_birth: str):
        self.__joint_date_of_birth = joint_date_of_birth

    def get_joint_date_of_birth(self) -> str:
        return self.__joint_date_of_birth

    def set_corporate_name(self, corporate_name: str):
        self.__corporate_name = corporate_name

    def get_corporate_name(self) -> str:
        return self.__corporate_name

    def set_legal_entity_identifier(self, legal_entity_identifier: str):
        self.__legal_entity_identifier = legal_entity_identifier

    def get_legal_entity_identifier(self) -> str:
        return self.__legal_entity_identifier
