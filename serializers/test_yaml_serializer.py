from serializers.yaml_serializer import YAMLSerializer
from model import PersonalData
def test_serialization():
    data = PersonalData("Jason", "111 That St.", "123-1234")
    expected_yaml_string = 'address: 111 That St.\nname: Jason\nphone_number: 123-1234\n'
    class_under_test = YAMLSerializer()
    serialized_data = class_under_test.serialize(data)
    assert serialized_data == expected_yaml_string

def test_deserialization():
    yaml_string = 'address: 111 That St.\nname: Jason\nphone_number: 123-1234\n'
    expected_data = PersonalData("Jason", "111 That St.", "123-1234")
    class_under_test = YAMLSerializer()
    deserialized_data = class_under_test.deserialize(yaml_string)
    assert deserialized_data == expected_data

def test_serialization_list():
    data = [PersonalData("Jason", "111 That St.", "123-1234"), PersonalData("John", "303 This St.", "604-3334"), PersonalData("Adam", "1100 Burrard St.", "236-0044")]
    # expected_yaml_string = "- address: '111 That St.'\nname: Jason\nphone_number: '123-1234'\n- address: '303 This St.'\nname: John\nphone_number: '604-3334'\n - address: '1100 Burrard St.'\n name: Adam\n phone_number: '236-0044'"
    expected_yaml_string = '''- address: 111 That St.
  name: Jason
  phone_number: 123-1234
- address: 303 This St.
  name: John
  phone_number: 604-3334
- address: 1100 Burrard St.
  name: Adam
  phone_number: 236-0044
'''
    class_under_test = YAMLSerializer()
    serialized_data = class_under_test.serialize(data)
    assert serialized_data == expected_yaml_string

def test_deserialization_list():
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
    deserialized_data = class_under_test.deserialize(yaml_string)
    assert deserialized_data == expected_data

def test_serialization_deserialization():
    data = PersonalData("Jason", "111 That St.", "123-1234")
    class_under_test = YAMLSerializer()
    serialized_data = class_under_test.serialize(data)
    deserialized_data = class_under_test.deserialize(serialized_data)
    assert deserialized_data == data
