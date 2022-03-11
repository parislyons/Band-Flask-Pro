#!/bin/bash

echo "Deploy stage"
scp docker-compose.yaml jenkins@BFPDocker:/home/jenkins/docker-compose.yaml
ssh jenkins@BFPDocker \
    DOCKER_HUB_CREDS_USR=$DOCKER_HUB_CREDS_USR \
    MY_SQL_ROOT_PASSWORD=$MY_SQL_ROOT_PASSWORD \
    docker stack deploy --compose-file docker-compose.yaml band-flask-pro
