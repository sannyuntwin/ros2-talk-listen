#!/usr/bin/env python3
"""Drives the robot in a square: forward 2s, turn 2s, repeat 4 times."""
import time
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class DriveSquare(Node):
    def __init__(self):
        super().__init__("drive_square")
        self._pub = self.create_publisher(Twist, "/cmd_vel", 10)

    def publish(self, linear=0.0, angular=0.0):
        msg = Twist()
        msg.linear.x  = linear
        msg.angular.z = angular
        self._pub.publish(msg)

    def stop(self):
        self.publish(0.0, 0.0)


def main():
    rclpy.init()
    node = DriveSquare()

    node.get_logger().info("Driving in a square...")
    time.sleep(1.0)

    for i in range(4):
        node.get_logger().info(f"Side {i+1}: going forward")
        node.publish(linear=0.3)
        time.sleep(2.0)

        node.get_logger().info(f"Side {i+1}: turning")
        node.publish(angular=0.6)
        time.sleep(2.4)

    node.stop()
    node.get_logger().info("Done.")
    rclpy.shutdown()


if __name__ == "__main__":
    main()
