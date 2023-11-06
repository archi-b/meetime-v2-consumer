from objects.base import Base

class Data(object):

    def __init__(self, id, lead_id, owner_id, owner_name, cadence, cadence_id, rd_conversion_date, created_date, deleted_date, begin_date, scheduled_date, end_date, last_activity_date, status, lost_reason, lost_reason_id, lead_origin_channel, lead_origin_source, lead_origin_campaign, conversion):
        self.id = id
        self.lead_id = lead_id
        self.owner_id = owner_id
        self.owner_name = owner_name
        self.cadence = cadence
        self.cadence_id = cadence_id
        self.rd_conversion_date = rd_conversion_date
        self.created_date = created_date
        self.deleted_date = deleted_date
        self.begin_date = begin_date
        self.scheduled_date = scheduled_date
        self.end_date = end_date
        self.last_activity_date = last_activity_date
        self.status = status
        self.lost_reason = lost_reason
        self.lost_reason_id = lost_reason_id
        self.lead_origin_channel = lead_origin_channel
        self.lead_origin_source = lead_origin_source
        self.lead_origin_campaign = lead_origin_campaign
        self.conversion = conversion

class Parameters(object):
    
    @property
    def lead_id(self):
        return self.__lead_id
    
    @lead_id.setter
    def lead_id(self, value):
        self.__lead_id = value

    def __init__(self, lead_id):
        self.lead_id = lead_id

class Prospection(Base):
     
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