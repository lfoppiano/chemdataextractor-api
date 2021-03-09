import argparse
import json

from bottle import route, request, run
from chemdataextractor import Document


@route('/info')
def info():
    returnText = "ChemDataExtractor service."
    return returnText


# @route('/<filename:path>')
# def server_static(filename):
#     return static_file(filename, root='webapp')


@route('/process', method='POST')
def process():
    text = request.forms.get("text")

    doc = Document.from_string(text.encode('utf-8'))
    # output = {"records": [], "cems": []}
    # for record in doc.records:
    #     output['records'].append(record.serialize())

    # for cem in doc.cems:
    #     output['cems'].append(cem)

    # for abbr in doc.abbreviation_definitions:
    #     output['abbreviations'].append(abbr)

    output = []

    for cem in doc.cems:
        output.append({'start': cem.start, 'end': cem.end, 'label': cem.text})

    return json.dumps(output)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Chemdataextractor API")
    parser.add_argument("--host", help="Hostname to be bound the service", type=str, required=False, default="0.0.0.0")
    parser.add_argument("--port", help="Port to be listening to", type=str, required=False, default="8080")

    args = parser.parse_args()

    host = args.host
    port = args.port

    run(host=host, port=port, debug=True)
