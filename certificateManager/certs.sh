#!/bin/bash

helpFunction()
{
   echo ""
   echo "Usage: $0 -a parameterA "
   echo -e "\t-a Domain name that needs revalidation"
   exit 1 # Exit script after printing help
}

while getopts "a:b:c:" opt
do
   case "$opt" in
      a ) export parameterA="$OPTARG" ;;
      b ) parameterB="$OPTARG" ;;
      c ) parameterC="$OPTARG" ;;
      ? ) helpFunction ;; # Print helpFunction in case parameter is non-existent
   esac
done

# Print helpFunction in case parameters are empty
if [ -z "$parameterA" ] || [ -z "$parameterB" ]
then
   echo "Some or all of the parameters are empty";
   helpFunction
fi

echo $parameterA >> logCerts.txt

# Begin script in case all parameters are correct

certbot certonly --key-type rsa --rsa-key-size 2048 --non-interactive --manual --preferred-challenges http --manual-auth-hook "sh /certificateManager/authenticator.sh" --email $parameterC --server https://acme-v02.api.letsencrypt.org/directory --agree-tos -d $parameterA
sh /certificateManager/importCerts.sh -a $parameterB


