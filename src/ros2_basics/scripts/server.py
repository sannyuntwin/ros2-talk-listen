#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts


class AddTwoIntsServer(Node):
    def __init__(self):
        super().__init__("add_two_ints_server")
        self.create_service(AddTwoInts, "add_two_ints", self._callback)
        self.get_logger().info("Server ready — waiting for requests")

    def _callback(self, request, response):
        response.sum = request.a + request.b
        self.get_logger().info(f"{request.a} + {request.b} = {response.sum}")
        return response


def main():
    rclpy.init()
    rclpy.spin(AddTwoIntsServer())
    rclpy.shutdown()


if __name__ == "__main__":
    main()
