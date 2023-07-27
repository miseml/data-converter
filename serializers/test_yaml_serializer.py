from serializers.yaml_serializer import YAMLSerializer
from model import PersonalData

def test_serialization():
    yaml_string = 'address: 111 That St.\nname: Jason\nphone_number: 123-1234\n'
    expected_data = PersonalData("Jason", "111 That St.", "123-1234")
    class_under_test = YAMLSerializer()
    serialized_data = class_under_test.serialize(yaml_string)
    assert serialized_data == expected_data

def test_serialization_list():
    yaml_string = '''- address: 111 That St.
  name: Jason
  phone_number: 123-1234
- address: 303 This St.
  name: John
  phone_number: 604-3334
- address: 1100 Burrard St.
  name: Adam
  phone_number: 236-0044
'''
    expected_data = [PersonalData("Jason", "111 That St.", "123-1234"), PersonalData("John", "303 This St.", "604-3334"), PersonalData("Adam", "1100 Burrard St.", "236-0044")]
    class_under_test = YAMLSerializer()
    serialized_data = class_under_test.serialize(yaml_string)
    assert serialized_data == expected_data
