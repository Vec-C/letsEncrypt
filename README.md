<h1>AWS | CERTBOT</h1>

<h2>Automatic Let's encrypt ACM certificate autosign.</h2>

<h3>Requirements:</h3>

> Create a new public bucket in S3.

> Create a new Lambda function with the code inside de lambda_function.py file.

> Inside the function code replace the ***BUCKET_NAME*** tag with your bucket name.

> Create a new GET method "/reimport" inside a new API Gateway and link the lambda function as a proxy integration backend.

> Create a new Cloudwatch event alarm that triggers when an ACM certificate is close to expiring.

> Launch a new EC2 Linux instance and add the content of the userData file to the userData property of the instance.

> Go to the Lambda function and add the API Gateway and the alarm as triggers.

Add the following environment variables to the lambda:

> INSTANCE: ***i-xxxxx*** (recently launched instance ID).\
> PORT:     5000

<h3>ONCE THE INSTANCE IS RUNNING...</h3>

Create a new ssh connection to the instance.

Configure a new aws profile with the following command (Owner with ACM and EC2 rights):

> sudo aws configure --profile ***PROFILE***.

Go to /letsEncrypt:

> cd /letsEncrypt.

Edit the docker-compose.yml file:

> ***AWS_LOCAL_PROFILE*** for your recently created aws profile name.

> ***WEBHOOK*** for your API Gateway url including the method. (http://xxxx....aws.../reimport).

> ***EMAIL*** for the email that you want to be linked to the certificate.

<h4>Stop your instance and don't be bothered about this again.</h4>


