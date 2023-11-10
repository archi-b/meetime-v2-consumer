import datetime as date
import re
import json

from apis.leadsApi import LeadsApi
from apis.prospectionsApi import ProspectionsApi
from apis.cadencesApi import CadencesApi
from apis.activitiesApi import ActivitiesApi
from objects.lead import Lead
from objects.cadence import Cadence
from objects.prospection import Prospection
from objects.activity import Activity
from entities.historyLeadsEntity import HistoryLeadsEntity

class HistoryLeadsBusiness:

    def getDailyLeads(self):
        leads = LeadsApi().getLeads_D1()
        leads = self.__aggregated_data(leads)
        return leads

    def getLeadsAll(self):
        params = []
        params.append(["lead_created_before", date.datetime.today().strftime("%Y-%m-%d")])
        leads = LeadsApi().getLeads_ByQueryParams(params)
        leads = self.__aggregated_data(leads)
        return leads
    
    def convertDailyLeadsToHistory(self, leads):
        historyLeads = []
        for lead in leads:
            prospection = lead["prospections"][0]
            activities = prospection["activities"]
            cadence = prospection["cadences"][0]
            ignored_activities = self._getActivitiesByfilter(activities, ["status", "IGNORED"])

            historyLead = HistoryLeadsEntity()
            historyLead.id = lead["id"]
            historyLead.primeiro_nome = lead["lead_name"]
            historyLead.nome = lead["lead_name"]
            historyLead.email = lead["lead_email"]
            historyLead.empresa = lead["lead_company"]
            historyLead.cargo = lead["lead_position"]
            historyLead.telefones = lead["phonesString"]
            historyLead.site = lead["lead_site"]
            historyLead.criado_em = lead["lead_created_date"] # TODO: *ver formatacao
            historyLead.estado = lead["lead_state"]
            historyLead.cidade = lead["lead_city"]
            historyLead.twitter = lead["lead_twitter"]
            historyLead.facebook = lead["lead_facebook"]
            historyLead.linkedin = lead["urlLinkedin"]
            historyLead.cadencia = cadence["name"] + (str("|" + cadence["description"]) if cadence["description"] is not None else '')
            historyLead.tipo = cadence["cadence_focus"]
            historyLead.status = prospection["status"]
            historyLead.motivo_perda = prospection["lost_reason"]
            historyLead.vendedor = lead["nomeDoVendedor"]

            # historyLead.recebido_pelo_vendedor_em = lead[""] # TODO: activities.available_from date.datetime.today().strftime(self.date_format)
            historyLead.tempo_resposta_min = None # Ignored
            historyLead.iniciado_em = prospection["begin_date"]
            # historyLead.primeira_atividade = lead[""] # TODO: ???
            # historyLead.atividades = lead[""] # TODO: ???
            # historyLead.ultima_atividade = lead[""] # TODO: ???
            # historyLead.dias_em_prospeccao = lead[""] # TODO: ???
            historyLead.finalizado_em = prospection["end_date"]
            historyLead.origem_campanha = prospection["lead_origin_campaign"]
            historyLead.origem_fonte = prospection["lead_origin_source"]
            historyLead.origem_canal = prospection["lead_origin_channel"]
            historyLead.origem_conversao = prospection["conversion"]

            historyLead.pesquisas = len(self._getActivitiesByfilter(activities, ["type", "SEARCH"]))
            historyLead.social_points = len(self._getActivitiesByfilter(activities, ["type", "SOCIAL_POINTS"]))
            historyLead.emails = len(self._getActivitiesByfilter(activities, ["type", "E_MAIL"]))
            historyLead.ligacoes = len(self._getActivitiesByfilter(activities, ["type", "CALL"]))
            historyLead.atividades_ignoradas = len(ignored_activities)            
            historyLead.pesquisas_ignoradas = len(self._getActivitiesByfilter(ignored_activities, ["type", "SEARCH"]))
            historyLead.social_points_ignoradas = len(self._getActivitiesByfilter(ignored_activities, ["type", "SOCIAL_POINTS"]))
            historyLead.emails_ignorados = len(self._getActivitiesByfilter(ignored_activities, ["type", "E_MAIL"]))
            historyLead.ligacoes_ignoradas = len(self._getActivitiesByfilter(ignored_activities, ["type", "CALL"]))
            
            historyLead.cnpj = lead["cnpj"]
            historyLead.ramo_empresa = lead["ramoEmpresa"]
            historyLead.bu_do_cliente = lead["areaDoCliente"]
            historyLead.faturamento_dolares = lead["faturamentoEmDolares"]
            historyLead.faturamento = lead["faturamento"]
            historyLead.qtd_funcionarios = lead["numeroDeFuncionarios"]
            historyLead.cliente_gavb = lead["eCliente"]
            historyLead.setor_que_atendemos = lead["setorQueAtendemos"]

            historyLeads.append(historyLead.to_dict())
            
        return historyLeads
    
    def _getActivitiesByfilter(self, activities, filter):
        result = [x for x in activities if filter[1] in x[filter[0]]]
        return result
    
    def __aggregated_data(self, leads, enable_reduce_requests = False):

        if leads == None:
            return None
        
        if (enable_reduce_requests == True):
            leads = self.__reduce_requests(leads)
        else:    
            for lead in leads:
                lead["prospections"] = ProspectionsApi().getProspections_ById(lead["current_prospection_id"])
                for prospection in lead["prospections"]:
                    prospection["activities"] =  ActivitiesApi().getActivities_ByProspectionId(prospection["id"])
                    prospection["cadences"] = CadencesApi().getCadences_ById(prospection["cadence_id"])
        return leads
    
    def __reduce_requests(self, leads):
        # TODO: Quando a api /prospection aceitar array de ids.
        #       Pode-se alterar a logica para buscar a lista de prospeccoes em uma única requisicao, para depois
        #       realizar a juncao com seus respectivos Leads, evitando o erro HTTP 429 - Too Many Requests.
        #       
        #       prospections = ProspectionsApi().getProspections_ById(','.join(prospection_ids))
        
        prospection_ids = re.findall(r'"current_prospection_id": "(\d+)"', json.dumps(leads))
        activities =  ActivitiesApi().getActivities_ByProspectionId(','.join(prospection_ids))

        for lead in leads:
            lead["prospections"] = ProspectionsApi().getProspections_ById(lead["current_prospection_id"])
            for prospection in lead["prospections"]:
                prospection["activities"] =  []
                for activity in activities:
                    if activity["prospection_id"] == prospection["id"]:
                        prospection["activities"].append(activity)
        
        cadence_ids = re.findall(r'"cadence_id": "(\d+)"', json.dumps(leads))
        cadence_ids_unique = list(set(cadence_ids))
        cadences =  CadencesApi().getCadences_ById(','.join(cadence_ids_unique))

        for lead in leads:
            for prospection in lead["prospections"]:
                prospection["cadences"] = []
                for cadence in cadences:
                    if prospection["cadence_id"] == cadence["id"]:
                        prospection["cadences"].append(cadence)

        return leads