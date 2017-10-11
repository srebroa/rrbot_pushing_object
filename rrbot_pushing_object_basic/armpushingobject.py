#!/usr/bin/env python

import rospy
import math

from std_msgs.msg import Float64
from math import sin, cos, atan2, sqrt, fabs

# Define publishers for joint1 and joint2 position controller commands.
joint1publisher = rospy.Publisher('/rrbot/joint1_position_controller/command', Float64, queue_size=10)
joint2publisher = rospy.Publisher('/rrbot/joint2_position_controller/command', Float64, queue_size=10)


# RRArm initial joint positions publisher for joint controllers.
def rrarm_positions_publisher():
    global joint1publisher, joint2publisher
    positioning = True
    joint1initial_position = 1.0
    joint2initial_position = 2.4
    move_step_joint1 = 0.01
    move_step_joint2 = 0.035
    step_upward1 = 0.02
    step_upward2 = 0.04

    joint1current_position = joint1initial_position
    joint2current_position = joint2initial_position

    # Initialization of node for controlling joint1 and joint2 positions.
    rospy.init_node('joint_positions_node', anonymous=True)

    rate = rospy.Rate(80)  # Rate 80 Hz

    while not rospy.is_shutdown() and positioning:
        rrarm_initial_joints_position(joint1initial_position, joint2initial_position)
        rospy.sleep(1)
        joint1current_position, joint2current_position = rrarm_pushing_object(joint1initial_position,
                                                                              joint2initial_position, move_step_joint1,
                                                                              move_step_joint2)
        rospy.sleep(0.2)
        joint1current_position, joint2current_position = rrarm_roll_back(joint1current_position, joint2current_position,
                                                                         step_upward1, step_upward2)
        rospy.sleep(1)
        joint1current_position = rrarm_lift_up(joint1current_position, step_upward1)
        positioning = False
    print "End of positioning!"


def rrarm_initial_joints_position(joint1initial_position, joint2initial_position):
    publish_joints_position(joint1initial_position, joint2initial_position)
    print "%.2f joint1 position:" % (joint1initial_position)
    print "%.2f joint2 position:" % (joint2initial_position)


def rrarm_pushing_object(joint1initial_position, joint2initial_position, move_step_joint1, move_step_joint2):
    for x in range(0, 50):
        joint1_position = joint1initial_position + move_step_joint1 * x
        joint2_position = joint2initial_position - move_step_joint2 * x
        publish_joints_position(joint1_position, joint2_position)
        print "%.2f joint2 position:" % (joint2_position)
        rospy.sleep(0.2)
    return joint1_position, joint2_position


def rrarm_roll_back(joint1_position, joint2_position, step_upward1, step_upward2):
    for x in range(1, 10):
        joint2_position = joint2_position + step_upward2
        joint1_position = joint1_position - step_upward1
        publish_joints_position(joint1_position, joint2_position)
        rospy.sleep(0.2)
        print "%.2f joint1 position:" % (joint1_position)
    return joint1_position, joint2_position


def rrarm_lift_up(joint1_position, step_upward1):
    for x in range(1, 10):
        joint1_position = joint1_position - step_upward1 * x
        publish_joint_position(joint1_position, 1)
        rospy.sleep(0.2)
        print "%.2f joint1 position:" % (joint1_position)
    return joint1_position


def publish_joints_position(joint1_position, joint2_position):
    joint1publisher.publish(joint1_position)
    joint2publisher.publish(joint2_position)


def publish_joint_position(joint_position, joint_number):
    if joint_number == 1:
        joint1publisher.publish(joint_position)
    elif joint_number == 2:
        joint2publisher.publish(joint_position)


# Below code that will continuously run (to stop it press CTRL+C)
if __name__ == '__main__':
    try:
        rrarm_positions_publisher()
    except rospy.ROSInterruptException:
        pass
