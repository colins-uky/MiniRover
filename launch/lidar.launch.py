from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
import os
from ament_index_python import get_package_share_directory

from minibot.config_loader import return_config

# This launch file runs the ros2 rplidar_ros rplidar_composition node and publishes its message to
# the /scan topic

# DEBUG
# If having trouble connecting to /dev/ttyUSB0, 
# try >> sudo chmod 666 /dev/ttyUSB

# Command for running rplidar node:
#>> ros2 run rplidar_ros rplidar_composition --ros-args -p serial_port:=/dev/ttyUSB0


serial_port = "/dev/ttyUSB0"

def generate_launch_description():

    cfg = return_config()["lidar_node"]



    rplidar_node = Node(
        package="rplidar_ros",
        executable="rplidar_composition",
        name="lidar_node",
        parameters=[
            {"serial_port": serial_port},
        ]
    )

    




    # Return list of nodes to run
    return LaunchDescription([
        rplidar_node,
    ])