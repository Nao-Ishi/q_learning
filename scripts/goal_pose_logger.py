#!/usr/bin/env python

import rospy
from nav_msgs.msg import Odometry
from aruco_msgs.msg import MarkerArray

global pose_log

def odomCb(mag):
    global pose_log
    pose_log = mag.pose.pose

def idCb(data):
    global pose_log
    log = str(data.markers[0]).split()
    print log[10],log[11], pose_log

def pose_logger():
    rospy.init_node('goal_pose_logger', anonymous=True)

    rospy.Subscriber("odom",Odometry,odomCb)
    rospy.Subscriber("target_id",MarkerArray,idCb)
    rospy.spin()

if __name__ == "__main__":
    pose_logger()