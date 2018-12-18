#!/usr/bin/env python
import rospy
from std_msgs.msg import Int16, Bool, String
from sensor_msgs.msg import Joy
from joysticks.msg import drive, arm, grip
import os

controller_topic_left = "controller_left"
controller_port_left = rospy.get_param(controller_topic_left)['dev']
controller_topic_right = "controller_left"
controller_port_right = rospy.get_param(controller_topic_right)['dev']
left_offset = -1
right_offset = -1
headlights_mode = "off"

left_stick = 0
right_stick = 0

# responds to raw joystick data, splitting it into topics relevant to different devices
def joystick_callback_left(data): # Logitech Attack 3
	global mode # the current mode of the control system
	global left_offset
	global right_offset
	global left_stick
	global right_stick

	left_axis = 1
	side_axis = 0
	throttle = 3
	middle_button = 2


	mode_switch(data.buttons[middle_button]) # switch modes if the middle button is pressed
	left_stick = 255 * data.axes[left_axis] # obtain left thumbstick y-axis data
	side_stick = 255 * data.axes[side_axis] # obtain left thumbstick x-axis data


	# drive mode: publish axis data to drive topic
	if mode == "drive":
		msg = drive()
		msg.left = left_stick
		msg.right = right_stick
		pub_drive.publish(msg)
	# arm mode: publish axis data to arm topic
	'''elif mode == "arm":
		msg = arm()
		msg.joint1 = left_stick
		msg.joint2 = right_stick
		msg.joint3 = up_down
		pub_arm.publish(msg)
	# grip mode: publish axis data to grip topic
	else:
		msg = grip()
		msg.grip = up_down
		msg.roll = left_stick
		msg.pan = right_stick
		pub_grip.publish(msg)'''


def joystick_callback_right(data):
	global mode # the current mode of the control system
	global left_offset
	global right_offset
	global left_stick
	global right_stick

	right_axis = 1
	side_axis = 0
	turret_axis = 2
	throttle = 3
	middle_button = 2


	mode_switch(data.buttons[middle_button]) # switch modes if the middle button is pressed
	right_stick = 255 * data.axes[right_axis] # obtain right thumbstick data
	side_stick = 255 * data.axes[side_axis] # obtain left thumbstick x-axis data


	# set turret to difference of right and left sides
	turret = 255 * data.axes[turret_axis]
	# drive mode: publish axis data to drive topic
	if mode == "drive":
		msg = drive()
		msg.left = left_stick
		msg.right = right_stick
		pub_drive.publish(msg)
	# arm mode: publish axis data to arm topic
	'''elif mode == "arm":
		msg = arm()
		msg.joint1 = left_stick
		msg.joint2 = right_stick
		msg.joint3 = up_down
		pub_arm.publish(msg)
	# grip mode: publish axis data to grip topic
	else:
		msg = grip()
		msg.grip = up_down
		msg.roll = left_stick
		msg.pan = right_stick
		pub_grip.publish(msg)'''

	# publish turret data
	pub_turret.publish(turret)
def headlight_switch(button):
	global headlights_mode
	global pub_headlights
	if button == 1:
		result = 0
		if headlights_mode == "on":
			headlights_mode = "off"
		else:
			headlights_mode = "on"
			result = 255
		pub_headlights.publish(result)
# switch the control mode
def mode_switch(button):
	global mode
	if button == 1:
		if mode == "drive":
			mode = "arm"
		elif mode == "arm":
			mode = "grip"
		else:
			mode = "drive"
		pub_mode.publish(mode);

def lock_switch(button):
	global lock
	global mode
	if button == 1 and mode == "grip":
		if lock == True:
			lock = False
		else:
			lock = True
		msg = Bool()
		msg.data = lock
		pub_lock.publish(msg)
	
# Intializes everything
def start():
	global mode # make mode available to other functions
	global lock
	lock = False
	mode = "drive" # start in drive mode
	rospy.init_node('controller_publisher') # initialize the node

	# make publishers available to other functions
	global pub_drive
	global pub_arm
	global pub_grip
	global pub_turret
	global pub_timeout
	global pub_headlights
	global pub_mode
	global pub_lock

	# create publishers
	pub_drive = rospy.Publisher('drive', drive, queue_size=1)
	pub_arm = rospy.Publisher('arm', arm, queue_size=1)
	pub_grip = rospy.Publisher('grip', grip, queue_size=1)
	pub_turret = rospy.Publisher('turret', Int16, queue_size=1)
	pub_timeout = rospy.Publisher('controller_timeout', Bool, queue_size=1)
	pub_headlights = rospy.Publisher("headlights", Int16, queue_size=1)
	pub_mode = rospy.Publisher("mode", String, queue_size=1)
	pub_lock = rospy.Publisher("lock_grip", Bool, queue_size=1)
	pub_mode.publish(mode)

	msg = Bool()
	msg.data = False
	pub_lock.publish(msg)

	# subscribed to joystick inputs on topic "joy"
	rospy.Subscriber("controller_left", Joy, joystick_callback_left)
	rospy.Subscriber("controller_right", Joy, joystick_callback_right)
	rospy.Timer(rospy.Duration(0.2), timeoutCallback)
	rospy.spin()

	#rospy.Subscriber("controller_right", Joy, joystick_callback_right)
	#rospy.Timer(rospy.Duration(0.2), timeoutCallback)
	#rospy.spin()

def timeoutCallback(event):
	msg = Bool()
	msg.data = checkController()
	pub_timeout.publish(msg)

def checkController():
	result = os.path.exists(controller_port_left)
	if (not result):
		reset_offset()
	return result

def reset_offset():
	global left_offset
	global right_offset
	left_offset = -1
	right_offset = -1
	
if __name__ == '__main__':
	start()
