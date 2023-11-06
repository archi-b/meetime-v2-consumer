import sys
import os.path

# Necessario referenciar a pasta pai "(../)" para buscar a api da Meetime (linha 13)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

import json
from business.historyLeadsBusiness import HistoryLeadsBusiness

if __name__ == '__main__':
    
    dailyLeads = HistoryLeadsBusiness().getDailyLeads()
    historyLeads = HistoryLeadsBusiness().convertDailyLeadsToHistory(dailyLeads)

    for lead in dailyLeads:
        activities = lead["activities"]
        del lead["activities"]
        print(json.dumps(lead, indent=4))
        lead["activities"] = activities

        print('"activities": [')
        for activity in activities:
            print(json.dumps(activity, indent=4))
        print(']')