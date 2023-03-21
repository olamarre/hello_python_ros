# hello_python_ros

A simple ROS 1 wrapper example for [hello-python](https://github.com/olamarre/hello-python), a pure Python project isolated in its own conda environment.

Presented as part of the University of Toronto's Robotics Institute Tutorial Series.

## Setup

The following was tested with a standard ROS Noetic full desktop installation on Ubuntu 20.04.

1. Download the [hello-python](https://github.com/olamarre/hello-python) project anywhere on your system, create its conda environment and make sure it is functional on its own.

2. With an active conda environment (in this case, it is called `hello-env`), open a Python terminal and make sure that both ROS-specific `/.../dist-packages` paths are included in sys.path by default, in addition to the conda environment paths:

```pycon
(hello-env) [~]$ python
Python 3.9.16 | packaged by conda-forge | (main, Feb  1 2023, 21:39:03) 
[GCC 11.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import sys
>>> for p in sys.path:
...     print(p)
... 

/home/olamarre/catkin_ws/devel/lib/python3/dist-packages
/opt/ros/noetic/lib/python3/dist-packages
/home/olamarre/miniconda3/envs/hello-env/lib/python39.zip
/home/olamarre/miniconda3/envs/hello-env/lib/python3.9
/home/olamarre/miniconda3/envs/hello-env/lib/python3.9/lib-dynload
/home/olamarre/miniconda3/envs/hello-env/lib/python3.9/site-packages
/home/olamarre/projects/hello-python
>>> 
```

> The ROS related-paths are included because of both `source ...` commands added to the ~/.bashrc file as part of the ROS installation. If you are not using ROS, it is actually recommended to comment those out to avoid unwanted confusion with conda paths.

3. Install the missing system-level dependencies in the conda environment.  
Even though the ROS-specific Python packages can be found from within the conda environment, the (system-level) Python packages that they depend on may not be visible. It is difficult to know what dependencies are missing ahead of time - usually, you need to install whatever ROS/Python complains about at run time.  
For this tutorial, the `pyyaml` and `rospkg` Python packages were missing:  
`conda install -c conda-forge pyyaml rospkg`  
> We could instead create a conda `environment_ros.yml` file in the current repository and install them within the already-existing environment: `conda env update -f environment_ros.yml -n hello-env`

4. Git clone the current ROS package & build it (it doesn't matter whether the conda environment is active or not):

```bash
cd ~/catkin_ws/src && git clone https://github.com/olamarre/hello_python_ros.git
cd .. && catkin build hello_python_ros
```

5. Try it!

    - Start a ROS master in a terminal without the conda environment running:  
    `roscore`

    - Start the random calculator input publisher in another terminal without the conda environment running:  
    `rosrun hello_python_ros random_num_publisher.py`

    - Start the calculator node in another terminal **with** the conda environment active:  
    `rosrun hello_python_ros calculator_demo.py`

    - Echo the calculator node output in another terminal:  
    `rostopic echo /calculator_result`

