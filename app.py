from flask import Flask, request, jsonify
from flask_cors import CORS  # <- Add this import
import openai
import json
import io
import os
app = Flask(__name__)
CORS(app)  # <- Add this to enable CORS for all routes

OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

@app.route('/ask', methods=['POST'])

def ask_gpt():
    data = request.json
    prompt = data['prompt']
    try:
        client = OpenAI(api_key = OPENAI_API_KEY)
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        answer = response.choices[0].message['content']

        return jsonify({'message': answer})

    except Exception as e:
        return jsonify({'message': 'Error occurred. Please try again.'}), 500
