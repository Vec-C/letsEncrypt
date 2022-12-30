#!/bin/bash
sudo docker system prune -a -f
cd /home/ec2-user/letsEncrypt
make