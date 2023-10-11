#!/usr/bin/env python

import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import PoseStamped

def callback(data):
    pose_msg = PoseStamped()
    pose_msg.header = data.header
    pose_msg.pose = data.pose.pose

    pub.publish(pose_msg)

rospy.init_node('odom_to_pose_node')
sub = rospy.Subscriber('/rtabmap/odom', Odometry, callback)
pub = rospy.Publisher('/mavros/setpoint_position/local', PoseStamped, queue_size=10)
rospy.spin()

