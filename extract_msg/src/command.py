#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Point

def callback(data):
    yaw = data.x
    spin = data.y
    roll = data.z
    

def start():

    rospy.init_node('yawspinroll', anonymous=True)

    rospy.Subscriber("ysr_drive", Point , callback)

    rospy.spin()

if __name__ == '__main__':
    start()