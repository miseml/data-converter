import json
from model import PersonalData
class JSONSerializer:
    def serialize(self, data_json_str):
        data_dict = json.loads(data_json_str)
        if isinstance(data_dict, list):
            return [PersonalData(**entry) for entry in data_dict]

        return PersonalData(**data_dict)
