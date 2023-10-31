import sys, os
import requests
import json

# Necessario referenciar a pasta pai "(../)" para buscar a api da Meetime (linha 13)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from apis.baseApi import BaseApi
from objects.prospection import Prospection

class ProspectionsApi(BaseApi):
        
    def buscarProspections_ByLeadId(self, lead_id):
        # Init object
        if (hasattr(self, "url") == False):
            self.__result = []
            self.__url = f"{self.host}{self.stage}/prospections?lead_id={lead_id}&" \
                f"show_deleted={self.show_deleted}"

        response = requests.request("GET", self.__url, headers=self.headers, data={})

        data = lambda:None
        data.__dict__ = json.loads(response.text)

        if (hasattr(data, "size") is False):
            data.size = 0
        obj = Prospection(data.limit, data.start, data.size, data.next, data.data, data.parameters)
        
        self.__result.extend(obj.data)

        # Pagination
        while (obj.next is not None):
            self.__url = f"{self.host}" + data.next
            return self.buscarProspections_ByLeadId(lead_id)

        return self.__result