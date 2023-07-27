
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

SERIALIZER_TYPES = ["json", "simplejson", "yaml"]

def configure(binder):
    binder.bind("json", JSONSerializer())
    binder.bind("simplejson", SimpleJSONSerializer())
    binder.bind("yaml", YAMLSerializer())

inject.configure(configure)

def print_supported_filetypes():
    print("Supported filetypes: ")
    print(set([inject.instance(type).get_supported_format() for type in SERIALIZER_TYPES]))

def main():
    parser = argparse.ArgumentParser(description="Serialize data from a file using different serializers and output formats.")
    parser.add_argument("-f", "--filepath", type=str, help="Path to the file.")
    parser.add_argument("-s", "--serializer", choices=SERIALIZER_TYPES, help="Choose the serializer (json, simplejson, or yaml).")
    parser.add_argument("-o", "--outputFormat", choices=["text", "html"], help="Choose the output format (text or html).")
    parser.add_argument("-x", "--supportedFormats", action='store_true', help="Print supported input file types.")

    args = parser.parse_args()

    if args.supportedFormats:
        print_supported_filetypes()
        return

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
