#!/usr/bin/env python3
import time
import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer
from ros2_basics.action import Countdown


class CountdownServer(Node):
    def __init__(self):
        super().__init__("countdown_server")
        ActionServer(self, Countdown, "countdown", self._execute)
        self.get_logger().info("Action server ready")

    def _execute(self, goal_handle):
        target = goal_handle.request.target
        feedback = Countdown.Feedback()

        for i in range(target, 0, -1):
            feedback.remaining = i
            goal_handle.publish_feedback(feedback)
            self.get_logger().info(f"Counting: {i}")
            time.sleep(1.0)

        goal_handle.succeed()
        result = Countdown.Result()
        result.message = "done"
        return result


def main():
    rclpy.init()
    rclpy.spin(CountdownServer())
    rclpy.shutdown()


if __name__ == "__main__":
    main()
