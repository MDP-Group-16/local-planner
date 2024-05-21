# Notes
Used ChatGPT4o to get everythin working

Installed ros navigation. Appearently it is split up in nav_core, move_base and amcl.

Creating new package with dependencies:

```
cd ~/catkin_ws/src
catkin_create_pkg turtle_dwa rospy std_msgs geometry_msgs nav_msgs turtlesim move_base
```

Start DWA turtle:
Make sure roscore is on with

```
roscore
```

```
cd ~/catkin_ws
catkin_make
source devel/setup.bash
```

```
roslaunch turtle_dwa turtle_dwa.launch
```

Monitor the goal topic:

```
rostopic echo turtle2/move_base_simple/goal
```

Move turtle2 with:

```
rostopic pub /turtle2/move_base_simple/goal geometry_msgs/PoseStamped "header:
  seq: 0
  stamp:
    secs: 0
    nsecs: 0
  frame_id: 'world'
pose:
  position:
    x: 9.0
    y: 5.0
    z: 0.0
  orientation:
    x: 0.0
    y: 0.0
    z: 0.0
    w: 1.0"
```
