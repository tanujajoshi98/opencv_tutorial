# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 20:22:48 2020

@author: acer
"""

#......Color Detection ......

import cv2
import numpy as np
framewidth = 300
frameheight=400
cap= cv2.VideoCapture(0)
cap.set(3,framewidth)
cap.set(4,frameheight)
cap.set(10,130)

def empty(a):
    pass

#path = "lambo.jpg"
#img = cv2.imread("Lambo1.jpg")
cv2.namedWindow("TrackBars")
cv2.resizeWindow("Trackbars",640,240)
cv2.createTrackbar("Hue Min","TrackBars",0,179,empty)
cv2.createTrackbar("Hue Max","TrackBars",179,179,empty)
cv2.createTrackbar("Sat Min","TrackBars",0,255,empty)   # Saturation 
cv2.createTrackbar("Sat Max","TrackBars",255,255,empty)
cv2.createTrackbar("Val Min","TrackBars",0,255,empty)    #Value
cv2.createTrackbar("Val Max","TrackBars",255,255,empty)


while True:
    success, img =cap.read()
    #img = cv2.imread("Lambo3.jpg")
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    
    h_min = cv2.getTrackbarPos("Hue Min","TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max","TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min","TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max","TrackBars")
    v_min = cv2.getTrackbarPos("Val Min","TrackBars")
    v_max = cv2.getTrackbarPos("Val Max","TrackBars")
    print(h_min,h_max,s_min,s_max,v_min,v_max)
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    
    mask=cv2.inRange(imgHSV,lower,upper)
    result = cv2.bitwise_and(img, img, mask = mask)
    
    mask = cv2.cvtColor(mask,cv2.COLOR_GRAY2BGR)
    #imgResult = cv2.bitwise_and(img, img, mask=mask)
    cv2.imshow("Image",img)
   # cv2.imshow("HSV",imgHSV)
    cv2.imshow("mask",mask)
    cv2.imshow("result",result)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
    
    
cap.release()
cv2.destroyAlWindows()    
 
    
 
    
 #yellow== 20,45,55,164,125,255
   