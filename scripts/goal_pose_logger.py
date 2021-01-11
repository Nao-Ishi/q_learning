#!/usr/bin/env python

import rospy
from nav_msgs.msg import Odometry
from aruco_msgs.msg import MarkerArray

def odomCb(mag):
    print mag.pose.pose

def idCb(data):
    log = str(data.markers[0]).split()
    print log[10],log[11]

def pose_logger():
    rospy.init_node('goal_pose_logger', anonymous=True)

    #rospy.Subscriber("odom",Odometry,odomCb)
    rospy.Subscriber("target_id",MarkerArray,idCb)
    rospy.spin()

if __name__ == "__main__":
    pose_logger()