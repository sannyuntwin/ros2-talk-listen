# ROS 2 Basics — Talker & Listener

A beginner ROS 2 project for learning core concepts step by step: topics, services, and actions.

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

---

## Prerequisites

**Install ROS 2 Jazzy** — follow the [official guide](https://docs.ros.org/en/jazzy/Installation/Ubuntu-Install-Debs.html)

```bash
# After installing ROS 2
sudo apt install python3-colcon-common-extensions
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

## Package Structure

```
src/ros2_basics/
├── package.xml
├── CMakeLists.txt
└── scripts/
    ├── talker.py     # Publishes String to /chatter every 1 second
    └── listener.py   # Subscribes to /chatter and prints messages
```

---

## License

MIT
