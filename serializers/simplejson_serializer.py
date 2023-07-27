import simplejson
from model import PersonalData
class SimpleJSONSerializer:
    def serialize(self, data):
        if isinstance(data, list):
            return simplejson.dumps([vars(entry) for entry in data])
        return simplejson.dumps(data.__dict__)

    def deserialize(self, data_json_str):
        data_dict = simplejson.loads(data_json_str)
        if isinstance(data_dict, list):
            return [PersonalData(**entry) for entry in data_dict]
        return PersonalData(**data_dict)
