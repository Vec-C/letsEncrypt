import os

def get_api_url():
    host = os.environ.get("API_HOST", "localhost")
    port = 5005 if host == "localhost" else 80
    return f"http://{host}:{port}"

def get_aws_profile():
    return os.environ['AWS_PROFILE']

def get_lambda_webhook():
    return os.environ['WEBHOOK']

def get_email():
    return os.environ['EMAIL']