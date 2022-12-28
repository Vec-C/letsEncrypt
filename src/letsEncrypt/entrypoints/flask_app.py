import requests
from datetime import datetime
from flask import Flask, request
from letsEncrypt.service_layer import services
from letsEncrypt import config

app = Flask(__name__)

def notify_lambda():
    webhook = config.get_lambda_webhook()
    try:
        requests.get(webhook, timeout=1.0)
    except requests.exceptions.ReadTimeout:
        pass

notify_lambda()

@app.route("/reimport", methods=["POST"])
def request_certificate():
    arn = request.json["arn"]
    domain = request.json["domain"]
    if arn is None or domain is None:
        return "Error", 500
    services.sendLetsEncryptRequest(domain, arn)
    return "OK", 201