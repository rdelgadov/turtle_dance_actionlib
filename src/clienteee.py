#! /usr/bin/env python

import roslib; 
roslib.load_manifest('turtle_dance_actionlib')
import rospy

# Brings in the SimpleActionClient
import actionlib

# Brings in the messages used by the fibonacci action, including the
# goal message and the result message.
import turtle_dance_actionlib.msg

def clienteee():
    # Creates the SimpleActionClient, passing the type of the action
    # (FibonacciAction) to the constructor.
	client = actionlib.SimpleActionClient('server', turtle_dance_actionlib.msg.choreographerAction)

    # Waits until the action server has started up and started
    # listening for goals.
	client.wait_for_server()

    # Creates a goal to send to the action server.
	goal = turtle_dance_actionlib.msg.choreographerGoal()
	goal.xpos = 2.0
	goal.angle = 0.0
	goal.xsignal = 1
	goal.anglesignal = 0

    # Sends the goal to the action server.
	client.send_goal( goal )

    # Waits for the server to finish performing the action.
	client.wait_for_result()
	
	goal = turtle_dance_actionlib.msg.choreographerGoal( xpos = -2, angle = 0, xsignal = -1, anglesignal = 0)
	client.send_goal( goal )
	client.wait_for_result()
	
	goal = turtle_dance_actionlib.msg.choreographerGoal( xpos = 2, angle = 0, xsignal = 1, anglesignal = 0)
	client.send_goal( goal )
	client.wait_for_result()
	
	goal = turtle_dance_actionlib.msg.choreographerGoal( xpos = 0, angle = 0.85 ,xsignal = 0, anglesignal = 1)
	client.send_goal( goal )
	client.wait_for_result()
	
	goal = turtle_dance_actionlib.msg.choreographerGoal( xpos = 0, angle = -0.85 ,xsignal = 0, anglesignal = -1)
	client.send_goal( goal )
	client.wait_for_result()
	
	goal = turtle_dance_actionlib.msg.choreographerGoal( xpos = 0, angle = 0 ,xsignal = 0, anglesignal = 1)
	client.send_goal( goal )
	client.wait_for_result()	
	
	goal = turtle_dance_actionlib.msg.choreographerGoal( xpos = -2, angle = 0 ,xsignal = -1, anglesignal = 0)
	client.send_goal( goal )
	client.wait_for_result()
	# Prints out the result of executing the action
	return "dance"  # A FibonacciResult

if __name__ == '__main__':
    try:
        # Initializes a rospy node so that the SimpleActionClient can
        # publish and subscribe over ROS.
        rospy.init_node('clienteee.py')
        result = clienteee()
        rospy.spin()
    except rospy.ROSInterruptException:
        print "program interrupted before completion"
