#!/usr/bin/env python3

"""
    Start a random number publisher node

    Author: Olivier Lamarre
    Affl.: STARS Laboratory, University of Toronto
"""

import random

import rospy
from geometry_msgs.msg import Point


def random_2d_point_msg() -> Point:
    """Generate a random Point with x and y fields in the range [1,10]"""
    return Point(
        x=random.randint(1,10)*1.0,
        y=random.randint(1,10)*1.0) # 3rd (z) field is unused


def publish_random_numbers():
    """Publish random numbers every 3 seconds"""
    pub = rospy.Publisher('calculator_input', Point, queue_size=10)
    rospy.init_node('random_number_generator', anonymous=True)
    rate = rospy.Rate(0.5) # 0.5 Hz (or 3 seconds)

    while not rospy.is_shutdown():
        random_point = random_2d_point_msg()
        rospy.loginfo(
            f"Publishing random input: x={random_point.x}, y={random_point.y}")
        pub.publish(random_point)
        rate.sleep()

if __name__ == '__main__':
    try:
        publish_random_numbers()
    except rospy.ROSInterruptException:
        pass