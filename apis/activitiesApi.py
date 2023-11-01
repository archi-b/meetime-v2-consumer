
from apis.baseApi import BaseApi
from apis.objects.activity import Activity

class ActivitiesApi(BaseApi):

    @property
    def __api(self):
        return "/prospections/activities"
        
    def buscarActivities_ByLeadId(self, lead_id):
        params = []
        params.append(["lead_id", lead_id])

        self.__result = self.RequestApi(Activity, self.__api, params)
        return self.__result