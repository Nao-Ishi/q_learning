#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def war_stateCb(data):
    log = str(data.data).split()
    print log

def war_state_listener():
    rospy.init_node("war_state_listener",anonymous=True)
    rospy.Subscriber("war_state",String,war_stateCb)
    rospy.spin()

if __name__ == "__main__":
    war_state_listener()