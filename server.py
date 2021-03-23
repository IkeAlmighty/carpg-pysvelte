from flask import Flask, request, send_from_directory
from flask_cors import CORS
import importlib
import json

app = Flask(__name__)
CORS(app)

# api path setup:
@app.route('/api/<resource>')
def call_api(resource):
    res = importlib.import_module("api.{}".format(resource)).get(request)
    return json.dumps(res)

# path for main svelte page:
@app.route('/')
def base():
    return send_from_directory('svelte-client/public', 'index.html')

# path for all frontend static files
@app.route('/<path:path>')
def home(path):
    return send_from_directory('svelte-client/public', path)

if __name__ == "__main__":
    app.run()
