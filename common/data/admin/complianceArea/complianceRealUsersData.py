import os.path

from common.commonFunctions import CommonFunctions
from common.pojo.admin.complianceRealUsers import ComplianceRealUsers
from common.enum.admin.complianceArea.complianceRealUsers.clientCategorizationType import ClientCategorizationType
from common.enum.admin.complianceArea.complianceRealUsers.clientRiskType import ClientRiskType


class ComplianceRealUsersData:

    # @staticmethod
    # def upload_user_docs():
    #     filename = 'files/fakePassport.jpg'
    #     filepath = os.path.abspath(filename)
    #     print(filepath)
    #     return CommonFunctions.upload_files(filepath)

    @staticmethod
    def compliance_real_users(comp_id_status, comp_por_status):
        return ComplianceRealUsers(ClientRiskType.medium.value, ClientCategorizationType.professional.value, "Mar", "8",
                                   "2030", "Mar", "8", "2028", comp_id_status, comp_por_status, "Approved By Admin",
                                   "Incorrect Passport Doc")
