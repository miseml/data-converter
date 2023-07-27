import yaml
from model import PersonalData
class YAMLSerializer:
    def serialize(self, data_yaml_str):
        data_dict = yaml.safe_load(data_yaml_str)
        if isinstance(data_dict, list):
            return [PersonalData(**entry) for entry in data_dict]
        return PersonalData(**data_dict)

    def get_supported_format(self):
        return "yaml"
