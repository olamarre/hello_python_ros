#!/usr/bin/env python3

## ! DO NOT MANUALLY INVOKE THIS setup.py, USE CATKIN INSTEAD
## More info: http://docs.ros.org/en/jade/api/catkin/html/user_guide/setup_dot_py.html

from distutils.core import setup

setup(
    version='0.0.1',
    packages=['hello_python_ros'],
    package_dir={'': 'src'},
    description='Simple ROS wrapper for a pure Python project using conda',
    author='Olivier Lamarre',
    url='https://github.com/olamarre/hello_python_ros.git',
)
