#!/usr/bin/env python

from ros_services.srv import Float 
from ros_services.srv import FloatResponse
import rospy
import time

def handle(req):
    print("service call")
    print(req.data)
    rospy.sleep(3)
    res = FloatResponse()
    res.result = 1
    return res

def server():
    rospy.init_node('server')
    s = rospy.Service('float', Float, handle)
    rospy.spin()

if __name__ == "__main__":
    server()
