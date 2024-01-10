from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
import os
from ament_index_python import get_package_share_directory

#https://roverrobotics.com/blogs/guides/fusing-imu-encoders-with-ros-robot-localization

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
            os.path.join(get_package_share_directory('realsense2_camera'),
                         'launch/rs_launch.py')
        ),
        launch_arguments={
            "enable_gyro":"true",
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