import sys
import os.path

# Necessario referenciar a pasta pai "(../)" para buscar a api da Meetime (linha 13)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

import json
from apis.leadsApi import LeadsApi
from apis.prospectionsApi import ProspectionsApi
from apis.cadencesApi import CadencesApi
from apis.activitiesApi import ActivitiesApi

if __name__ == '__main__':
    
    print("Loading Leads...")
    leads = LeadsApi().buscarLeads_ById(3105692) # (3105692)Prospection.status = "LOST", (11809204)Prospection.status = "WON"
    print("...OK!")

    for lead in leads:
        print("Aggregated Prospections ByLeadId = ", lead['id'], "...")

        prospections = ProspectionsApi().buscarProspections_ByLeadId(lead["id"])
        lead["prospections"] = prospections
        print("...OK!")

        print("Loading Prospections ByLeadId = ", lead['id'], "...")
        activities =  ActivitiesApi().buscarActivities_ByLeadId(lead["id"])    
        lead["activities"] = activities
        print("...OK!")

        # Aggregated Cadences by Prospections["cadence_id"]
        for prospection in prospections:
            print("Aggregated Cadences by Prospections['cadence_id'] = ", prospection["cadence_id"], "...")
            cadences = CadencesApi().buscarCadences_ById(prospection["cadence_id"])
            prospection["cadences"] = cadences
            print("...OK!")

    # TODO: Salvar registros da base
    
    for lead in leads:
        activities = lead["activities"]
        del lead["activities"]
        print(json.dumps(lead, indent=4))
        lead["activities"] = activities

        print('"activities": [')
        for activity in activities:
            print(json.dumps(activity, indent=4))
        print(']')