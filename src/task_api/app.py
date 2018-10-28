from flask import Flask, request, jsonify, make_response
import json

from manage_data import read
from manage_data import remove
from manage_data import save

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config["JSON_SORT_KEYS"] = False

@app.route("/tasks/<user_id>", methods=["POST"])
def get_Tasks(user_id):
    print(request.json)
    save.data_to_json(request.json)
    return "OK"

@app.route("/tasks/<user_id>", methods=["GET"])
def post_Tasks(user_id):
    return make_response(jsonify({'tasks': read.json_to_data(user_id)}))

@app.route("/tasks/<user_id>", methods=["DELETE"])
def delete_Tasks(user_id):
    remove.task(request.json['user_id'], request.json['task_name'])
    return "OK"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
