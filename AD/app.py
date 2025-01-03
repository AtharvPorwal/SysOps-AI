from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/run_command', methods=['POST'])
def run_command():
    # Get the text from the POST request
    command_text = request.json.get('text')

    if not command_text:
        return jsonify({'error': 'No command text provided'}), 400

    try:
        # Run the command as a subprocess
        result = subprocess.run(command_text, shell=True, text=True, capture_output=True)

        if result.returncode != 0:
            # If there's an error, return the stderr
            return jsonify({'error': result.stderr.strip()}), 400

        # Otherwise, return the output of the command
        return jsonify({'output': result.stdout.strip()}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    
@app.route('/save', methods=['POST'])
def save():
    # Get the text from the POST request
    code = request.json.get('text')
    script_path = "TempFile.py"
    with open(script_path, "w", encoding="utf-8") as temp_script:
        temp_script.write(code)
    return script_path

if __name__ == '__main__':
    app.run(debug=True)
