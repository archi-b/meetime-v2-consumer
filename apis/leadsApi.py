
from apis.baseApi import BaseApi
from apis.objects.lead import Lead

class LeadsApi(BaseApi):

    @property
    def __api(self):
        return "/leads"
        
    def buscarLeads_D1(self):
        params = []
        params.append(["limit", self.items_by_request])
        params.append(["start", "0"]) 
        params.append(["lead_created_after", self.dtTodayD1])
        params.append(["lead_created_before", self.dtToday])
        params.append(["lead_updated_after", self.dtTodayD1])
        params.append(["lead_updated_before", self.dtToday])
        params.append(["show_deleted", self.show_deleted])
        
        self.__result = self.RequestApi(Lead, self.__api, params)
        return self.__result
        
    def buscarLeads_ById(self, id):
        params = []
        params.append(["id", id])

        self.__result = self.RequestApi(Lead, self.__api, params)
        return self.__result