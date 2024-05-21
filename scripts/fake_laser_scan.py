#!/usr/bin/env python3
import rospy
from turtlesim.msg import Pose
from sensor_msgs.msg import LaserScan
import math

# Parameters
RADIUS = 2.0  # Radius of the circular obstacles
LASER_RANGE = 4.0  # Range for the laser scan to simulate circular obstacles
RESOLUTION = 360  # Resolution of the fake laser scan (number of points)

# Global variable to store turtle1's pose
turtle1_pose = None

def create_fake_laser_scan(turtle2_pose):
    scan = LaserScan()
    scan.header.stamp = rospy.Time.now()
    scan.header.frame_id = "turtle2"
    scan.angle_min = -math.pi
    scan.angle_max = math.pi
    scan.angle_increment = 2 * math.pi / RESOLUTION
    scan.range_min = 0.0
    scan.range_max = LASER_RANGE
    scan.ranges = [LASER_RANGE] * RESOLUTION

    if turtle1_pose:
        for i in range(RESOLUTION):
            angle = scan.angle_min + i * scan.angle_increment
            world_angle = angle + turtle2_pose.theta  # Transform angle to world frame
            x = turtle2_pose.x
            y = turtle2_pose.y
            x1 = turtle1_pose.x
            y1 = turtle1_pose.y

            dx = x1 - x
            dy = y1 - y
            distance = math.sqrt(dx ** 2 + dy ** 2)

            theta = math.atan2(dy, dx)
            if abs(theta - world_angle) < scan.angle_increment:
                if distance <= RADIUS:
                    scan.ranges[i] = distance

    return scan

def pose_callback_turtle1(msg):
    global turtle1_pose
    turtle1_pose = msg

def pose_callback_turtle2(msg):
    global turtle2_scan_pub
    scan = create_fake_laser_scan(msg)
    turtle2_scan_pub.publish(scan)

if __name__ == '__main__':
    rospy.init_node('fake_laser_scan')

    turtle2_scan_pub = rospy.Publisher('/turtle2/scan', LaserScan, queue_size=10)

    rospy.Subscriber('/turtle1/pose', Pose, pose_callback_turtle1)
    rospy.Subscriber('/turtle2/pose', Pose, pose_callback_turtle2)

    rospy.spin()
