from flask import Flask, jsonify, request

app = Flask(__name__)

items = [
    {"id": 1, "name": "Item 1", "description": "Primeiro item"},
    {"id": 2, "name": "Item 2", "description": "Segundo item"},
]

@app.route("/")
def home():
    return jsonify({"message": "Bem-vindo a API Flask!"})

@app.route("/api/items")
def get_items():
    return jsonify(items)

@app.route("/api/items", methods=["POST"])
def create_item():
    data = request.get_json()
    item = {
        "id": len(items) + 1,
        "name": data.get("name"),
        "description": data.get("description"),
    }
    items.append(item)
    return jsonify(item), 201

if __name__ == "__main__":
    app.run(debug=True, port=5000)