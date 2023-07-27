from serializers.simplejson_serializer import SimpleJSONSerializer
from model import PersonalData
def test_serialization():
    data = PersonalData("Jason", "111 That St.", "123-1234")
    expected_json_string = '{"name": "Jason", "address": "111 That St.", "phone_number": "123-1234"}'
    class_under_test = SimpleJSONSerializer()
    serialized_data = class_under_test.serialize(data)
    assert serialized_data == expected_json_string

def test_deserialization():
    json_string = '{"name": "Jason", "address": "111 That St.", "phone_number": "123-1234"}'
    expected_data = PersonalData("Jason", "111 That St.", "123-1234")
    class_under_test = SimpleJSONSerializer()
    deserialized_data = class_under_test.deserialize(json_string)
    assert deserialized_data == expected_data

def test_serialization_list():
    data = [PersonalData("Jason", "111 That St.", "123-1234")]
    expected_json_string = '[{"name": "Jason", "address": "111 That St.", "phone_number": "123-1234"}]'
    class_under_test = SimpleJSONSerializer()
    serialized_data = class_under_test.serialize(data)
    assert serialized_data == expected_json_string

def test_deserialization_list():
    json_string = '[{"name": "Jason", "address": "111 That St.", "phone_number": "123-1234"}]'
    expected_data = [PersonalData("Jason", "111 That St.", "123-1234")]
    class_under_test = SimpleJSONSerializer()
    deserialized_data = class_under_test.deserialize(json_string)
    assert deserialized_data == expected_data

def test_serialization_deserialization():
    data = PersonalData("Jason", "111 That St.", "123-1234")
    class_under_test = SimpleJSONSerializer()
    serialized_data = class_under_test.serialize(data)
    deserialized_data = class_under_test.deserialize(serialized_data)
    assert deserialized_data == data
