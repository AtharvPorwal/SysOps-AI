from CodeAgentZeroShot import RunAgent
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route('/Chat', methods=['POST'])
def reverse_string():
    # Get the data from the POST request
    data = request.json
    print(data)
    
    if not data or 'text' not in data:
        return jsonify({"error": "Please provide a 'text' field in JSON format"}), 400
    
    # Extract the text
    original_text = data['text']
    
    # Reverse the string but not really
    try:
        reversed_text = RunAgent(original_text)
    except Exception as e:
        reversed_text = "Task Done"
    
    # Return the reversed string
    return jsonify({"original": original_text, "OutputData": reversed_text}), 200 ##HAD tested this

if __name__ == '__main__':
    app.run(debug=True)

