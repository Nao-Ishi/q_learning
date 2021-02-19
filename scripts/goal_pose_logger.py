#!/usr/bin/env python

import rospy
import tf
from nav_msgs.msg import Odometry
from aruco_msgs.msg import MarkerArray

global pose_log

def odomCb(mag):
    global pose_log
    pose_log_x = str(round(mag.pose.pose.position.x,2))
    pose_log_y = str(round(mag.pose.pose.position.y,2))
    angs = tf.transformations.euler_from_quaternion((mag.pose.pose.orientation.x,mag.pose.pose.orientation.y,mag.pose.pose.orientation.z,mag.pose.pose.orientation.w))
    pose_log = pose_log_x + ',' + pose_log_y + ',' + str(round(angs[2],2))

def idCb(data):
    global pose_log
    log = str(data.markers[0]).split()
    print log[10],log[11],'writed',pose_log
    path = 'data/' + str(log[11]) + '.txt'
    with open(path,mode='a') as f:
        f.write(str(pose_log))
        f.write('\n')



def pose_logger():
    rospy.init_node('goal_pose_logger', anonymous=True)

    rospy.Subscriber("odom",Odometry,odomCb)
    rospy.Subscriber("target_id",MarkerArray,idCb)
    rospy.spin()

if __name__ == "__main__":
    pose_logger()