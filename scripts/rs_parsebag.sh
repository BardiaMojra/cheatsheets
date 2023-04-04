#!/bin/bash

if [ "$EUID" -ne 0 ]
  then echo "Please run as root..."
  exit
fi

# e.g. file tag 't001_'
# -i <ros-bag-file>	ROS-bag filename
# -p <png-path>	convert to PNG, set output path to png-path
# -v <csv-path>	convert to CSV, set output path to csv-path, supported formats: depth, color, imu, pose
# -r <raw-path>	convert to RAW, set output path to raw-path
# -l <ply-path>	convert to PLY, set output path to ply-path
# -b <bin-path>	convert to BIN (depth matrix), set output path to bin-path
# -T	convert to text (frame dump) output to standard out
# -d	convert depth frames only
# -c	convert color frames only

echo ' ' && echo ' ' &&
echo '--->> parsing rs bag file $1 w file tag $2...' && echo ' ' && echo ' '

mkdir png csv raw ply bin
rs-convert -i $1 -p png/$2
rs-convert -i $1 -v csv/$2
rs-convert -i $1 -r raw/$2
rs-convert -i $1 -l ply/$2
rs-convert -i $1 -b bin/$2
