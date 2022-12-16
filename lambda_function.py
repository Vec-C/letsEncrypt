import json
import os
import requests


def lambda_handler(event, context):
    CERTBOT = os.environ['CERTBOT']

    for certificate in event["resources"]:
        headers   = {'Content-type': 'application/json'}
        data      = {'domain': event["detail"]["CommonName"],
                     'arn': certificate}
        data_json = json.dumps(data)

        response = requests.post('http://' + CERTBOT + '/reimport',
                                 data=data_json, headers=headers)

        return {
            'statusCode': 200,
            'body': json.dumps(response.text)
        }
