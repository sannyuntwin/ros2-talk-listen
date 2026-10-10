#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
import tf2_ros


class TFListener(Node):
    def __init__(self):
        super().__init__("tf_listener")
        self._buffer = tf2_ros.Buffer()
        self._listener = tf2_ros.TransformListener(self._buffer, self)
        self.create_timer(1.0, self._print_transform)

    def _print_transform(self):
        try:
            t = self._buffer.lookup_transform(
                "odom", "base_link", rclpy.time.Time()
            )
            x = t.transform.translation.x
            y = t.transform.translation.y
            self.get_logger().info(f"Robot position: x={x:.2f}  y={y:.2f}")
        except tf2_ros.LookupException:
            self.get_logger().warn("Transform not available yet...")


def main():
    rclpy.init()
    rclpy.spin(TFListener())
    rclpy.shutdown()


if __name__ == "__main__":
    main()
