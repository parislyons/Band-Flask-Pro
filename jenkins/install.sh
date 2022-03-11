#!/bin/bash
echo "Updating packages"
sudo apt-get update
echo "Installing venv"
sudo apt-get install python3 python3-pip python3-venv -y
echo "Install docker" 
sudo apt-get install curl -y
curl https://get.docker.com | sudo bash
sudo usermod -aG docker jenkins
echo "Install docker compose"
sudo apt-get install curl -y jq
version=$(curl -s https://api.github.com/repos/docker/compose/releases/latest | jq -r '.tag_name')
sudo curl -L "https://github.com/docker/compose/releases/download/${version}/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
echo "Docker login"
docker login -u $DOCKER_HUB_CREDS_USR --password $DOCKER_HUB_CREDS_PSW