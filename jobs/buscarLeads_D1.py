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

    for lead in leads:
        print("Aggregated Prospections ByLeadId = ", lead['id'], "...")

        prospections = ProspectionsApi().buscarProspections_ByLeadId(lead["id"])
        lead["prospections"] = prospections
        print("...OK!")

        for prospection in prospections:
            print("Aggregated Cadences by Prospections['cadence_id'] = ", prospection["cadence_id"], "...")
            cadences = CadencesApi().buscarCadences_ById(prospection["cadence_id"])
            prospection["cadences"] = cadences
            print("...OK!")

    # TODO: Salvar registros da base
    
    for lead in leads:
        print(json.dumps(lead, indent=4))