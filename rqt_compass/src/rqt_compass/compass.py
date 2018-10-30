# Copyright (c) 2018, Matthew Cardinal, York University Robotics Society
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#   * Redistributions of source code must retain the above copyright
#     notice, this list of conditions and the following disclaimer.
#   * Redistributions in binary form must reproduce the above
#     copyright notice, this list of conditions and the following
#     disclaimer in the documentation and/or other materials provided
#     with the distribution.
#   * Neither the name of the TU Darmstadt nor the names of its
#     contributors may be used to endorse or promote products derived
#     from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

import os
import rospy
import rospkg
import sys
import math
import Queue


from qt_gui.plugin import Plugin
from python_qt_binding import loadUi, QtGui, QtCore, QtWidgets
from python_qt_binding.QtWidgets import QWidget
from std_msgs.msg import Float32, String
from sensor_msgs.msg import NavSatFix
# ui image paths
rover_image = os.path.join(rospkg.RosPack().get_path('rqt_compass'), 'images', 'rover.png')
compass_image = os.path.join(rospkg.RosPack().get_path('rqt_compass'), 'images', 'compass.png')
destination_image = os.path.join(rospkg.RosPack().get_path('rqt_compass'), 'images', 'destination.png')
base_image = os.path.join(rospkg.RosPack().get_path('rqt_compass'), 'images', 'base.png')


class Compass(Plugin):
    def center(self, label):
        c_x = self._widget.compass.width() / 2 + self._widget.compass.x() - label.width() / 2
        c_y = self._widget.compass.height() / 2 + self._widget.compass.y() - label.height() / 2
        label.move(int(c_x), int(c_y))
    # set initial position and sizes for ui images
    def setup(self):
        self.setImage(compass_image, 300, 300, self._widget.compass, self.rover_bearing, scale = False)
        self.setImage(compass_image, 300, 300, self._widget.compass, self.rover_bearing, scale = False)
        self.setImage(rover_image, 100, 100, self._widget.rover, 0)
        self.setImage(destination_image, 100, 200, self._widget.destination, 0)
        self.setImage(base_image, 100, 800, self._widget.base, 0)
        self.center(self._widget.rover)
        self.base_bearing = self.gps_to_bearing(self.rover_position['lat'], self.rover_position['long'], self.base_position['lat'], self.base_position['long'])
        self.goal_bearing = self.gps_to_bearing(self.rover_position['lat'], self.rover_position['long'], self.goal_position['lat'], self.goal_position['long'])
        self.setTargetPosition(self._widget.destination, self.goal_bearing+ self.rover_bearing, self._widget.compass)
        self.setTargetPosition(self._widget.base, self.base_bearing + self.rover_bearing, self._widget.compass)

    # set the position and bearing of an image
    def setImage(self, image_string, x, y, label, l_bearing, scale=True):
        if scale == False:
            l_bearing -= 90
        p_map = QtGui.QPixmap(image_string)
        p_map = p_map.scaled(x, y, QtCore.Qt.KeepAspectRatio)
        transform = QtGui.QTransform().rotate(l_bearing)
        p_map = p_map.transformed(transform, QtCore.Qt.SmoothTransformation)
        QtWidgets.QLabel.setPixmap(label , p_map)
        label.setAlignment(QtCore.Qt.AlignCenter)
        if scale == True:
            label.setScaledContents(True)

    # set the position and bearing of a target location
    def setTargetPosition(self, label, bearing, compass):
        bearing = math.radians(- 1 * bearing)
        radius = compass.x() + (compass.width() / 2)
        new_x = radius + math.cos(bearing) * 0.59 * radius - 0.5 * label.width()
        new_y = radius - radius * math.sin(bearing) * 0.59 - 0.5 *label.width()
        label.move(int(new_x), int(new_y))

    # transform from gps coordinates to bearing
    def gps_to_bearing(self, lat1, long1, lat2, long2):
        delta_long = float(long2) - float(long1)
        y = math.sin(delta_long) * math.cos(float(lat2))
        x = math.cos(float(lat1)) * math.sin(float(lat2)) - math.sin(float(lat1))*math.cos(float(lat2))*math.cos(delta_long)
        result = math.degrees(math.atan2(y, x))
        return float(result)

    def __init__(self, context):
        super(Compass, self).__init__(context)
        self.setObjectName('Compass')
        self._publisher = None

        self._widget = QWidget()
        rp = rospkg.RosPack()
        ui_file = os.path.join(rospkg.RosPack().get_path('rqt_compass'), 'resource', 'compass.ui')
        loadUi(ui_file, self._widget)
        self._widget.setObjectName('Compass')
        if context.serial_number() > 1:
            self._widget.setWindowTitle(
            self._widget.windowTitle() + (' (%d)' % context.serial_number()))
        context.add_widget(self._widget)
        self.setup()
        self._widget.goButton.clicked.connect(self.go_button_click)
        self._widget.refresh = QtCore.QTimer()
        self._widget.refresh.timeout.connect(self.update_compass)
        self._widget.refresh.start(100)
        self.listen()

    base_position = {'lat': float(43.774497), 'long': float(-79.500872)}
    base_bearing = float(0)
    rover_position = {'lat': float(43.771529), 'long': float(-79.506777)}
    rover_bearing = float(45)
    goal_position = {'lat': float(43.771875), 'long': float(-79.503300)}
    goal_bearing = float(0)
    mode = "drive"
    atmo = 0.0
    rad = 0.0
    rad_error = 0.0
    temperature = 0.0
    radio = 0.0
    oxygen = 0.0
    load = 0.0
    bearing_queue = Queue.Queue(maxsize=10)	

    def add_bearing(self, bearing):
	if (self.bearing_queue.qsize() >= 10):
                self.bearing_queue.get()
        if bearing >= 360:
            bearing -= 360
	self.bearing_queue.put(bearing)

    def get_bearing(self):
        bearing_total = 0.0
	ne, se = 0, 0
        bearing_copy = Queue.Queue(maxsize=10)
        while (not self.bearing_queue.empty()):
	    bearing = self.bearing_queue.get()
	    bearing_total += bearing
            if bearing > 270:
                se += 1
            elif bearing < 90:
                ne += 1
            bearing_copy.put(bearing)
        if ne > 0 and se > 0:
            bearing_total -= 360 * se
        self.bearing_queue = bearing_copy
        result = bearing_total / float(self.bearing_queue.qsize())
        if result >= 360:
            result -= 360
	return result

    def go_button_click(self):
        try:
            self.goal_position['lat'] = float(self._widget.latText.text())
            self.goal_position['long'] = float(self._widget.longText.text())
            self.update_compass()
            self.update_data()
        except:
            self._widget.bearingLabel.setText("error")

    def listen(self):
        self.mag_sub = rospy.Subscriber("/compass", Float32, self.mag_callback)
        self.base_sub = rospy.Subscriber("/base_gps_data", NavSatFix, self.base_callback)
        self.rover_sub = rospy.Subscriber("/rover_gps_data", NavSatFix, self.rover_callback)
	self.mode_sub = rospy.Subscriber("/mode", String, self.mode_callback)
	self.atmo_sub = rospy.Subscriber("/pressure", Float32, self.atmo_callback)
	self.rad_sub = rospy.Subscriber("/radiation", Float32, self.rad_callback)
	self.rad_error_sub = rospy.Subscriber("/radiation_error", Float32, self.rad_error_callback)
	self.temp_sub = rospy.Subscriber("/temperature", Float32, self.temperature_callback)
	self.radio_sub = rospy.Subscriber("/radio", Float32, self.radio_callback)
	self.oxygen_sub = rospy.Subscriber("/oxygen", Float32, self.oxygen_callback)
	self.load_sub = rospy.Subscriber("/load", Float32, self.load_callback)
        pass

    def load_callback(self, data):
	self.load = data.data
    def oxygen_callback(self, data):
	self.oxygen = data.data
    def temperature_callback(self, data):
        self.temperature = data.data
    def radio_callback(self, data):
	self.radio = data.data
    def atmo_callback(self, data):
	self.atmo = data.data
    def rad_callback(self, data):
	self.atmo = data.data
    def rad_error_callback(self, data):
	self.rad_error = data.data
    def mode_callback(self, data):
	self.mode = data.data;
    def mag_callback(self, data):
        self.add_bearing( (float(data.data) + 90) )
        self.rover_bearing = self.get_bearing()
    def rover_callback(self, data):
        self.rover_position['long'] = data.longitude
        self.rover_position['lat'] = data.latitude
    def base_callback(self, data):
        self.base_position['long'] = data.longitude
        self.base_position['lat'] = data.latitude
    def update_compass(self):
        self.setImage(compass_image, 300, 300, self._widget.compass, self.rover_bearing, scale = False)
        self.refresh_goal()
        self.refresh_base()
        self.update_data()
    def update_data(self):
        self._widget.bearingLabel.setText(("%.2f degrees" % (self.rover_bearing)));
        self._widget.goalDistanceData.setText(("%.3f km" % self.distance(self.rover_position, self.goal_position)))
        self._widget.baseDistance.setText(("%.3f km" % self.distance(self.rover_position, self.base_position)))
	self._widget.modeData.setText(self.mode)
	self._widget.airPressureData.setText(("%.2f kPa" % (self.atmo)))
	self._widget.radiationData.setText(("%.2f uSv +/- %.2f" % (self.rad, self.rad_error)))
        self._widget.temperatureData.setText(("%.2f C" % self.temperature))
	self._widget.radioData.setText(("%.2f V" % self.radio))
	self._widget.oxygenData.setText(("%.4f" % self.oxygen))
	self._widget.loadData.setText(("%.2f" % self.load))
    def distance (self, pos1, pos2):
        R = 6371
        deltaLat = math.radians(pos2['lat'] -  pos1['lat'])
        deltaLong = math.radians(pos2['long'] - pos1['long'])
        a =  math.pow(math.sin(deltaLat / 2.0), 2) + math.cos(math.radians(pos1['lat']))*math.cos(math.radians(pos2['lat'])) * math.pow(math.sin(deltaLong / 2.0), 2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
	return c * R

    def refresh_goal(self):
        self.goal_bearing = self.gps_to_bearing(self.rover_position['lat'], self.rover_position['long'], self.goal_position['lat'], self.goal_position['long'])
        self.setTargetPosition(self._widget.destination, self.goal_bearing + self.rover_bearing, self._widget.compass)

    def refresh_base(self):
        self.base_bearing = self.gps_to_bearing(self.rover_position['lat'], self.rover_position['long'], self.base_position['lat'], self.base_position['long'])
        self.setTargetPosition(self._widget.base, self.base_bearing + self.rover_bearing, self._widget.compass)

    def shutdown_plugin(self):
        # Tunregister all publishers here
        self.mag_sub.unregister()
        self.base_sub.unregister()
        self.rover_sub.unregister()
	self.mode_sub.unregister()
        pass

    def save_settings(self, plugin_settings, instance_settings):
        # TODO save intrinsic configuration, usually using:
        #instance_settings.set_value(k, v)
        #instance_settings.set_value('bearing', self.rover_bearing)
        #instance_settings.set_value('rover_position', self.rover_position)
        #instance_settings.set_value('base_position', self.base_position)
        #instance_settings.set_value('goal_position', self.goal_position)
        pass

    def restore_settings(self, plugin_settings, instance_settings):
        # TODO restore intrinsic configuration, usually using:
        # v = instance_settings.value(k)
        #self.rover_bearing = float(instance_settings.value('bearing'))
        #self.rover_position = instance_settings.value('rover_position')
        #self.base_position = instance_settings.value('base_position')
        #self.goal_position = instance_settings.value('goal_position')
        pass
