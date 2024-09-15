from flask import Flask, request, jsonify
import time
from utils.db_helper import get_db_connection, update_user_request_count, get_user_request_count
from utils.encoder import encode_query, retrieve_documents, load_encoder
from utils.scraper import start_scraping

app = Flask(__name__)

# Load encoder
encoder = load_encoder()

# Start background thread for scraping news articles
start_scraping()

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'ok', 'message': 'API is active'})

@app.route('/search', methods=['POST'])
def search():
    start_time = time.time()
    
    data = request.json
    query_text = data.get('text', '')
    top_k = data.get('top_k', 5)
    threshold = data.get('threshold', 0.5)
    user_id = data.get('user_id', '')

    if not query_text or not user_id:
        return jsonify({'error': 'Missing query text or user ID'}), 400

    # Track API calls
    request_count = get_user_request_count(user_id)
    if request_count is None:
        return jsonify({'error': 'User not found'}), 400

    if request_count > 5:
        return jsonify({'error': 'Too many requests'}), 429

    update_user_request_count(user_id)

    query_vector = encode_query(query_text, encoder)
    documents = retrieve_documents(query_vector, top_k, threshold)

    # Calculate inference time
    inference_time = time.time() - start_time

    return jsonify({
        'documents': documents,
        'inference_time': inference_time
    })

if __name__ == '__main__':
    app.run(debug=True)
