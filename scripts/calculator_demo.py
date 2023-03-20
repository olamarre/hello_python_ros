#!/usr/bin/env python

import rospy
from hello_python_ros.calculator import CalculatorROS

def main():

    rospy.init_node('calculator', anonymous=True)
    CalculatorROS(in_topic='calculator_input')
    rospy.spin()

if __name__ == '__main__':
    main()