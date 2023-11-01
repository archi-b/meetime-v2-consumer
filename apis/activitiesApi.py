import sys, os
import requests
import json

# Necessario referenciar a pasta pai "(../)" para buscar a api da Meetime (linha 13)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from apis.baseApi import BaseApi
from objects.activity import Activity

class ActivitiesApi(BaseApi):

    @property
    def __api(self):
        return "/prospections/activities"
        
    def buscarActivities_ByLeadId(self, lead_id):
        params = []
        params.append(["lead_id", lead_id])

        self.__result = self.RequestApi(Activity, self.__api, params)
        return self.__result