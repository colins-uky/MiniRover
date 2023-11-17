from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    # Run joy node
    joy_node = Node(
        package="joy",
        executable="joy_node",
        name="joy_node",
    )

    # Run teleop_twist_joy to convert /joy to /cmd_vel
    # Parameters to change the input buttons/joysticks
    twist_node = Node(
        package="teleop_twist_joy",
        executable="teleop_node",
        name="twist_node",
        parameters=[
            {"axis_linear.x": 4},
            {"axis_angular.yaw": 3}
        ],
        remappings=[('/cmd_vel', '/diff_controller/cmd_vel_unstamped')]
    )















    # Return list of nodes to run
    return LaunchDescription([
        joy_node,
        twist_node,
    ])