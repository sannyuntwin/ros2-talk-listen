#!/usr/bin/env python3
import rclpy
from rclpy.lifecycle import LifecycleNode, TransitionCallbackReturn
from std_msgs.msg import String


class LifecycleTalker(LifecycleNode):
    def __init__(self):
        super().__init__("lifecycle_talker")
        self._pub = None
        self._timer = None

    def on_configure(self, state):
        self.get_logger().info("Configuring...")
        self._pub = self.create_lifecycle_publisher(String, "/chatter", 10)
        return TransitionCallbackReturn.SUCCESS

    def on_activate(self, state):
        self.get_logger().info("Activating...")
        self._timer = self.create_timer(1.0, self._publish)
        return TransitionCallbackReturn.SUCCESS

    def on_deactivate(self, state):
        self.get_logger().info("Deactivating...")
        self._timer.cancel()
        return TransitionCallbackReturn.SUCCESS

    def on_cleanup(self, state):
        self.get_logger().info("Cleaning up...")
        self._pub = None
        self._timer = None
        return TransitionCallbackReturn.SUCCESS

    def _publish(self):
        msg = String()
        msg.data = "Hello from lifecycle node"
        self._pub.publish(msg)
        self.get_logger().info(f"Published: {msg.data}")


def main():
    rclpy.init()
    rclpy.spin(LifecycleTalker())
    rclpy.shutdown()


if __name__ == "__main__":
    main()
