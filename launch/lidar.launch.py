from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
import os
from ament_index_python import get_package_share_directory


# This launch file runs the ros2 rplidar_ros rplidar_composition node and publishes its message to
# the /scan topic

# DEBUG
# If having trouble connecting to /dev/ttyUSB0 try >>sudo chmod 666 /dev/ttyUSB

# Command for running rplidar node:
#>> ros2 run rplidar_ros rplidar_composition --ros-args -p serial_port:=/dev/ttyUSB0

def generate_launch_description():

    camera_node = Node(
        package="minibot",
        executable="qr_detector",
        name="qr_detector",
    )

    
    imu_node = Node(
        package="minibot",
        executable="imu_echo",
        name="imu_echo",
    )

    # Launch rs_launch.py from the realsense2_camera package
    #                               (realsense-ros wrapper)
    ld = LaunchDescription()
    realsense_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory('rplidar_ros'),
                         'launch/rs_launch.py')
        ),
        launch_arguments={
            "serial_port":"/dev/ttyUSB0",
            "enable_accel":"true",
            "unite_imu_method":"2",
        }.items()
    )

    ld.add_action(realsense_launch)





    # Return list of nodes to run
    return LaunchDescription([
        ld,
        camera_node,
        imu_node,
    ])