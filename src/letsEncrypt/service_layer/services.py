from __future__ import annotations
from letsEncrypt import config
import shlex
import os

rootdir = '/'
aws_profile = config.get_aws_profile()
email       = config.get_email()

def setup_aws_shell(domain, arn, account, step):
    return f'export AWS_PROFILE={account} && sh ' + shlex.quote(rootdir) + f'certificateManager/{step}.sh -a {domain} -b {arn} -c {email}'

def sendLetsEncryptRequest(domain, arn, account=aws_profile):
    print(f'Ordering certificate: {domain}')
    os.system(setup_aws_shell(domain, arn, account, 'certs'))


