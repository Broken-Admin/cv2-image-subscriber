import rclpy
from rclpy.node import Node

# from std_msgs.msg import String
import std_msgs.msg
# import sensor messages
import sensor_msgs.msg

import numpy as np
import cv2
from cv_bridge import CvBridge

class ImageSubscriber(Node):
    def __init__(self):
        super().__init__('image_subscriber')

        self.bridge = CvBridge()
        
        self.subscription = self.create_subscription(
            sensor_msgs.msg.Image,
            '/image_raw',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        current_frame = self.bridge.imgmsg_to_cv2(msg)
        cv2.imshow("camera", current_frame)
        cv2.waitKey(1)
        self.get_logger().info('Data recieved from camera stream')


def main(args=None):
    rclpy.init(args=args)

    image_subscriber = ImageSubscriber()

    rclpy.spin(image_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    image_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()