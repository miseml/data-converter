# data-converter

## CLI
```
-f OR --filepath Path to the file.
-s OR --serializer Choose the serializer (json, simplejson, or yaml).
-o OR --outputFormat Choose the output format (text or html).
-x OR --supportedFormats Print supported input file types.
```
## Serializers
Converts file with personal details into PersonalData objects and prints it on screen.

Supported formats:
* json(builtin json lib and simplejson)
* yaml

## Formatters
Presents data as text or HTML

## Example usage

Convert yaml file into text

`python main.py --filepath test_files/test.yaml --serializer yaml --outputFormat text`

Convert json file into html

`python main.py --filepath test_files/test.json --serializer json --outputFormat html`

Get supported formats for input files:

`python main.py --supportedFormats`
