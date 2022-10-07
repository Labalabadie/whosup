#!/usr/bin/env bash
# Programs
sudo apt-get install -y mysql-server=8.0.30
sudo apt-get install -y python=3.8.10
sudo apt-get install -y python3-pip

# Python virtual environment
sudo apt-get install -y python3-venv
sudo python3 -m venv fastapi-mysql 
source fastapi-mysql/bin/activate

# Python libraries to be installed
# inside the venv
pip install httptools==0.1.2 
pip install uvicorn==0.18.3
pip install fastapi[all] 
pip install sqlalchemy 
pip install pymysql==1.0.2 