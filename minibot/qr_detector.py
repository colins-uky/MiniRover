#!/usr/bin/env python

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

from std_msgs.msg import Int32MultiArray

class RealSense(Node):

    def __init__(self):
        super().__init__('qr_detector')
        self.subscription = self.create_subscription(
            Image,
            "/camera/color/image_raw",
            self.callback,
            10
        )

        self.subscription


        self.publisher = self.create_publisher(
            Int32MultiArray,
            '/qr_detector',
            10
        )

        self.qr = cv2.QRCodeDetector()


        
    def callback(self, msg):
        bridge = CvBridge()
        cv_image = bridge.imgmsg_to_cv2(msg, "bgr8")


        decoded_info = ""
        points = []
        qr_bin = ""

        try:

            decoded_info, points, qr_bin = self.qr.detectAndDecode(cv_image)
        except:
            print("QR_NODE_ERROR: Unknown error trying to get QR code data.")
        

        cv2.imshow("Camera Image", cv_image)
        cv2.waitKey(1)

        # data = [isQRCodeFound, center_point, radius, distance_to_qrCode]
        data = [1, 45, 90, 550]

        IntArray = Int32MultiArray()
        IntArray.data = data

        self.publisher.publish(IntArray)




def main(args=None):
    rclpy.init(args=args)
    camera_node = RealSense()

    rclpy.spin(camera_node)

    camera_node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()