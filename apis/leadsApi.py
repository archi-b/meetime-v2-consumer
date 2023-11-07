
from apis.baseApi import BaseApi
from objects.lead import Lead

class LeadsApi(BaseApi):

    @property
    def __api(self):
        return "/leads"
        
    def getLeads_D1(self):
        params = []
        params.append(["limit", self.items_by_request])
        params.append(["start", "0"]) 
        params.append(["lead_created_after", "2023-10-01"]) # TODO: remover
        params.append(["lead_created_before", "2023-11-01"]) # TODO: remover
        params.append(["lead_updated_after", "2023-10-01"]) # TODO: remover
        params.append(["lead_updated_before", "2023-11-01"]) # TODO: remover
        params.append(["show_deleted", self.show_deleted])
        
        self.__result = self.RequestApi(Lead, self.__api, params)
        return self.__result
        
    def getLeads_ById(self, id):
        params = []
        params.append(["id", id])

        self.__result = self.RequestApi(Lead, self.__api, params)
        return self.__result