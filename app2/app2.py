import logging

import requests
from flask import Flask

import node_trace_client

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

app = Flask(__name__)

url_format: str = "http://{app_name}:5000"


@app.route("/")
def hello_world():
    logger.info("app2 receives request.")

    send_request_to_app(app_name="app3")
    return "App 2 returning"


def send_request_to_app(app_name: str) -> requests.Response:
    r = requests.get(url_format.format(app_name=app_name))
    logger.info("Response from %s: %s", app_name, r)
    return r


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
