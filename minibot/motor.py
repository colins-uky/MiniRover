import rclpy
from rclpy.node import Node
import serial
import time
from std_msgs.msg import String

from config_loader import return_config





# Motor Strings:
#
#  M 0000 0000 0000 0000
#
# 'M' followed by four strings of bits.
#
#  First bit is directional bit, 1 = Forward, 0 = Reverse
#
#  Next 3 'bits' are the speed [0, 255], 
#  (notice that they are not binary bits).
#
#  First string is first motor, second is second, etc.
#
#                   (1)-(2)
#                    |   |
#                    |   |
#                   (3)-(4)
#
#  Examples:
#
#  Stop all motors:             M 0000 0000 0000 0000   (only directional bit changed,
#  Stop all motors again:       M 1000 1000 1000 1000     speed still zeros)
#                                                       
#  Forward slowly:              M 1025 1025 1025 1025
#
#
#
#







# Store some common motor strings and encode to bytes
HALT = "M0000000000000000\r\n".encode()





# ROS2 Node to control 4 drive motors
class MotorNode:
    def __init__(self) -> None:
        super.__init__('motor_node')
        
        # Get config from config.yaml
        cfg = return_config()["motor_node"]





        # Initialize serial port over UART pins 
        # (pins 8 & 10 on Nvidia Jetson Nano 40 pin header)
        # Serial port for Jetson UART is /dev/ttyTHS1
        self.serial = serial.Serial(
            port=cfg["serial_port"],
            baudrate=cfg["baud_rate"],
            bytesize=serial.EIGHTBITS,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
        )


        self.subscription = self.create_subscription(
            String,
            '/motor_speeds',
            self.motor_callback,
            10
        )

        self.subscription







    def STOP_ALL_MOTORS(self):
        self.serial.write(HALT)

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