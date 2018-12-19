#!/usr/bin/env python
import rospy
from sensor_msgs.msg import NavSatFix
from std_msgs.msg import Float32
import os
from geographiclib.geodesic import Geodesic
import math

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
	from geographiclib.geodesic import Geodesic
	g = Geodesic.WGS84.Inverse(rover_position['lat'], rover_position['long'], base_position['lat'], base_position['long'])
	return g['a12']


def publish_bearing(bearing):
	pub_base_bearing.publish(get_bearing())

def start():
	rospy.init_node('base_station_bearing') # initialize the node

	# make publishers available to other functions
	global pub_base_bearing

	# create publishers
	pub_base_bearing = rospy.Publisher('base_bearing', Float32, queue_size=1)

	# subscribed to position inputs
	rospy.Subscriber("base_pos", NavSatFix, base_callback)
	rospy.Subscriber("rover_pos", NavSatFix, rover_callback)
	rospy.spin()
	
if __name__ == '__main__':
	start()
