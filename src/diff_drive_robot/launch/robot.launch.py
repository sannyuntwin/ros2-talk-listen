from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch.substitutions import Command, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    pkg = FindPackageShare("diff_drive_robot")
    urdf = PathJoinSubstitution([pkg, "urdf", "robot.urdf.xacro"])

    return LaunchDescription([
        
        # 1 — Robot State Publisher
        # Reads the URDF and broadcasts TF frames (where each link is in 3D space)
        # Other nodes use this to know where the wheels, body etc are
        Node(
            package="robot_state_publisher",
            executable="robot_state_publisher",
            parameters=[{"robot_description": Command(["xacro ", urdf])}],
            output="screen",
        ),
        
        # 2 — Gazebo
        # Opens the Gazebo window with an empty world
        ExecuteProcess(
            cmd=["gz", "sim", "empty.sdf", "-r"],
            output="screen",
        ),
        
        # 3 — Spawn robot into Gazebo
        # Takes robot_description topic (the URDF) and puts the robot into Gazebo
        Node(
            package="ros_gz_sim",
            executable="create",
            arguments=["-name", "diff_drive_robot", "-topic", "robot_description"],
            output="screen",
        ),
        
        # 4 — Bridge 
        # Takes robot_description topic (the URDF) and puts the robot into Gazebo
        # This bridge connects /cmd_vel and /odom between them

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
