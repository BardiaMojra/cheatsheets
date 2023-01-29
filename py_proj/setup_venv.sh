# !/bin/bash

ENV="dlo-venv"

sudo apt install python3.10
sudo apt install python3.10-venv
python3 -m venv ${ENV}
source ${ENV}/bin/activate

#python3 -m pip install -r requirements.txt
pip install numpy
pip install matplotlib
pip install pandas
pip install opencv-contrib-python
pip install pyrealsense2
pip install pyglet==1.5.27

sudo chown -R ${USER}:${USER} ${ENV}
