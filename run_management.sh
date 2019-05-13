#!/bin/bash
cd ./management
sudo docker stop management
sudo docker rm management

sudo docker build -t management .
sudo docker create -it --net db_subnet --rm --name management management
sudo docker start management
sudo docker exec -it management python3 management.py
