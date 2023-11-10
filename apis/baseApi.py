import sys
import requests
import json
import datetime as date
import time
from http import HTTPStatus

class BaseApi(object):

    @property
    def headers(self):
        return {
            'Accept': 'application/json',
            'Authorization': self.token
        }
    
    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, value):
        self.__url = value
        
    def __init__(self):
        try:
            self.host = sys.argv[3] # "https://api.meetime.com.br"
            self.stage = sys.argv[4] # "/v2"
            self.token = sys.argv[5] # "<TOKEN_AUTHORIZATION>"
            self.date_format = sys.argv[6] # "%Y-%m-%d"
            self.items_by_request = sys.argv[7] # 100
            self.show_deleted = sys.argv[8] # "false"
            # self.delay_by_request_ms = sys.argv[9] # "200" in miliseconds
            self.SLEEP_HTTP_ERROR_429_SECONDS = 10 # Default: "10" in seconds
        except Exception as err:
            raise SystemExit("Exception: Any those sys.argv[]=[host, stage, token, date_format, items_by_request, show_deleted] is required.")

        try:
            self.show_deleted = sys.argv[8] # "false"
        except Exception as err:
            raise SystemExit("Exception: sys.argv[8]=<show_deleted> is required. Message: " + str(err.args[0]))

        self.dtToday = date.datetime.today().strftime(self.date_format)
        self.dtTodayD1 = (date.datetime.today() - date.timedelta(days=1)).strftime(self.date_format)

    def RequestApi(self, object, api, params, pagination_enabled = True):
        # Init object
        if (hasattr(self, "url") == False):
            self.__result = []
            self.__url = f"{self.host}{self.stage}{api}?"

            for param in params:
                self.__url += f"&{param[0]}={param[1]}"

        response = requests.request("GET", self.__url, headers=self.headers, data={})

        if response.status_code == HTTPStatus.TOO_MANY_REQUESTS:
            time.sleep(self.SLEEP_HTTP_ERROR_429_SECONDS)
            return self.RequestApi(object, api, params)
        if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
            return None

        data = lambda:None
        data.__dict__ = json.loads(response.text)

        if (hasattr(data, "size") is False):
            data.size = 0
        obj = object(data.limit, data.start, data.size, data.next, data.data, data.parameters)
        
        self.__result.extend(obj.data)

        if pagination_enabled == True:
            # Pagination
            while (obj.next is not None):
                self.__url = f"{self.host}" + data.next
                return self.RequestApi(object, api, params)

        return self.__result