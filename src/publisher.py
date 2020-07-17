#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from udm_ros_tutorials.msg import udm_custom_message

def talker():
	rospy.init_node('publisher',anonymous=True)
	pub=rospy.Publisher('publish_topic',udm_custom_message,queue_size=10)
	rate=rospy.Rate(10)
	while not rospy.is_shutdown():
		message=udm_custom_message()
		message.header.stamp=rospy.Time.now()

		pub.publish(message)
		rate.sleep()

if __name__=='__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass