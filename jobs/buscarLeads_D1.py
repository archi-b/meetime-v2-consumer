import sys
import os.path

# Necessario referenciar a pasta pai "(../)" para buscar a api da Meetime (linha 13)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

import json
from apis.leadsApi import LeadsApi
from apis.prospectionsApi import ProspectionsApi

if __name__ == '__main__':
    leadsApi = LeadsApi()
    leads = leadsApi.buscarLeads_D1()

    prospectionsApi = ProspectionsApi()
    for lead in leads:
        prospections = prospectionsApi.buscarProspections_ByLeadId(lead["id"])
        lead["prospections"] = prospections

    # TODO: Salvar registros da base
    
    for lead in leads:
        print(json.dumps(lead, indent=4))