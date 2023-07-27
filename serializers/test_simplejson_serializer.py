from serializers.simplejson_serializer import SimpleJSONSerializer
from model import PersonalData

def test_serialization():
    json_string = '{"name": "Jason", "address": "111 That St.", "phone_number": "123-1234"}'
    expected_data = PersonalData("Jason", "111 That St.", "123-1234")
    class_under_test = SimpleJSONSerializer()
    serialized_data = class_under_test.serialize(json_string)
    assert serialized_data == expected_data

def test_serialization_list():
    json_string = '[{"name": "Jason", "address": "111 That St.", "phone_number": "123-1234"}]'
    expected_data = [PersonalData("Jason", "111 That St.", "123-1234")]
    class_under_test = SimpleJSONSerializer()
    serialized_data = class_under_test.serialize(json_string)
    assert serialized_data == expected_data

