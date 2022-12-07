FROM public.ecr.aws/amazonlinux/amazonlinux:latest

RUN yum -y update
RUN amazon-linux-extras install epel -y
RUN yum -y install python3-pip
COPY requirements.txt /tmp/
RUN pip3 install -r /tmp/requirements.txt
RUN yum -y install augeas unzip
RUN python3 -m pip install certbot certbot-apache
RUN mkdir -p /src
COPY ./src/ /src/
RUN pip3 install -e /src
COPY ./core-prod/ /core-prod/
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
RUN unzip awscliv2.zip
RUN ./aws/install


WORKDIR /src
ENV FLASK_APP=letsEncrypt/entrypoints/flask_app.py FLASK_DEBUG=1 PYTHONBUFFERED=1
CMD flask run --host=0.0.0.0 --port=80