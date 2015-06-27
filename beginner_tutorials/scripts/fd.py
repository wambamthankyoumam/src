#!/usr/bin/env python
import roslib
import sys
import rospy
import cv2
import math
import numpy as np
from numpy.linalg import inv
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

faceCascade = cv2.CascadeClassifier('/haarcascade_frontalface_default.xml')


class fd:


  def __init__(self,data):
    faces = faceCascade.detectMultiScale(
    data,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    flags = cv2.cv.CV_HAAR_SCALE_IMAGE
    )
    print "tits"

    for(a,b,c,d) in faces:
      cv2.rectangle(img, (a, b), (a+c, b+d), (0, 255, 0), 2)
      print "tits"
      cv2.imshow("Image window", img)
      cv2.waitKey(3)




class image_converter:

  def __init__(self):
    # self.image_pub = rospy.Publisher("image_topic_2",Image)

    cv2.namedWindow("Image window", 1)
    self.bridge = CvBridge()
    self.image_sub = rospy.Subscriber("image_raw",Image,self.callback)


  def callback(self,data):
    try:
      cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
    except CvBridgeError, e:
      print e

    gray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY) 
    




      

    # (rows,cols,channels) = cv_image.shape
    # if cols > 60 and rows > 60 :
    #   cv2.circle(cv_image, (50,50), 10, 255)



    
    
    # try:
    #   self.image_pub.publish(self.bridge.cv2_to_imgmsg(cv_image, "bgr8"))
    # except CvBridgeError, e:
    #   print e

def main(args):
  img = cv2.imread('1.jpg')
  ic = image_converter()
  fc = fd(img)
  rospy.init_node('image_converter', anonymous=True)
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print "Shutting down"
  cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)