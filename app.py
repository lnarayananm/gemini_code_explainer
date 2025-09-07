from flask import Flask, request, jsonify, render_template
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

genai.configure(api_key=GEMINI_API_KEY)

app = Flask(__name__)

@app.route('/')
def home():
    # This will serve the index.html file from the 'templates' folder
    return render_template('index.html')

@app.route('/explain', methods=['POST'])
def explain_code():
    data = request.get_json()
    code = data.get('code', '')
    if not code:
        return jsonify({'error': 'No code provided'}), 400
    try:
        model = genai.GenerativeModel('gemini-2.0-flash')
        prompt = f"Explain the following code in detail:\n{code}"
        response = model.generate_content(prompt)
        explanation = response.text
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    return jsonify({'explanation': explanation})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
