from flask import Flask, request, jsonify
from flask_cors import CORS
import anthropic
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
CORS(app)  # Allow frontend to make requests to backend

# Initialize Anthropic client
client = anthropic.Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY")
)

@app.route('/api/dramatize', methods=['POST'])
def dramatize():
    try:
        # Get the complaint from the request
        data = request.get_json()
        complaint = data.get('complaint', '')
        
        if not complaint:
            return jsonify({'error': 'No complaint provided'}), 400
        
        # Call Anthropic API
        message = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=1000,
            messages=[{
                "role": "user",
                "content": f'Transform this mundane complaint into overly dramatic Shakespearean prose. Make it theatrical, flowery, and absurdly overdramatic. Use thee/thou, metaphors, and tragedy. Keep it to 1-2 sentences: "{complaint}"'
            }]
        )
        
        # Extract the dramatic text
        dramatic_text = message.content[0].text
        
        return jsonify({'dramatic_text': dramatic_text})
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok', 'message': 'Backend is running!'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)