#!/bin/bash

eval $(aws ecr get-login --no-include-email --region us-east-1 | sed 's|https://||')
docker build -t docker-app .
docker tag docker-app 492864460344.dkr.ecr.us-east-1.amazonaws.com/docker-app:latest
docker push 492864460344.dkr.ecr.us-east-1.amazonaws.com/docker-app:latest