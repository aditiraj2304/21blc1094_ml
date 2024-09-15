from sentence_transformers import SentenceTransformer

def load_encoder():
    return SentenceTransformer('all-MiniLM-L6-v2')

def encode_query(query_text, encoder):
    return encoder.encode([query_text])[0]

def retrieve_documents(query_vector, top_k, threshold):
    # Dummy implementation for retrieval
    # Replace with actual retrieval logic
    return [{"title": "Example Document", "text": "This is an example document.", "similarity": 0.85}]
