import simplejson
from model import PersonalData
class SimpleJSONSerializer:
    def serialize(self, data_json_str):
        data_dict = simplejson.loads(data_json_str)
        if isinstance(data_dict, list):
            return [PersonalData(**entry) for entry in data_dict]
        return PersonalData(**data_dict)
