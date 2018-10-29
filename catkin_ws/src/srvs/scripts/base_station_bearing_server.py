#!/usr/bin/env python
import rospy
from sensor_msgs.msg import NavSatFix
from std_msgs.msg import Float32
import os

base_topic = "base_station"
rover_topic = "rover"
rover_position = {'long': 45.0, 'lat': 45.0}
base_position = {'long': 45.0, 'lat': 45.0}


def rover_callback(data):
	global rover_position

	rover_position['long'], rover_position['lat'] = get_location(data)
	publish_bearing()

def base_callback(data):

	global base_position

	base_position['long'], base_position['lat'] = get_location(data)
	publish_bearing()

def get_location(fix):
	return fix.longitude, fix.latitude

def get_bearing():
        delta_long = float(rover_position['long']) - float(base_position['long'])
        y = math.sin(delta_long) * math.cos(float(rover_position['lat']))
        x = math.cos(float(base_position['lat'])) * math.sin(float(rover_position['lat'])) - math.sin(float(base_position['lat']))*math.cos(float(rover_position['lat']))*math.cos(delta_long)
        result = math.degrees(math.atan2(y, x))
        return float(result)

def publish_bearing(bearing):
	pub_base_bearing.publish(get_bearing())

def start():
	rospy.init_node('base_station_bearing') # initialize the node

	# make publishers available to other functions
	global pub_base_bearing

	# create publishers
	pub_base_bearing = rospy.Publisher('base_bearing', Float32, queue_size=1)

	# subscribed to joystick inputs on topic "joy"
	rospy.Subscriber(base_topic, NavSatFix, base_callback)
	rospy.Subscriber(rover_topic, NavSatFix, rover_callback)
	rospy.spin()
	
if __name__ == '__main__':
	start()
