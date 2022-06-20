cmake_minimum_required(VERSION 3.0.2)
project(ros_services)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  sensor_msgs
  geometry_msgs
  message_generation
)

## Generate services in the 'srv' folder
add_service_files(
  FILES
  Float.srv
)

## Generate added messages and services with any dependencies listed here
generate_messages(
   DEPENDENCIES
   sensor_msgs
   geometry_msgs
)

catkin_package()

include_directories(
 ${catkin_INCLUDE_DIRS}
)

