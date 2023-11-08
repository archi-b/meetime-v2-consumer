import sys
import os.path

# Necessario referenciar a pasta pai "(../)" para buscar a api da Meetime (linha 13)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

import json
from business.historyLeadsBusiness import HistoryLeadsBusiness

if __name__ == '__main__':
    
    leads_api = HistoryLeadsBusiness().getDailyLeads()
    historyLeads = HistoryLeadsBusiness().convertDailyLeadsToHistory(leads_api)

    print("----before convertion----")
    for lead in leads_api:
        activities = lead["prospections"][0]["activities"]
        del lead["prospections"][0]["activities"]
        print(json.dumps(lead, indent=4, ensure_ascii=False))
        lead["prospections"][0]["activities"] = activities

        print('"activities": [')
        for activity in activities:
            print(json.dumps(activity, indent=4))
        print(']')

    print("----after convertion----")    
    print(json.dumps(historyLeads, indent=4, ensure_ascii=False))