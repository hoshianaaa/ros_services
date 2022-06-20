#!/usr/bin/env python3

from ros_services.srv import Float 
from ros_services.srv import FloatRequest
import rospy

rospy.init_node('client')

service_name = 'float'
rospy.wait_for_service(service_name)
service = rospy.ServiceProxy(service_name, Float)

r = rospy.Rate(20)

while not rospy.is_shutdown() :
  print("call")
  msg = FloatRequest()
  msg.data = 33.333
  res = service(msg)
  print("response:",res)
  r.sleep()
