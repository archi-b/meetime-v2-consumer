import sys
import requests
import json
import datetime as date

from objects.lead import Lead

try:
    HOST = sys.argv[1] # "https://api.meetime.com.br"
except Exception as err:
    raise SystemExit("Exception: sys.argv[1]=<host> is required. Message: " + str(err.args[0]))

try:
    STAGE = sys.argv[2] # "/v2"
except Exception as err:
    raise SystemExit("Exception: sys.argv[2]=<stage> is required. Message: " + str(err.args[0]))

try:
    TOKEN = sys.argv[3] # "<TOKEN_AUTHORIZATION>"
except Exception as err:
    raise SystemExit("Exception: sys.argv[3]=<token> is required. Message: " + str(err.args[0]))

try:
    DATE_FORMAT = sys.argv[4] # "%Y-%m-%d"
except Exception as err:
    raise SystemExit("Exception: sys.argv[4]=<date_format> is required. Message: " + str(err.args[0]))

try:
    ITEMS_BY_REQUEST = sys.argv[5] # 100
except Exception as err:
    raise SystemExit("Exception: sys.argv[5]=<items_by_request> is required. Message: " + str(err.args[0]))

try:
    SHOW_DELETED = sys.argv[6] # "false"
except Exception as err:
    raise SystemExit("Exception: sys.argv[6]=<show_deleted> is required. Message: " + str(err.args[0]))

class MeetimeApi(object):

    @property
    def headers(self):
        return {
            'Accept': 'application/json',
            'Authorization': TOKEN
        }
    
    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, value):
        self.__url = value
        
    def __init__(self):
        self.dtToday = date.datetime.today().strftime(DATE_FORMAT)
        self.dtTodayD1 = (date.datetime.today() - date.timedelta(days=1)).strftime(DATE_FORMAT)
        self.__setUrl(0)

    def __setUrl(self, start=0):
        self.url = f"{HOST}{STAGE}/leads?limit={ITEMS_BY_REQUEST}&" \
            f"start={start}&" \
            f"lead_created_after={self.dtTodayD1}&" \
            f"lead_created_before={self.dtToday}&" \
            f"lead_updated_after={self.dtTodayD1}&" \
            f"lead_updated_before={self.dtToday}&" \
            f"show_deleted={SHOW_DELETED}"

    def buscarLead_D1(self):
        arrayLeads = []
        start = 0
        response = requests.request("GET", self.url, headers=self.headers, data={})
        lead_json = json.loads(response.text)
        leads = Lead(**lead_json)
        arrayLeads = leads.data

        # TODO: realizar paginacao aqui para obter todos os leads
        # arrayLeads.extend(leads.data)
        
        return arrayLeads