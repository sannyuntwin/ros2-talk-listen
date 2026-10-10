#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from tf2_ros.static_transform_broadcaster import StaticTransformBroadcaster
from geometry_msgs.msg import TransformStamped


class StaticTFBroadcaster(Node):
    def __init__(self):
        super().__init__("static_tf_broadcaster")
        broadcaster = StaticTransformBroadcaster(self)

        t = TransformStamped()
        t.header.stamp = self.get_clock().now().to_msg()
        t.header.frame_id = "base_link"
        t.child_frame_id = "camera_link"
        t.transform.translation.x = 0.1   # 10cm in front
        t.transform.translation.z = 0.05  # 5cm up
        t.transform.rotation.w = 1.0      # no rotation

        broadcaster.sendTransform(t)
        self.get_logger().info("Published: base_link → camera_link")

    
def main():
    rclpy.init()
    node = StaticTFBroadcaster()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
