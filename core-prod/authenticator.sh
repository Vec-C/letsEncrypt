#!/bin/bash

#  IN HERE YOU NEED TO CONFIGURE YOUR AWS WORKSPACE, AN AWS PROFILE OR ACCESS ID AND SECRET VALUES

#  EXAMPLE: https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html
#  export AWS_PROFILE=user1

#  BEFORE THE COMANDS BELOW

aws configure set default.region us-east-1
aws sts get-caller-identity
echo $CERTBOT_VALIDATION > lastCert.txt && mv lastCert.txt "$CERTBOT_TOKEN" \
           && aws s3api put-object --bucket $CERTBOT_DOMAIN --key .well-known/acme-challenge/$CERTBOT_TOKEN  --body ./$CERTBOT_TOKEN