#!/bin/bash

eval $(aws ecr get-login --no-include-email --region us-east-1 | sed 's|https://||')
sudo docker build -t docker-app .
sudo docker tag docker-app 492864460344.dkr.ecr.us-east-1.amazonaws.com/docker-app:latest
sudo docker push 492864460344.dkr.ecr.us-east-1.amazonaws.com/docker-app:latest