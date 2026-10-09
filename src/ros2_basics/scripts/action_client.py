#!/usr/bin/env python3
import sys
import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from ros2_basics.action import Countdown


class CountdownClient(Node):
    def __init__(self):
        super().__init__("countdown_client")
        self._client = ActionClient(self, Countdown, "countdown")

    def send_goal(self, target):
        self._client.wait_for_server()
        goal = Countdown.Goal()
        goal.target = target

        future = self._client.send_goal_async(
            goal, feedback_callback=self._feedback
        )
        rclpy.spin_until_future_complete(self, future)

        result_future = future.result().get_result_async()
        rclpy.spin_until_future_complete(self, result_future)
        self.get_logger().info(f"Result: {result_future.result().result.message}")

    def _feedback(self, feedback):
        self.get_logger().info(f"Feedback: {feedback.feedback.remaining} remaining")


def main():
    rclpy.init()
    node = CountdownClient()
    target = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    node.send_goal(target)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
