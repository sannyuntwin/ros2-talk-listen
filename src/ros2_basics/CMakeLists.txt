cmake_minimum_required(VERSION 3.8)
project(ros2_basics)

find_package(ament_cmake REQUIRED)


install(PROGRAMS
    scripts/talker.py
    DESTINATION lib/${PROJECT_NAME}
    RENAME talker
)

install(PROGRAMS
    scripts/listener.py
    DESTINATION lib/${PROJECT_NAME}
    RENAME listener
)

install(PROGRAMS
    scripts/server.py
    DESTINATION lib/${PROJECT_NAME}
    RENAME server
)

install(PROGRAMS
    scripts/client.py
    DESTINATION lib/${PROJECT_NAME}
    RENAME client
)

find_package(rosidl_default_generators REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
  "action/Countdown.action"
)

install(PROGRAMS
    scripts/action_server.py
    DESTINATION lib/${PROJECT_NAME}
    RENAME action_server
)

install(PROGRAMS
    scripts/action_client.py
    DESTINATION lib/${PROJECT_NAME}
    RENAME action_client
)


ament_package()