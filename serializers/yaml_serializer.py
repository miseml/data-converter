import yaml
from model import PersonalData
class YAMLSerializer:
    def serialize(self, data):
        if isinstance(data, list):
            return yaml.dump([vars(entry) for entry in data])
        return yaml.dump(data.__dict__)

    def deserialize(self, data_yaml_str):
        data_dict = yaml.safe_load(data_yaml_str)
        if isinstance(data_dict, list):
            return [PersonalData(**entry) for entry in data_dict]
        return PersonalData(**data_dict)
