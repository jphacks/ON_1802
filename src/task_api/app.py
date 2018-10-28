from flask import Flask, request, jsonify, make_response
import json

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config["JSON_SORT_KEYS"] = False

@app.route("/tasks/<user_id>", methods=["POST"])
def get_Tasks(user_id):
    print(request.json)
    return "OK"

@app.route("/tasks/<user_id>", methods=["GET"])
def post_Tasks(user_id):
    return make_response(jsonify({'tasks': none}))

@app.route("/tasks/<user_id>", methods=["DELETE"])
def delete_Tasks(user_id):
    print(request.json)
    return "OK"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
