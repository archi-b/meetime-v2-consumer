import sys, os
import requests
import json

# Necessario referenciar a pasta pai "(../)" para buscar a api da Meetime (linha 13)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from apis.baseApi import BaseApi
from objects.cadence import Cadence

class CadencesApi(BaseApi):

    @property
    def __api(self):
        return "/cadences"
    
    def buscarCadences_ById(self, id):
        params = []
        params.append(["id", id])

        self.__result = self.RequestApi(Cadence, self.__api, params)
        return self.__result