#!/usr/bin/env python
from __future__ import print_function

import roslib
roslib.load_manifest('opencv_balltrack')
import sys
import rospy
import cv2
import imutils
import numpy as np
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from collections import deque


class image_converter:

  def __init__(self):
    self.image_pub = rospy.Publisher("trackedBall/camera1",Image,queue_size=10)
    self.location_pub = rospy.Publisher("locationBall/camera1",string,queue_size=10)

    self.bridge = CvBridge()
    self.image_sub = rospy.Subscriber("camera1/camera",Image,self.callback)

  def callback(self,data):
    try:
      cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
    except CvBridgeError as e:
      print(e)

    #define boundaries of color (in this case green, HSV)
    greenLower = (29, 86, 6)
    greenUpper = (64, 255, 255)
    
    #resize for easier manipulation
    cv_image = imutils.resize(cv_image, width=600)
    #option to blur if needed
    # blurred = cv2.GaussianBlur(cv_image, (11, 11), 0)
    #recolor to HSV
    hsv = cv2.cvtColor(cv_image, cv2.COLOR_BGR2HSV)  
    
    #construct masks for the green color, then remove blobs
    mask = cv2.inRange(hsv, greenLower, greenUpper)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    #find contours in mask and initialize center of ball (x,y)
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE)[-2]
    center = None

    #proceed if at least one contour was found.
    if len(cnts) > 0:
      # find the largest contour in the mask, then use
      # it to compute the minimum enclosing circle and
      # centroid
      c = max(cnts, key=cv2.contourArea)
      ((x, y), radius) = cv2.minEnclosingCircle(c)
      M = cv2.moments(c)
      center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

      # only proceed if radius meets a minimum size
      if radius > 10:
        # draw the circle and centroid on the frame,
        # then update the list of tracked points
        cv2.circle(cv_image, (int(x), int(y)), int(radius),
          (0, 255, 255), 2)
        cv2.circle(cv_image, center, 3, (0, 0, 255), -1)




    cv2.imshow("Image window", cv_image)
    cv2.waitKey(3)

    try:
      self.image_pub.publish(self.bridge.cv2_to_imgmsg(cv_image, "bgr8"))
    except CvBridgeError as e:
      print(e)

def main(args):
  
  rospy.init_node('image_converter', anonymous=True)
  ic = image_converter()
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")
  cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)
