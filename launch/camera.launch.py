from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
import os
from ament_index_python import get_package_share_directory

def generate_launch_description():

    camera_node = Node(
        package="minibot",
        executable="ball_node",
        name="ball_node",
    )


    ld = LaunchDescription()

    realsense_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory('realsense2_camera'),
                         'launch/rs_launch.py')
        )
    )

    ld.add_action(realsense_launch)













    # Return list of nodes to run
    return LaunchDescription([
        camera_node,
        ld
    ])