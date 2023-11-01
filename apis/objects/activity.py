from apis.objects.base import Base

class Data(object):

    def __init__(self, id, name, activity_template_id, call_id, type, status, scope, available_from, goal_date, execution_date, deleted_date, assigned_to_id, executed_by_id, cadence_id, cadence, prospection_id, lead_id, activity_annotation, updated):
        self.id = id
        self.name = name
        self.activity_template_id = activity_template_id
        self.call_id = call_id
        self.type = type
        self.status = status
        self.scope = scope
        self.available_from = available_from
        self.goal_date = goal_date
        self.execution_date = execution_date
        self.deleted_date = deleted_date
        self.assigned_to_id = assigned_to_id
        self.executed_by_id = executed_by_id
        self.cadence_id = cadence_id
        self.cadence = cadence
        self.prospection_id = prospection_id
        self.lead_id = lead_id
        self.activity_annotation = activity_annotation
        self.updated = updated

class Parameters(object):
    
    @property
    def lead_id(self):
        return self.__lead_id
    
    @lead_id.setter
    def lead_id(self, value):
        self.__lead_id = value

    def __init__(self, lead_id):
        self.lead_id = lead_id

class Activity(Base):
     
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