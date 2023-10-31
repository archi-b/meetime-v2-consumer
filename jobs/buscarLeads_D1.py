import sys
import os.path

# Necessario referenciar a pasta pai "(../)" para buscar a api da Meetime (linha 13)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

import json
from apis.leadsApi import LeadsApi
from apis.prospectionsApi import ProspectionsApi
from apis.cadencesApi import CadencesApi

if __name__ == '__main__':
    leadsApi = LeadsApi()

    print("Loading Leads...")
    leads = leadsApi.buscarLeads_D1()
    print("...OK!")

    # Aggregated Prospections by Leads
    prospectionsApi = ProspectionsApi()
    for lead in leads:
        print("Loading Prospections LeadId = ", lead['id'], "...")
        prospections = prospectionsApi.buscarProspections_ByLeadId(lead["id"])
        lead["prospections"] = prospections
        print("...OK!")

        # Aggregated Cadences by Prospections
        cadencesApi = CadencesApi()
        for prospection in prospections:
            print("Loading Cadences... CadenceId = ", prospection["cadence_id"], "...")
            cadences = cadencesApi.buscarCadences_ById(prospection["cadence_id"])
            prospection["cadences"] = cadences
            print("...OK!")

    # TODO: Salvar registros da base
    
    for lead in leads:
        print(json.dumps(lead, indent=4))