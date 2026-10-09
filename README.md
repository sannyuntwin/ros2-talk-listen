# ROS 2 Basics — Topics, Services, Actions & Diff Drive Robot

A beginner ROS 2 project for learning core concepts step by step: topics, services, actions, and a real diff-drive robot in Gazebo.

## Stack

| Component | Version |
|---|---|
| OS | Ubuntu 24.04 LTS |
| ROS 2 | Jazzy Jalisco |
| Language | Python (rclpy) |

---

## Concepts Covered

| Step | Concept | What it does |
|---|---|---|
| 1 | **Topic** | Talker publishes, Listener subscribes (one-way stream) |
| 2 | **Service** | Client sends a request, Server returns a response |
| 3 | **Action** | Client sends a goal, Server streams feedback, then returns result |
| 4 | **Diff Drive Robot** | URDF robot in Gazebo, driven by `/cmd_vel` Twist messages |

---

## Prerequisites

**Install ROS 2 Jazzy** — follow the [official guide](https://docs.ros.org/en/jazzy/Installation/Ubuntu-Install-Debs.html)

```bash
# After installing ROS 2
sudo apt install python3-colcon-common-extensions \
  ros-jazzy-ros-gz-sim ros-jazzy-ros-gz-bridge \
  ros-jazzy-robot-state-publisher ros-jazzy-xacro
```

Source ROS 2 in every new terminal (or add to `~/.bashrc`):
```bash
source /opt/ros/jazzy/setup.bash
```

---

## Setup

```bash
mkdir -p ~/ros2/ros2-talk-listen/src
cd ~/ros2/ros2-talk-listen/src
git clone https://github.com/<your-username>/ros2-talk-listen ros2_basics
cd ~/ros2/ros2-talk-listen
colcon build
source install/setup.bash
```

---

## Step 1 — Topic: Talker → Listener

One node publishes a message. Another node receives it.

```
talker  →  /chatter (String)  →  listener
```

**Terminal A:**
```bash
source ~/ros2/ros2-talk-listen/install/setup.bash
ros2 run ros2_basics talker
```

**Terminal B:**
```bash
source ~/ros2/ros2-talk-listen/install/setup.bash
ros2 run ros2_basics listener
```

Expected output:
```
[talker]   Published: Hello 0
[talker]   Published: Hello 1
[listener] Received: Hello 0
[listener] Received: Hello 1
```

---

## Step 2 — Service: AddTwoInts

A client sends two numbers, a server returns the sum. One request → one response.

```
client  →  request (a=3, b=5)  →  server
client  ←  response (sum=8)    ←  server
```

**Terminal A — start the server:**
```bash
source ~/ros2/ros2-talk-listen/install/setup.bash
ros2 run ros2_basics server
```

**Terminal B — call the client:**
```bash
source ~/ros2/ros2-talk-listen/install/setup.bash
ros2 run ros2_basics client 3 5
```

Expected output:
```
[add_two_ints_server] 3 + 5 = 8
[add_two_ints_client] Result: 3 + 5 = 8
```

---

## Step 3 — Action: Countdown

A client sends a goal (target number), the server streams feedback every second while counting down, then returns a final result.

```
client  →  goal (target=5)          →  server
client  ←  feedback (remaining: 4)  ←  server  (each second)
client  ←  result (message="done")  ←  server
```

**Terminal A — start the action server:**
```bash
source ~/ros2/ros2-talk-listen/install/setup.bash
ros2 run ros2_basics action_server
```

**Terminal B — send a goal:**
```bash
source ~/ros2/ros2-talk-listen/install/setup.bash
ros2 run ros2_basics action_client 5
```

Expected output:
```
[countdown_client] Feedback: 5 remaining
[countdown_client] Feedback: 4 remaining
[countdown_client] Feedback: 3 remaining
[countdown_client] Feedback: 2 remaining
[countdown_client] Feedback: 1 remaining
[countdown_client] Result: done
```

---

## Step 4 — Diff Drive Robot in Gazebo

A two-wheeled robot loaded from URDF, spawned in Gazebo, driven by keyboard.

```
teleop  →  /cmd_vel (Twist)  →  ros_gz_bridge  →  Gazebo diff drive plugin  →  wheels
```

**Architecture:**

| Component | Role |
|---|---|
| `robot_state_publisher` | Reads URDF, broadcasts TF frames |
| `gz sim` | Opens Gazebo with an empty world |
| `ros_gz_sim create` | Spawns the robot from `/robot_description` topic |
| `ros_gz_bridge` | Bridges `/cmd_vel` and `/odom` between ROS 2 and Gazebo |

**Terminal A — launch everything:**
```bash
source ~/ros2/ros2-talk-listen/install/setup.bash
ros2 launch diff_drive_robot robot.launch.py
```

**Terminal B — autonomous square drive:**
```bash
source ~/ros2/ros2-talk-listen/install/setup.bash
ros2 run diff_drive_robot drive
```

**Terminal B — keyboard control (click this terminal before pressing keys):**
```bash
source ~/ros2/ros2-talk-listen/install/setup.bash
ros2 run diff_drive_robot teleop
```

Keyboard controls:
```
w = forward      s = backward
a = turn left    d = turn right
space = stop     q = quit
```

---

## Package Structure

```
src/
├── ros2_basics/
│   ├── package.xml
│   ├── CMakeLists.txt
│   ├── action/
│   │   └── Countdown.action      # Custom action definition
│   └── scripts/
│       ├── talker.py             # Publishes String to /chatter every 1 second
│       ├── listener.py           # Subscribes to /chatter and prints messages
│       ├── server.py             # AddTwoInts service server
│       ├── client.py             # AddTwoInts service client
│       ├── action_server.py      # Countdown action server
│       └── action_client.py      # Countdown action client
│
└── diff_drive_robot/
    ├── package.xml
    ├── CMakeLists.txt
    ├── urdf/
    │   └── robot.urdf.xacro   # Box body, 2 wheels, caster + diff drive plugin
    ├── launch/
    │   └── robot.launch.py    # Launches RSP, Gazebo, spawn, bridge
    └── scripts/
        ├── drive.py           # Drives a square autonomously
        └── teleop.py          # Keyboard control via w/a/s/d
```

---

## License

MIT
