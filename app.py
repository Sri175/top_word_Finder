from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS  # Import CORS
import requests
from collections import Counter
import re

# Initialize the Flask application
app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/fetch-words', methods=['POST'])
def fetch_words():
    data = request.get_json()
    url = data.get('url')
    top_n = int(data.get('top_n', 10))  # Get the number of top words (default to 10)
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # If the URL is not reachable, raise an error
        
        # Only match alphabetic words
        words = re.findall(r'[a-zA-Z]+', response.text.lower())
        
        # Get the most common words based on the user's input
        most_common = Counter(words).most_common(top_n)
        
        return jsonify(most_common)
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
