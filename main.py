
import inject
import argparse

import formatters.html as html
import formatters.text as text

from serializers.json_serializer import JSONSerializer
from serializers.simplejson_serializer import SimpleJSONSerializer
from serializers.yaml_serializer import YAMLSerializer

# This should be injected, it would be easier to extend functionality of a program
DISPLAY_FORMATS = {
    "text": text.text_formatter,
    "html": html.html_formatter,
}

def configure(binder):
    binder.bind("json", JSONSerializer())
    binder.bind("simplejson", SimpleJSONSerializer())
    binder.bind("yaml", YAMLSerializer())

inject.configure(configure)

def main():
    parser = argparse.ArgumentParser(description="Serialize data from a file using different serializers and output formats.")
    parser.add_argument("filepath", type=str, help="Path to the file.")
    parser.add_argument("serializer", choices=["json", "simplejson", "yaml"], help="Choose the serializer (json, simplejson, or yaml).")
    parser.add_argument("outputFormat", choices=["text", "html"], help="Choose the output format (text or html).")

    args = parser.parse_args()

    filepath = args.filepath
    serializer = args.serializer
    output_format = args.outputFormat

    with open(filepath, "r") as file:
        file_content = file.read()
        result = inject.instance(serializer).serialize(file_content)
        display = DISPLAY_FORMATS[output_format]
        display(result)

if __name__ == "__main__":
    main()
