#!/bin/bash

# if [ "$EUID" -ne 0 ]
#   then echo "Please run as root..."
#   exit
# fi

# function pause(){
#   echo ' ' && echo ' '
#   read -s -n 1 -p "press any key to continue..."
#   echo ' ' && echo ' '
# }

: '
  usage: ./rs_parsebag.sh [bag file] [file tag]
  e.g.: ./rs_parsebag.sh 20230403_102634.bag t001
  file tag: e.g. 't001'
  -i <ros-bag-file>	ROS-bag filename
  -p <png-path>	convert to PNG, set output path to png-path
  -v <csv-path>	convert to CSV, set output path to csv-path, supported formats: depth, color, imu, pose
  -r <raw-path>	convert to RAW, set output path to raw-path
  -l <ply-path>	convert to PLY, set output path to ply-path
  -b <bin-path>	convert to BIN (depth matrix), set output path to bin-path
  -T	convert to text (frame dump) output to standard out
  -d	convert depth frames only
  -c	convert color frames only
'

echo ' ' && echo ' ' &&
echo "--->> parsing rs bag file $1 w file tag $2..." && echo ' ' && echo ' '

# mkdir png csv raw ply bin
mkdir png raw ply

echo ' ' && echo ' ' &&
echo '--->> parse png images...' && echo ' ' && echo ' '
rs-convert -i $1 -p png/${2}_

# rs-convert -i $1 -v csv/${2}_ # seg faults


echo ' ' && echo ' ' &&
echo '--->> parse raw data...' && echo ' ' && echo ' '
rs-convert -i $1 -r raw/${2}_


echo ' ' && echo ' ' &&
echo '--->> parse ply point cloud...' && echo ' ' && echo ' '
rs-convert -i $1 -l ply/${2}_

# echo ' ' && echo ' ' &&
# echo '--->> parse ply binary...' && echo ' ' && echo ' '
# rs-convert -i $1 -b bin/${2}_
