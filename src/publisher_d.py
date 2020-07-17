#!/usr/bin/env python
import rospy
from std_msgs.msg import String


rospy.init_node('publisher',anonymous=True)
pub=rospy.Publisher('publish_topic',String,queue_size=10)
rate=rospy.Rate(10)
while not rospy.is_shutdown():
	message="this message was sent at %s"%rospy.get_time()
	pub.publish(message)
	rate.sleep()
