#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from udm_ros_tutorials.msg import udm_custom_message

def callback(data):
    print(data)
    
def listener():
    rospy.init_node('subscriber', anonymous=True)
    rospy.Subscriber("subscribed_topic", udm_custom_message, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()