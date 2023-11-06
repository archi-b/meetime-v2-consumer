
from apis.baseApi import BaseApi
from objects.activity import Activity

class ActivitiesApi(BaseApi):

    @property
    def __api(self):
        return "/prospections/activities"
        
    def getActivities_ByLeadId(self, lead_id):
        params = []
        params.append(["lead_id", lead_id])

        self.__result = self.RequestApi(Activity, self.__api, params)
        return self.__result
        
    def getActivities_ByProspectionId(self, prospection_id):
        params = []
        params.append(["prospection_id", prospection_id])

        self.__result = self.RequestApi(Activity, self.__api, params)
        return self.__result