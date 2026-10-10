cmake_minimum_required(VERSION 3.8)
project(diff_drive_robot)

find_package(ament_cmake REQUIRED)

install(PROGRAMS
  scripts/drive.py
  DESTINATION lib/${PROJECT_NAME}
  RENAME drive
)

install(PROGRAMS
  scripts/teleop.py
  DESTINATION lib/${PROJECT_NAME}
  RENAME teleop
)

install(PROGRAMS
  scripts/tf_listener.py
  DESTINATION lib/${PROJECT_NAME}
  RENAME tf_listener
)

install(PROGRAMS
  scripts/static_tf.py
  DESTINATION lib/${PROJECT_NAME}
  RENAME static_tf
)

install(PROGRAMS
  scripts/odom_tf_pub.py
  DESTINATION lib/${PROJECT_NAME}
  RENAME odom_tf_pub
)

install(DIRECTORY
  urdf
  launch
  rviz
  DESTINATION share/${PROJECT_NAME}
)


ament_package()
