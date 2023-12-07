# letsEncrypt
AWS | CERTBOT

Automatic Let's encrypt ACM certificate autosign.

Requirements:

Create a new public bucket in S3.

Create a new Lambda function with the code inside de lambda_function.py file.

Inside the function code replace ***BUCKET*** with your bucket name.

Create a new GET method "/reimport" inside a new API Gateway and link the lambda function as a proxy integration backend.

Create a new Cloudwatch event alarm that triggers when an ACM certificate is close to expiring.

Launch a new EC2 Linux instance and add the content of the userData file to the userData property of the instance.

Go to the Lambda function and add the API Gateway and the alarm as triggers.

Add the following environment variables to the lambda:

INSTANCE: ***i-xxxxx*** (recently launched instance ID).
PORT:     5000

ONCE THE INSTANCE IS RUNNING...

Create a new ssh connection to the instance.

Configure a new aws profile with the following command:

  sudo aws configure --profile ***PROFILE***.

Go to /home/ec2-user/letsEncrypt:

  cd /home/ec2-user/letsEncrypt.

Edit the docker-compose.yml file:

***AWS_LOCAL_PROFILE*** for your recently created aws profile name.

***WEBHOOK*** for your API Gateway url including the method. (http://xxxx....aws.../reimport).

***EMAIL*** for the email linked to the certificate.


