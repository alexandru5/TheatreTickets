#!/bin/bash
cd ./client
sudo docker stop client
sudo docker rm client

sudo docker build -t client .
sudo docker create -it --net db_subnet --rm --name client client
sudo docker start client
sudo docker exec -it client python3 client.py
