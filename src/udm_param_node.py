#!/usr/bin/env python

import rospy
from std_msgs.msg import Int64

def talker():
	rospy.init_node("udm_param")
	gain = rospy.get_param('~gain', 255)
	pub=rospy.Publisher('gain_param',Int64,queue_size=10)
	rate=rospy.Rate(10)
	while not rospy.is_shutdown():
		pub.publish(gain)
		rate.sleep()


if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass