cmake_minimum_required(VERSION 3.8)
project(diff_drive_robot)

find_package(ament_cmake REQUIRED)

install(DIRECTORY
  urdf
  launch
  DESTINATION share/${PROJECT_NAME}
)

install(PROGRAMS
  scripts/drive.py
  DESTINATION lib/${PROJECT_NAME}
  RENAME drive
)

ament_package()
