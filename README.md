# rrbot_pushing_object
Simple tasks of pushing a nearby object by the RR robotic arm. This project was implemented in the ROS and Gazebo.
It is based on [gazebo_ros_demos](https://github.com/ros-simulation/gazebo_ros_demos).

<img src="https://github.com/srebroa/rrbot_pushing_object/blob/master/rrbot_pushing_object_basic/screenshots/rrbot_pushing_object.jpg"/>

# How to Launch the simulation?
Make sure you have all the required ROS and Gazebo packages installed, and that this package is in your ROS workspace (`~/catkin_ws`).
If you have not built your workspace do it now (make sure you are inside the workspace root directory):

```sh
$ cd ~/catkin_ws
$ catkin_make
```
Once the `rrbot_pushing_object` package has been built, you can launch the simulation environment using:

```sh
$ cd ~/catkin_ws/src/rrbot_pushing_object/rrbot_pushing_object_basic
$ bash rrbotsimstart.sh
```
The main script `rrbotsimstart.sh` runs four other scripts in separate terminals:
- `rrbot_gazebo_launch.sh`
- `rrbot_ros_control.sh`
- `rrbot_pushing_object.sh`
- `rrbot_camera_view.sh`

The `rrbot_gazebo_launch.sh` start Gazebo with object models listed in the file `rrbot_object.world` : RR robotic arm, stationary objects like table and cardboard_box, camera (`roslaunch rrbot_gazebo rrbot_obstacle_world.launch`). 
To load robotic arm controllers (ROS joint states controllers) we use the script `rrbot_ros_control.sh` that calls the command `roslaunch rrbot_control rrbot_control.launch`.

# Video Demo

See [YouTube](https://www.youtube.com/watch?v=OKOyTQQcrLw) video demo.
