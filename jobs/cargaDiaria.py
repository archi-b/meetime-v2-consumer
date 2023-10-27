import sys
import os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

import json
import datetime as date
from meetimeApi import MeetimeApi

if __name__ == '__main__':
    meetimeApi = MeetimeApi()
    data = meetimeApi.buscarLead_D1()

    # TODO: Salvar registros da base
    
    print(json.dumps(data, indent=4))