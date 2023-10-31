from objects.base import Base

class Data(object):

    def __init__(self, id, name, description, created_by_id, created_at, deleted, token, owner_id, executing, type, cadence_focus, priority, api_endpoint):
        self.id = id
        self.name = name
        self.description = description
        self.created_by_id = created_by_id
        self.created_at = created_at
        self.deleted = deleted
        self.token = token
        self.owner_id = owner_id
        self.executing = executing
        self.type = type
        self.cadence_focus = cadence_focus
        self.priority = priority
        self.api_endpoint = api_endpoint

class Parameters(object):
    
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, value):
        self.__id = value

    def __init__(self, id):
        self.id = id

class Cadence(Base):
     
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