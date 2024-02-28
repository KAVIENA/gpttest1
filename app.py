from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

app = Flask(__name__)
CORS(app)

# Load IPC sections data
ipc_data = pd.read_csv("C:\FYP1\gpttest1\ipc_sections.csv")

# Preprocess IPC sections data
stop_words = set(stopwords.words('english'))

@app.route('/query', methods=['POST'])
def query():
    data = request.get_json()
    query = data['query']
    # Implement your NLU logic here
    # For simplicity, let's just do keyword matching for now
    matches = ipc_data[ipc_data['section_text'].str.contains(query, case=False)]
    response = matches.to_dict('records')
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
