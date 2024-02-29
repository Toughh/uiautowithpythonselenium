class GetWebTableData:

    @staticmethod
    def get_rows(tbl_name):
        return "//table[@class= '" + tbl_name + "']/tbody/tr"

    @staticmethod
    def get_cols(tbl_name):
        return "//*[@class= '" + tbl_name + "']/tbody/tr/td"

    @staticmethod
    def get_cols_header(tbl_name, col_index, col_data_index):
        return "//*[@class= '" + tbl_name + "']/tbody/tr[" + str(col_index) + "]/th[" + str(col_data_index) + "]"

    @staticmethod
    def get_cols_data(tbl_name, col_index, col_data_index):
        return "//*[@class= '" + tbl_name + "']/tbody/tr[" + str(col_index) + "]/td[" + str(col_data_index) + "]"

    @staticmethod
    def row_size(tbl_name):
        return len(GetWebTableData.get_rows(tbl_name))

    @staticmethod
    def col_size(tbl_name):
        return len(GetWebTableData.get_cols(tbl_name))






