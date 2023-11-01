
from apis.leadsApi import LeadsApi
from apis.prospectionsApi import ProspectionsApi
from apis.cadencesApi import CadencesApi
from apis.activitiesApi import ActivitiesApi
#from entities.historyLeadsEntity import HistoryLeadsEntity

class HistoryLeadsBusiness:

    def buscarLeadsDiario(self):
        leads = LeadsApi().buscarLeads_D1()
        for lead in leads:
            lead["prospections"] = ProspectionsApi().buscarProspections_ByLeadId(lead["id"])
            lead["activities"] =  ActivitiesApi().buscarActivities_ByLeadId(lead["id"])    
            for prospection in lead["prospections"]:
                prospection["cadences"] = CadencesApi().buscarCadences_ById(prospection["cadence_id"])
        return leads

    #def convertLeadsDiarioToHistory(self, leads):
        



        




