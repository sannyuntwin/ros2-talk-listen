from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import Command, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    pkg = FindPackageShare("diff_drive_robot")
    urdf = PathJoinSubstitution([pkg, "urdf", "robot.urdf.xacro"])

    return LaunchDescription([
        # Robot state publisher
        Node(
            package="robot_state_publisher",
            executable="robot_state_publisher",
            parameters=[{"robot_description": Command(["xacro ", urdf])}],
            output="screen",
        ),
        # Gazebo
        Node(
            package="ros_gz_sim",
            executable="gz_sim",
            arguments=["-r", "empty.sdf"],
            output="screen",
        ),
        # Spawn robot into Gazebo
        Node(
            package="ros_gz_sim",
            executable="create",
            arguments=["-name", "diff_drive_robot", "-topic", "robot_description"],
            output="screen",
        ),
        # Bridge /cmd_vel and /odom
        Node(
            package="ros_gz_bridge",
            executable="parameter_bridge",
            arguments=[
                "/cmd_vel@geometry_msgs/msg/Twist@gz.msgs.Twist",
                "/odom@nav_msgs/msg/Odometry@gz.msgs.Odometry",
            ],
            output="screen",
        ),
    ])
