#!/bin/bash

helpFunction()
{
   echo ""
   echo "Usage: $0 -a parameterB "
   echo -e "\t-a Certificate ARN that needs revalidation"
   exit 1 # Exit script after printing help
}

while getopts "a:" opt
do
   case "$opt" in
      a ) parameterB="$OPTARG" ;;
      ? ) helpFunction ;; # Print helpFunction in case parameter is non-existent
   esac
done

# Print helpFunction in case parameters are empty
if [ -z "$parameterB" ] || [ -z "$parameterA" ]
then
   echo "Some or all of the parameters are empty";
   helpFunction
fi

cd /etc/letsencrypt/
chmod 777 live
cd live
cd $parameterA

aws acm import-certificate --certificate-arn $parameterB --certificate file://cert.pem --private-key file://privkey.pem --certificate-chain file://fullchain.pem