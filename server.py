from flask import Flask
from flask_cors import CORS
import importlib

app = Flask(__name__)
CORS(app)


@app.route('/api/<resource>')
def call_api(resource):
    return importlib.import_module("api.{}".format(resource)).handle()


if __name__ == "__main__":
    app.run()
