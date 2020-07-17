#!/usr/bin/env python


from udm_ros_tutorials.srv import *
import rospy

def handle_req(req):
    c=req.a.data+req.b.data
    rep=udm_serviceResponse()
    rep.c.data=c
    rep.res.data=True
    return rep
def simple_server():
    rospy.init_node('simple_service_server')
    s = rospy.Service('simple_Service', udm_service, handle_req)
    rospy.spin()

if __name__ == "__main__":
    simple_server()