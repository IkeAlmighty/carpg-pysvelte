from flask import Flask
from flask_cors import CORS
import importlib
import json

app = Flask(__name__)
CORS(app)


@app.route('/api/<resource>')
def call_api(resource):
    res = importlib.import_module("api.{}".format(resource)).get()
    return json.dumps(res)


if __name__ == "__main__":
    app.run()
