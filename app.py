from flask import Flask, request, jsonify
from flask_cors import CORS
from process import speech_process

app = Flask(__name__)
CORS(app)

@app.route('/audio', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        try:
            file = request.files.get('fileInput')
            return jsonify(message=speech_process(file)), 200
        except:
            return jsonify(error="Error from server"), 200