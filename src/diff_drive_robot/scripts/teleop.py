#!/usr/bin/env python3
"""
Keyboard teleoperation for diff drive robot.
w = forward   s = backward
a = turn left d = turn right
space = stop  q = quit
"""
import sys
import tty
import termios
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

SPEED    = 0.3
TURN     = 0.6

KEYS = {
    'w': ( SPEED,  0.0),
    's': (-SPEED,  0.0),
    'a': ( 0.0,    TURN),
    'd': ( 0.0,   -TURN),
    ' ': ( 0.0,    0.0),
}

def get_key():
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        return sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)


class Teleop(Node):
    def __init__(self):
        super().__init__("teleop")
        self._pub = self.create_publisher(Twist, "/cmd_vel", 10)

    def publish(self, linear, angular):
        msg = Twist()
        msg.linear.x  = linear
        msg.angular.z = angular
        self._pub.publish(msg)


def main():
    rclpy.init()
    node = Teleop()

    print("=== Keyboard Teleop ===")
    print("  w/s = forward/backward")
    print("  a/d = turn left/right")
    print("  space = stop")
    print("  q = quit")

    while True:
        key = get_key()
        if key == 'q':
            node.publish(0.0, 0.0)
            break
        if key in KEYS:
            linear, angular = KEYS[key]
            node.publish(linear, angular)
            node.get_logger().info(f"linear={linear}  angular={angular}")

    rclpy.shutdown()


if __name__ == "__main__":
    main()
