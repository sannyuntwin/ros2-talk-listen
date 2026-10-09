#!/user/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Listener(Node):
    def __init__(self):
        super().__init__('listener')
        self.create_subscription(String, '/chatter', self._callback, 10)
        self.get_logger().info("Listening on /chatter...")
        
    def _callback(self, msg: String):
        self.get_logger().info(f"Received: {msg.data}")
        
def main():
    rclpy.init()
    rclpy.spin(Listener())
    rclpy.shutdown()