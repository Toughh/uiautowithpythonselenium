class ComplianceRealUsers:

    def __init__(self, client_risk=None, client_categorization=None, id_exp_date_month=None, id_exp_date_day=None,
                 id_exp_date_year=None, por_exp_date_month=None, por_exp_date_day=None, por_exp_date_year=None,
                 comp_id_status=None, comp_por_status=None, note_comp=None, document_name=None):
        self.__client_risk = client_risk
        self.__client_categorization = client_categorization
        self.__id_exp_date_month = id_exp_date_month
        self.__id_exp_date_day = id_exp_date_day
        self.__id_exp_date_year = id_exp_date_year
        self.__por_exp_date_month = por_exp_date_month
        self.__por_exp_date_day = por_exp_date_day
        self.__por_exp_date_year = por_exp_date_year
        self.__comp_id_status = comp_id_status
        self.__comp_por_status = comp_por_status
        self.__note_comp = note_comp
        self.__document_name = document_name

    def set_client_risk(self, client_risk: str):
        self.__client_risk = client_risk

    def get_client_risk(self) -> str:
        return self.__client_risk

    def set_client_categorization(self, client_categorization: str):
        self.__client_categorization = client_categorization

    def get_client_categorization(self) -> str:
        return self.__client_categorization

    def set_id_exp_date_month(self, id_exp_date_month: str):
        self.__id_exp_date_month = id_exp_date_month

    def get_id_exp_date_month(self) -> str:
        return self.__id_exp_date_month

    def set_id_exp_date_day(self, id_exp_date_day: str):
        self.__id_exp_date_day = id_exp_date_day

    def get_id_exp_date_day(self) -> str:
        return self.__id_exp_date_day

    def set_id_exp_date_year(self, id_exp_date_year: str):
        self.__id_exp_date_year = id_exp_date_year

    def get_id_exp_date_year(self) -> str:
        return self.__id_exp_date_year

    def set_por_exp_date_month(self, por_exp_date_month: str):
        self.__por_exp_date_month = por_exp_date_month

    def get_por_exp_date_month(self) -> str:
        return self.__por_exp_date_month

    def set_por_exp_date_day(self, por_exp_date_day: str):
        self.__por_exp_date_day = por_exp_date_day

    def get_por_exp_date_day(self) -> str:
        return self.__por_exp_date_day

    def set_por_exp_date_year(self, por_exp_date_year: str):
        self.__por_exp_date_year = por_exp_date_year

    def get_por_exp_date_year(self) -> str:
        return self.__por_exp_date_year

    def set_comp_id_status(self, comp_id_status: str):
        self.__comp_id_status = comp_id_status

    def get_comp_id_status(self) -> str:
        return self.__comp_id_status

    def set_comp_por_status(self, comp_por_status: str):
        self.__comp_por_status = comp_por_status

    def get_comp_por_status(self) -> str:
        return self.__comp_por_status

    def set_note_comp(self, note_comp: str):
        self.__note_comp = note_comp

    def get_note_comp(self) -> str:
        return self.__note_comp

    def set_document_name(self, document_name: str):
        self.__document_name = document_name

    def get_document_name(self) -> str:
        return self.__document_name
