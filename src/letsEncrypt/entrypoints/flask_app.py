from datetime import datetime
from flask import Flask, request
from letsEncrypt.service_layer import services

app = Flask(__name__)

@app.route("/reimport", methods=["POST"])
def request_certificate():
    arn = request.json["arn"]
    domain = request.json["domain"]
    if arn is None or domain is None:
        return "Error", 500
    services.sendLetsEncryptRequest(domain, arn)
    return "OK", 201