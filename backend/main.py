from flask import Flask, request, jsonify
import json
from openai_Translate import processResults

app = Flask(__name__)

@app.route('/process_strings', methods=['POST'])
def process_strings():
    try:
        data = request.get_json()
        if not data or 'string_list' not in data:
            return jsonify({'error': 'Invalid JSON data'}), 400

        string_list = data['string_list']
        if not isinstance(string_list, list):
            return jsonify({'error': 'Input should be a list of strings'}), 400

        # Call the external function with the string_list
        result = processResults(string_list)
        s = str(result)
        # For debug
        print(type(s))
        print(s)
        resultJSON = json.loads(s)

        # Return the result in JSON format
        return jsonify({'result': resultJSON})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0')

