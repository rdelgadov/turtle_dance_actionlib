#! /usr/bin/env python

import roslib
roslib.load_manifest('turtle_dance_actionlib')
import rospy
import actionlib

import turtle_dance_actionlib.msg

from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist

class server(object):
	global odom
	global rate
	global odome
	global odometry
	
	def callback(self, data):
		global odometry
		odometry = data
		
	def __init__(self, name):
		self._action_name = name
		self._as = actionlib.SimpleActionServer(self._action_name, turtle_dance_actionlib.msg.choreographerAction, self.execute, False)
		global odom
		global odome
		odom = rospy.Publisher('mobile_base/commands/velocity', Twist, queue_size=10)
		rospy.Subscriber('odom', Odometry, self.callback )
		global rate
		
		rate = rospy.Rate(5) # 10hz
		
		self._as.start()
	
		
	def execute(self, goal):
    # Do lots of awesome groundbreaking robot stuff here
		global odom
		global rate
		global odome
		global odometry
		twist = Twist()
		twist.linear.x = 0.3*goal.xsignal
		twist.angular.z = 0.5*goal.anglesignal
		print goal
		print round(odometry.pose.pose.orientation.z)
		if goal.xpos!=0:
			while goal.xpos != round(odometry.pose.pose.position.x):
				odom.publish(twist)
		if goal.anglesignal > 0:
			while goal.angle > round(odometry.pose.pose.orientation.z,2):
				odom.publish(twist)
		if goal.anglesignal < 0:
			while goal.angle < round(odometry.pose.pose.orientation.z,2):
				odom.publish(twist)
		twist.linear.x = 0
		twist.angular.z = 0
		odom.publish(twist)
		rate.sleep()
		self._as.set_succeeded()


if __name__ == '__main__':
	rospy.init_node('server')
	server = server(rospy.get_name())
	rospy.spin()
