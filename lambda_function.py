import json
import boto3
import os
import requests
from botocore.exceptions import ClientError
import tempfile
import time

def speak(code, msg):
    return {
        'statusCode': code,
        'body': msg
    }

def saveEvent(event, bucket_name, file_key, s3):
    for certificate in event["resources"]:
        data = {'domain': event["detail"]["CommonName"],
                'arn': certificate}
        data_json = json.dumps(data)

    temp_file = tempfile.TemporaryFile()

    try:
        temp_file.write(bytes(data_json, encoding='utf-8'))
        temp_file.seek(0)
        s3.upload_fileobj(temp_file, bucket_name, file_key)
    except ClientError as e:
        print(e)
        return speak(500, json.dumps(e))
    finally:
        temp_file.close()

def startInstance(INSTANCE, ec2):
    try:
        certbot = ec2.start_instances(InstanceIds=[INSTANCE], DryRun=False)
    except ClientError as e:
        print(e)
        return speak(500, json.dumps(e))
    else:
        return speak(200, 'Starting Instance...')

def readLastEvent(bucket_name, file_key, s3):
    content_object = s3.get_object(Bucket=bucket_name, Key=file_key)
    file_content = content_object['Body'].read().decode('utf-8')
    json_content = json.loads(file_content)
    return json_content

def lambda_handler(event, context):
    instance = os.environ['INSTANCE']
    port = os.environ['PORT']
    ec2 = boto3.client('ec2')
    s3 = boto3.client('s3')
    bucket_name = '<<BUCKET_NAME>>'
    file_key = 'certificates/last.txt'

    try:
        r = ec2.describe_instance_status(InstanceIds=[instance], IncludeAllInstances=True, DryRun=False)
    except ClientError as e:
        print(e)
        return speak(500, json.dumps(e))

    for status in r['InstanceStatuses']:
        # IF CERTBOT STATUS IS NOT RUNNING(16):
        if status['InstanceState']['Code'] != 16:
            s = saveEvent(event, bucket_name, file_key, s3)
            if s is not None:
                return s
            return startInstance(instance, ec2)

        # CERTBOT SERVICE IS READY:
        else:
            ip = ec2.describe_instances(InstanceIds=[instance], DryRun=False)["Reservations"][0]["Instances"][0]["PrivateIpAddress"]
            json_content = readLastEvent(bucket_name, file_key, s3)
            headers = {'Content-type': 'application/json'}
            renew = requests.post('http://' + ip + ':' + port +'/reimport',
                                     data=json.dumps(json_content), headers=headers)
            time.sleep(15)
            try:
                stopInstance = ec2.stop_instances(InstanceIds=[instance], DryRun=False)
            except ClientError as e:
                print(e)
                return speak(500, json.dumps(e))
            else:
                return speak(200, json.dumps(renew.text))