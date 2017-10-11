#!/bin/bash

gnome-terminal -x ./rrbot_gazebo_launch.sh
sleep 5 &&
gnome-terminal -x ./rrbot_ros_control.sh
sleep 2 &&
gnome-terminal -x ./rrbot_pushing_object.sh
sleep 1 &&
gnome-terminal -x ./rrbot_camera_view.sh
 
