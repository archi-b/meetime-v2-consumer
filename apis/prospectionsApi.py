
from apis.baseApi import BaseApi
from objects.prospection import Prospection

class ProspectionsApi(BaseApi):

    @property
    def __api(self):
        return "/prospections"
        
    def getProspections_ById(self, id):
        params = []
        params.append(["id", id])

        self.__result = self.RequestApi(Prospection, self.__api, params)
        return self.__result
        
    def getProspections_ByLeadId(self, lead_id):
        params = []
        params.append(["lead_id", lead_id])

        self.__result = self.RequestApi(Prospection, self.__api, params)
        return self.__result