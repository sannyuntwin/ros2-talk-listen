#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Talker(Node):
    def __init__(self):
        super().__init__('talker')
        self._pub = self.create_publisher(String, '/chatter', 10)
        self._count = 0
        self.create_timer(1.0, self._publish)

    def _publish(self):
        msg = String()
        msg.data = f'Hello, world! {self._count}'
        self._pub.publish(msg)
        self.get_logger().info(f'Publishing: "{msg.data}"')
        self._count += 1

def main():
    rclpy.init()
    rclpy.spin(Talker())
    rclpy.shutdown()
