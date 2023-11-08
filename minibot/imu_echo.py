#!/usr/bin/env python

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu
from cv_bridge import CvBridge
import cv2

from std_msgs.msg import Float32MultiArray

class IMU(Node):

    def __init__(self):
        super().__init__('imu_echo')
        self.subscription = self.create_subscription(
            Imu,
            "/camera/gyro/sample",
            self.callback,
            10
        )

        self.subscription

        self.publisher = self.create_publisher(
                Float32MultiArray,
                '/imu_echo',
                10
            )
            


        
    def callback(self, msg):
        data = [
                msg.linear_acceleration.x, 
                msg.linear_acceleration.y, 
                msg.linear_acceleration.z,
                msg.angular_velocity.x,
                msg.angular_velocity.y,
                msg.angular_velocity.z, 
            ]
        
        imu_data = Float32MultiArray()

        imu_data.data = data

        self.publisher.publish(imu_data)


    def print_msg(self, msg):
        print('IMU Data:')
        print('Linear Acceleration:')
        print(f'x: {msg.linear_acceleration.x}')
        print(f'y: {msg.linear_acceleration.y}')
        print(f'z: {msg.linear_acceleration.z}')
        print('Angular Velocity:')
        print(f'x: {msg.angular_velocity.x}')
        print(f'y: {msg.angular_velocity.y}')
        print(f'z: {msg.angular_velocity.z}')


def main(args=None):
    rclpy.init(args=args)
    imu = IMU()

    rclpy.spin(imu)

    imu.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()