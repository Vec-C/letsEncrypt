from __future__ import annotations
import shlex
import os

rootdir = '/'

def setup_aws_shell(domain, arn, account, step):
    return f'export AWS_PROFILE={account} && sh ' + shlex.quote(rootdir) + f'{account}/{step}.sh -a {domain} -b {arn}'

def sendLetsEncryptRequest(domain, arn, account="core-prod"):
    print(f'Ordering certificate: {domain}')
    os.system(setup_aws_shell(domain, arn, account, 'certs'))


