from flask import Flask, jsonify

app = Flask(__name__)

data = [
    {"category": "Food", "amount": 120},
    {"category": "Travel", "amount": 300},
    {"category": "Shopping", "amount": 200}
]

@app.route("/api/data", methods=["GET"])
def get_data():
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
