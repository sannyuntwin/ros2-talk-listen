#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
from tf2_ros import TransformBroadcaster
from geometry_msgs.msg import TransformStamped


class OdomTFPublisher(Node):
    def __init__(self):
        super().__init__("odom_tf_pub")
        self._broadcaster = TransformBroadcaster(self)
        self.create_subscription(Odometry, "/odom", self._callback, 10)
        self.get_logger().info("Publishing odom → base_link TF from /odom")

    def _callback(self, msg: Odometry):
        t = TransformStamped()
        t.header.stamp = msg.header.stamp
        t.header.frame_id = "odom"
        t.child_frame_id = "base_link"
        t.transform.translation.x = msg.pose.pose.position.x
        t.transform.translation.y = msg.pose.pose.position.y
        t.transform.translation.z = msg.pose.pose.position.z
        t.transform.rotation = msg.pose.pose.orientation
        self._broadcaster.sendTransform(t)


def main():
    rclpy.init()
    rclpy.spin(OdomTFPublisher())
    rclpy.shutdown()


if __name__ == "__main__":
    main()
