from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    joy_node = Node(
        package="joy",
        executable="joy_node",
        name="joy_node",
    )

    twist_node = Node(
        package="teleop_twist_joy",
        executable="teleop_node",
        name="twist_node",
    )















    # Return list of nodes to run
    return LaunchDescription([
        joy_node,
        twist_node,
    ])