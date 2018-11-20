# Copyright (c) 2018, Adam Silverman et al, York University Robotics Society
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

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'compass.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Compass(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.batteryVoltage = QtWidgets.QTableWidget(self.centralwidget)
        self.batteryVoltage.setGeometry(QtCore.QRect(20, 10, 331, 131))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.batteryVoltage.setFont(font)
        self.batteryVoltage.setObjectName("batteryVoltage")
        self.batteryVoltage.setColumnCount(2)
        self.batteryVoltage.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(16)
        item.setFont(font)
        self.batteryVoltage.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(16)
        item.setFont(font)
        self.batteryVoltage.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(16)
        item.setFont(font)
        self.batteryVoltage.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(16)
        item.setFont(font)
        self.batteryVoltage.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(16)
        item.setFont(font)
        self.batteryVoltage.setHorizontalHeaderItem(1, item)
        self.temp = QtWidgets.QLabel(self.centralwidget)
        self.temp.setGeometry(QtCore.QRect(360, 70, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.temp.setFont(font)
        self.temp.setObjectName("temp")
        self.compass = QtWidgets.QWidget(self.centralwidget)
        self.compass.setGeometry(QtCore.QRect(360, 180, 300, 300))
        self.compass.setObjectName("compass")
        self.currentLat = QtWidgets.QLabel(self.centralwidget)
        self.currentLat.setGeometry(QtCore.QRect(360, 10, 221, 17))
        self.currentLat.setObjectName("currentLat")
        self.currentLong = QtWidgets.QLabel(self.centralwidget)
        self.currentLong.setGeometry(QtCore.QRect(590, 10, 231, 17))
        self.currentLong.setObjectName("currentLong")
        self.targetLong = QtWidgets.QLineEdit(self.centralwidget)
        self.targetLong.setGeometry(QtCore.QRect(680, 36, 141, 31))
        self.targetLong.setObjectName("targetLong")
        self.targetLat_2 = QtWidgets.QLabel(self.centralwidget)
        self.targetLat_2.setGeometry(QtCore.QRect(360, 40, 81, 17))
        self.targetLat_2.setObjectName("targetLat_2")
        self.targetLat = QtWidgets.QLineEdit(self.centralwidget)
        self.targetLat.setGeometry(QtCore.QRect(440, 36, 141, 31))
        self.targetLat.setObjectName("targetLat")
        self.targetLong_2 = QtWidgets.QLabel(self.centralwidget)
        self.targetLong_2.setGeometry(QtCore.QRect(590, 40, 101, 17))
        self.targetLong_2.setObjectName("targetLong_2")
        self.signalStrength = QtWidgets.QProgressBar(self.centralwidget)
        self.signalStrength.setGeometry(QtCore.QRect(520, 110, 118, 21))
        self.signalStrength.setProperty("value", 24)
        self.signalStrength.setObjectName("signalStrength")
        self.signalStrengthLabel = QtWidgets.QLabel(self.centralwidget)
        self.signalStrengthLabel.setGeometry(QtCore.QRect(360, 100, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.signalStrengthLabel.setFont(font)
        self.signalStrengthLabel.setObjectName("signalStrengthLabel")
        self.driveMode = QtWidgets.QLabel(self.centralwidget)
        self.driveMode.setGeometry(QtCore.QRect(360, 140, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.driveMode.setFont(font)
        self.driveMode.setObjectName("driveMode")
        self.roverHeading = QtWidgets.QLabel(self.centralwidget)
        self.roverHeading.setGeometry(QtCore.QRect(20, 150, 331, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.roverHeading.setFont(font)
        self.roverHeading.setObjectName("roverHeading")
        self.antennaHeading = QtWidgets.QLabel(self.centralwidget)
        self.antennaHeading.setGeometry(QtCore.QRect(20, 180, 331, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.antennaHeading.setFont(font)
        self.antennaHeading.setObjectName("antennaHeading")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(680, 70, 99, 27))
        self.pushButton.setObjectName("pushButton")
        self.waypointTable = QtWidgets.QTableWidget(self.centralwidget)
        self.waypointTable.setGeometry(QtCore.QRect(670, 110, 321, 191))
        self.waypointTable.setObjectName("waypointTable")
        self.waypointTable.setColumnCount(2)
        self.waypointTable.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        item.setFont(font)
        self.waypointTable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        item.setFont(font)
        self.waypointTable.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        item.setFont(font)
        self.waypointTable.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        item.setFont(font)
        self.waypointTable.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        item.setFont(font)
        self.waypointTable.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        item.setFont(font)
        self.waypointTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        item.setFont(font)
        self.waypointTable.setHorizontalHeaderItem(1, item)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.batteryVoltage.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Motor 1"))
        item = self.batteryVoltage.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Motor 2"))
        item = self.batteryVoltage.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Electronics"))
        item = self.batteryVoltage.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Current"))
        item = self.batteryVoltage.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Voltage"))
        self.temp.setText(_translate("MainWindow", "Temperature: "))
        self.currentLat.setText(_translate("MainWindow", "Current Lat:"))
        self.currentLong.setText(_translate("MainWindow", "Current Long:"))
        self.targetLat_2.setText(_translate("MainWindow", "Target Lat:"))
        self.targetLong_2.setText(_translate("MainWindow", "Target Long:"))
        self.signalStrengthLabel.setText(_translate("MainWindow", "Signal Strength: "))
        self.driveMode.setText(_translate("MainWindow", "Drive Mode: "))
        self.roverHeading.setText(_translate("MainWindow", "Rover Heading: "))
        self.antennaHeading.setText(_translate("MainWindow", "Antenna Heading: "))
        self.pushButton.setText(_translate("MainWindow", "Add"))
        item = self.waypointTable.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Waypoint 1"))
        item = self.waypointTable.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Waypoint 2"))
        item = self.waypointTable.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Waypoint 3"))
        item = self.waypointTable.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "Waypoint 4"))
        item = self.waypointTable.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "Waypoint 5"))
        item = self.waypointTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Distance"))
        item = self.waypointTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Heading"))

