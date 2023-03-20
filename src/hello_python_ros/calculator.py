#!/usr/bin/env python

""" ROS Wrapper for the calculator module
"""


import rospy
from geometry_msgs.msg import Point
from hello_python_ros.msg import CalculatorResult

# Calculator from our pure Python project
from hello import calculator

class CalculatorROS:
    """ROS wrapper for the calculator module"""

    def __init__(self, in_topic: str):

        self.sub = rospy.Subscriber(in_topic, Point, self.callback)
        self.pub = rospy.Publisher('calculator_result', CalculatorResult, queue_size=1)

    def callback(self, data):
        result = CalculatorResult()
        result.sum = calculator.add(data.x, data.y)
        result.difference = calculator.subtract(data.x, data.y)
        result.product = calculator.multiply(data.x, data.y)
        result.quotient = calculator.divide(data.x, data.y)
        self.pub.publish(result)
