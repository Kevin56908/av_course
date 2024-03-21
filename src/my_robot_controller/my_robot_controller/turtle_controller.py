#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist

class TurtleControllerNode(Node):
    def __init__(self):
        super().__init__("turtle_controller")
        self.get_logger().info("Controller has been started.")
        self.cmd_vel_publisher = self.create_publisher(
            Twist, "/turtle1/cmd_vel", 10)
        self._pose_subscriber = self.create_subscription(
            Pose, '/turtle1/pose', self.pose_callback, 10)
        
    def pose_callback(self, pose: Pose):
        cmd = Twist()
        if 1.0 < pose.x < 9.0 and 1.0 < pose.y < 9.0:
            cmd.linear.x = 5.0
            cmd.angular.z = 0.0
        else:
            cmd.linear.x = 1.0
            cmd.angular.z = 2.0
        self.cmd_vel_publisher.publish(cmd)

def main(args=None):
    rclpy.init(args=args)
    node = TurtleControllerNode()
    rclpy.spin(node)
    rclpy.shutdown()