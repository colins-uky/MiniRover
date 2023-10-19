from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    joy_node = Node(
        package="joy",
        executable="joy_node",
        name="joy_node",
    )

















    # Return list of nodes to run
    return LaunchDescription([
        joy_node,
    ])