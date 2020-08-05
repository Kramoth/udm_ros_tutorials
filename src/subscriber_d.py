#!/usr/bin/env python
import rospy
from std_msgs.msg import String


def callback(data):
    print(data)

rospy.init_node('subscriber', anonymous=True)
rospy.Subscriber("subscribed_topic", String, callback)
rospy.spin()