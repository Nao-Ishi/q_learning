#!/usr/bin/env python

import rospy 
import rospkg 
import random
import tf
from gazebo_msgs.msg import ModelState 
from gazebo_msgs.srv import SetModelState

def state_sender():
    rospy.init_node('state_sender')
    r = rospy.Rate(10)
    state_msg = ModelState()
    state_msg.model_name = 'blue_bot'
    state_msg.pose.position.x = 0.0
    state_msg.pose.position.y = 3.0
    state_msg.pose.position.z = 0.5
    state_msg.pose.orientation.x = 0
    state_msg.pose.orientation.y = 0
    state_msg.pose.orientation.z = 0
    state_msg.pose.orientation.w = 0
    state_msg.reference_frame = 'world'
    rospy.wait_for_service('/gazebo/set_model_state')
    try:
        set_state = rospy.ServiceProxy('/gazebo/set_model_state', SetModelState)
        resp = set_state( state_msg )
    except rospy.ServiceException, e:
        print "Service call failed: %s" % e

    while not rospy.is_shutdown():
        pose_x = random.uniform(-2,2)
        pose_y = random.uniform(-2,2)
        while abs(pose_x) + abs(pose_y) > 1.6:
            pose_x = random.uniform(-2,2)
            pose_y = random.uniform(-2,2)
        q = tf.transformations.quaternion_from_euler(0.0, 0.0, random.uniform(-3.14159,3.14159))

        state_msg = ModelState()
        state_msg.model_name = 'red_bot'
        state_msg.pose.position.x = pose_x
        state_msg.pose.position.y = pose_y
        state_msg.pose.position.z = 0.0
        state_msg.pose.orientation.x = q[0]
        state_msg.pose.orientation.y = q[1]
        state_msg.pose.orientation.z = q[2]
        state_msg.pose.orientation.w = q[3]
        state_msg.reference_frame = 'world'
        rospy.wait_for_service('/gazebo/set_model_state')
        try:
            set_state = rospy.ServiceProxy('/gazebo/set_model_state', SetModelState)
            resp = set_state( state_msg )
        except rospy.ServiceException, e:
            print "Service call failed: %s" % e

        r.sleep()

   
    
if __name__ == '__main__':
    try:
        state_sender()
    except rospy.ROSInterruptException:
        pass