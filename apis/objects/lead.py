from apis.objects.base import Base

class Data(object):

    def __init__(self, id, current_prospection_id, lead_created_date, lead_deleted_date, lead_updated_date, lead_email, lead_name, lead_company, phones, lead_position, lead_site, lead_city, lead_state, lead_twitter, lead_facebook, lead_linkedin, lead_annotations, lead_fit_score, public_url, external_reference, phonesString, primaryPhoneString, workshopsVisualizados, setorQueAtendemos, nomeDoVendedor, desafios, eCliente, numeroDeFuncionarios, faturamento, faturamentoEmDolares, urlLinkedin, areaDoCliente, ramoEmpresa, cnpj, origemCampanha):
        self.id = id
        self.current_prospection_id = current_prospection_id
        self.lead_created_date = lead_created_date
        self.lead_deleted_date = lead_deleted_date
        self.lead_updated_date = lead_updated_date
        self.lead_email = lead_email
        self.lead_name = lead_name
        self.lead_company = lead_company
        self.phones = phones
        self.lead_position = lead_position
        self.lead_site = lead_site
        self.lead_city = lead_city
        self.lead_state = lead_state
        self.lead_twitter = lead_twitter
        self.lead_facebook = lead_facebook
        self.lead_linkedin = lead_linkedin
        self.lead_annotations = lead_annotations
        self.lead_fit_score = lead_fit_score
        self.public_url = public_url
        self.external_reference = external_reference
        self.phonesString = phonesString
        self.primaryPhoneString = primaryPhoneString
        self.workshopsVisualizados = workshopsVisualizados
        self.setorQueAtendemos = setorQueAtendemos
        self.nomeDoVendedor = nomeDoVendedor
        self.desafios = desafios
        self.eCliente = eCliente
        self.numeroDeFuncionarios = numeroDeFuncionarios
        self.faturamento = faturamento
        self.faturamentoEmDolares = faturamentoEmDolares
        self.urlLinkedin = urlLinkedin
        self.areaDoCliente = areaDoCliente
        self.ramoEmpresa = ramoEmpresa
        self.cnpj = cnpj
        self.origemCampanha = origemCampanha

class Parameters(object):
    
    @property
    def limit(self):
        return self.__limit

    @property
    def start(self):
        return self.__start

    @property
    def lead_created_after(self):
        return self.__lead_created_after
    
    @limit.setter
    def limit(self, value):
        self.__limit = value

    @start.setter
    def start(self, value):
        self.__start = value

    @lead_created_after.setter
    def lead_created_after(self, value):
        self.__lead_created_after = value

    def __init__(self, limit, start, lead_created_after):
        self.limit = limit
        self.start = start
        self.lead_created_after = lead_created_after

class Lead(Base):
     
    @property
    def data(self):
        return self.__data
     
    @data.setter
    def data(self, value):
        self.__data = value
     
    def __init__(self, limit, start, size, next, data, parameters):
        super().__init__(limit, start, size, next)
        self.data = data
        self.parameters = parameters