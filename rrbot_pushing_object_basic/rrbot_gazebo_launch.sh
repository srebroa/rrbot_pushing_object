#!/bin/bash

#In a new terminal (Gazebo Simulator)
cd ~/catkin_ws &&
source ./devel/setup.bash &&
roslaunch rrbot_gazebo rrbot_obstacle_world.launch

