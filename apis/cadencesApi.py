
from apis.baseApi import BaseApi
from objects.cadence import Cadence

class CadencesApi(BaseApi):

    @property
    def __api(self):
        return "/cadences"
    
    def getCadences_ById(self, id):
        params = []
        params.append(["id", id])

        self.__result = self.RequestApi(Cadence, self.__api, params)
        return self.__result