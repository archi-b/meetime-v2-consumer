import requests
import json
import datetime as date
from meetimeApi import MeetimeApi

if __name__ == '__main__':
    meetimeApi = MeetimeApi()
    data = meetimeApi.buscarLead_D1()
    print(json.dumps(obj.__dict__))