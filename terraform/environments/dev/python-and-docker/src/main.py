import os
from flask import Flask, jsonify, request  # type: ignore

# Limites de segurança para entrada do usuário
MAX_MESSAGE_LENGTH = 4096

app = Flask(__name__)


@app.after_request
def security_headers(response):
    """Adiciona headers de segurança à resposta."""
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["Content-Security-Policy"] = "default-src 'self'"
    return response

# Example data (in-memory, for simplicity)
data = {"message": "Hello from Flask API!"}

lista = [{
    "id": 1,
    "name": "Item One"
},
{
    "id": 2,
    "name": "Item Two"
}]


@app.route('/', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy", "message": "API is running"}), 200

def create_new():
    new_item = {
        "id": len(lista) + 1,
        "name": f"Item {len(lista) + 1}"
    }
    lista.append(new_item)
    return jsonify(new_item), 201

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify(data)

@app.route('/api/data', methods=['POST'])
def update_data():
    if not request.is_json:
        return jsonify({"status": "error", "message": "Content-Type must be application/json"}), 400
    new_message = request.json.get('message') if request.json else None
    if new_message is not None:
        if not isinstance(new_message, str):
            return jsonify({"status": "error", "message": "message must be a string"}), 400
        if len(new_message) > MAX_MESSAGE_LENGTH:
            return jsonify({"status": "error", "message": f"message exceeds max length ({MAX_MESSAGE_LENGTH})"}), 400
        data['message'] = new_message
        return jsonify({"status": "success", "message": "Data updated"}), 200
    return jsonify({"status": "error", "message": "No message provided"}), 400


@app.route('/api/items', methods=['GET'])
def get_items():
    return jsonify(lista), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=False)
