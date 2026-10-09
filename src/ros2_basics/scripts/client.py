#!/usr/bin/env python3
import sys
import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts


class AddTwoIntsClient(Node):
    def __init__(self):
        super().__init__("add_two_ints_client")
        self._client = self.create_client(AddTwoInts, "add_two_ints")
        while not self._client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("Waiting for server...")

    def send(self, a, b):
        req = AddTwoInts.Request()
        req.a = a
        req.b = b
        future = self._client.call_async(req)
        rclpy.spin_until_future_complete(self, future)
        return future.result().sum


def main():
    rclpy.init()
    node = AddTwoIntsClient()
    a = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    b = int(sys.argv[2]) if len(sys.argv) > 2 else 5
    result = node.send(a, b)
    node.get_logger().info(f"Result: {a} + {b} = {result}")
    rclpy.shutdown()


if __name__ == "__main__":
    main()
