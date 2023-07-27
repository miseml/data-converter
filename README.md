# data-converter



## Serializers
Converts file with personal details into PersonalData objects and prints it on screen.

Supported formats:
* json(builtin json lib and simplejson)
* yaml

## Formatters
Presents data as text or HTML

## Example usage

Convert yaml file into text

`python main.py test_files/test.yaml yaml text`

Convert json file into html

`python main.py test_files/test.json json html`
