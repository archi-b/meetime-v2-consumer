
from apis.leadsApi import LeadsApi
from apis.prospectionsApi import ProspectionsApi
from apis.cadencesApi import CadencesApi
from apis.activitiesApi import ActivitiesApi
from objects.lead import Lead
from objects.cadence import Cadence
from objects.prospection import Prospection
from objects.activity import Activity
from entities.historyLeadsEntity import HistoryLeadsEntity
from modules.utils import Dotdict

class HistoryLeadsBusiness:

    def getDailyLeads(self):
        leads = LeadsApi().getLeads_ById(11809204)
        for lead in leads:
            lead["prospections"] = ProspectionsApi().getProspections_ById(lead["current_prospection_id"])
            for prospection in lead["prospections"]:
                prospection["activities"] =  ActivitiesApi().getActivities_ByProspectionId(prospection["id"])
                prospection["cadences"] = CadencesApi().getCadences_ById(prospection["cadence_id"])
        return leads

    def convertDailyLeadsToHistory(self, leads):

        historyLeads = []

        for lead in leads:
            historyLead = HistoryLeadsEntity()
            historyLead.id = lead["id"]
            historyLead.primeiro_nome = lead["lead_name"]
            historyLead.nome = lead["lead_name"]
            historyLead.email = lead["lead_email"]
            historyLead.empresa = lead["lead_company"]
            historyLead.cargo = lead["lead_position"]
            historyLead.telefones = lead["phones"]
            historyLead.site = lead["lead_site"]
            historyLead.criado_em = lead["lead_created_date"] # TODO: *ver formatacao
            historyLead.estado = lead["lead_state"]
            historyLead.cidade = lead["lead_city"]
            historyLead.twitter = lead["lead_twitter"]
            historyLead.facebook = lead["lead_facebook"]
            historyLead.linkedin = lead["urlLinkedin"]
            # historyLead.cadencia = lead[""] # TODO: cadence.name|cadence.description
            # historyLead.tipo = lead[""] # TODO: cadence.cadence_focus
            historyLead.status = lead["prospections"][0]["status"]
            historyLead.motivo_perda = lead["prospections"][0]["lost_reason"]
            historyLead.vendedor = lead["nomeDoVendedor"]
            # historyLead.recebido_pelo_vendedor_em = lead[""] # TODO: prospections.activities.available_from
            # historyLead.tempo_resposta_min = lead[""] # TODO: ???
            # historyLead.iniciado_em = lead[""] # TODO: ???
            # historyLead.primeira_atividade = lead[""] # TODO: ???
            # historyLead.atividades = lead[""] # TODO: ???
            # historyLead.ultima_atividade = lead[""] # TODO: ???
            # historyLead.dias_em_prospeccao = lead[""] # TODO: ???
            historyLead.finalizado_em = lead["prospections"][0]["end_date"]
            historyLead.origem_campanha = lead["prospections"][0]["lead_origin_campaign"]
            historyLead.origem_fonte = lead["prospections"][0]["lead_origin_source"]
            historyLead.origem_canal = lead["prospections"][0]["lead_origin_channel"]
            historyLead.origem_conversao = lead["prospections"][0]["conversion"]
            # historyLead.pesquisas = lead[""] # TODO: prospections.activities.count().filter("pesquisas")
            # historyLead.social_points = lead[""] # TODO: prospections.activities.count().filter("social_points")
            # historyLead.emails = lead[""] # TODO: prospections.activities.count().filter("emails")
            # historyLead.ligacoes = lead[""] # TODO: prospections.activities.count().filter("ligacoes")
            # historyLead.atividades_ignoradas = lead[""] # TODO: prospections.activities.count().filter("atividades_ignoradas")
            # historyLead.pesquisas_ignoradas = lead[""] # TODO: prospections.activities.count().filter("pesquisas_ignoradas")
            # historyLead.social_points_ignoradas = lead[""] # TODO: prospections.activities.count().filter("social_points_ignoradas")
            # historyLead.emails_ignorados = lead[""] # TODO: prospections.activities.count().filter("emails_ignorados")
            # historyLead.ligacoes_ignoradas = lead[""] # TODO: prospections.activities.count().filter("ligacoes_ignoradas")
            historyLead.cnpj = lead["cnpj"]
            historyLead.ramo_empresa = lead["ramoEmpresa"]
            historyLead.bu_do_cliente = lead["areaDoCliente"]
            historyLead.faturamento_dolares = lead["faturamentoEmDolares"]
            historyLead.faturamento = lead["faturamento"]
            historyLead.qtd_funcionarios = lead["numeroDeFuncionarios"]
            historyLead.cliente_gavb = lead["eCliente"]
            historyLead.setor_que_atendemos = lead["setorQueAtendemos"]
            
            historyLeads.append(historyLead)
            
        return historyLeads