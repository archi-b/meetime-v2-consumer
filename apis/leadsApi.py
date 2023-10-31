import sys, os
import requests
import json

# Necessario referenciar a pasta pai "(../)" para buscar a api da Meetime (linha 13)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from apis.baseApi import BaseApi
from objects.lead import Lead

class LeadsApi(BaseApi):
        
    def buscarLeads_D1(self):
        # Init object
        if (hasattr(self, "url") == False):
            self.__result = []
            self.__url = f"{self.host}{self.stage}/leads?limit={self.items_by_request}&" \
                f"start=0&" \
                f"lead_created_after=2023-10-24&" \
                f"lead_created_before=2023-10-25&" \
                f"lead_updated_after=2023-10-24&" \
                f"lead_updated_before=2023-10-25&" \
                f"show_deleted={self.show_deleted}"

        response = requests.request("GET", self.__url, headers=self.headers, data={})

        data = lambda:None
        data.__dict__ = json.loads(response.text)

        if (hasattr(data, "size") is False):
            data.size = 0
        obj = Lead(data.limit, data.start, data.size, data.next, data.data, data.parameters)
        
        self.__result.extend(obj.data)

        # Pagination
        while (obj.next is not None):
            self.__url = f"{self.host}" + data.next
            return self.buscarLeads_D1()

        return self.__result