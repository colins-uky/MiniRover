import rclpy
from rclpy.node import Node
import serial
import time
from std_msgs.msg import String


serial_port = serial.Serial(
    port="/dev/ttyTHS1",
    baudrate=115200,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
)
# Wait a second to let the port initialize
time.sleep(1)

# Send a simple header
serial_port.write("M1050105010501050\r\n".encode())
time.sleep(2)

serial_port.write("M0000000000000000\r\n".encode())

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