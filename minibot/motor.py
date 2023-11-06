import rclpy
from rclpy.node import Node

from std_msgs.msg import String


# ROS2 Node to control 4 drive motors
class MotorNode:
    def __init__(self) -> None:
        super.__init__('motor_node')
        self.subscription = self.create_subscription(
            String,
            '/motor_speeds',
            self.motor_callback,
            10
        )

        self.subscription


    def motor_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)


def main(args=None):
    rclpy.init(args=args)

    motor_node = MotorNode()

    rclpy.spin(motor_node)



    # Destroy node when finished
    motor_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()