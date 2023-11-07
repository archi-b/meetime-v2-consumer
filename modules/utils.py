import json

def Dotdict(dict):
    """dot.notation access to dictionary attributes"""
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__
    
def toJSON(obj):
    return json.dumps(obj, default=lambda o: o.__dict__, 
        sort_keys=True, indent=4)