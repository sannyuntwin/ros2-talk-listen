#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class ParamTalker(Node):
    def __init__(self):
        super().__init__("param_talker")

        self.declare_parameter("rate", 1.0)
        self.declare_parameter("message", "Hello")

        rate = self.get_parameter("rate").value
        self._msg = self.get_parameter("message").value

        self._pub = self.create_publisher(String, "/chatter", 10)
        self.create_timer(1.0 / rate, self._publish)
        self.get_logger().info(f"Publishing '{self._msg}' at {rate} Hz")

    def _publish(self):
        msg = String()
        msg.data = self._msg
        self._pub.publish(msg)
        self.get_logger().info(f"Published: {msg.data}")


def main():
    rclpy.init()
    rclpy.spin(ParamTalker())
    rclpy.shutdown()


if __name__ == "__main__":
    main()
