# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 20:40:40 2020

@author: acer
"""

import cv2
import numpy as np 


img = np.zeros((512,512,3),np.uint8)
print (img.shape) 
#img[200:300,100:150]=255,255,255      #height, width


img[:]=0,0,0
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)       #start point , end , color , thickness (do no use ":")
cv2.rectangle (img,(0,0),(250,300),(255,0,0),2)      #instead of 2 write cv2.FILLED for complete shaded region 

cv2.circle(img , (400,50),35,(0,0,255),5)      # 400 -->width(x-axis), 50 y axis -->height 

#put text in image 

cv2.putText(img,"  OPENCV  ",(300 ,150),cv2.FONT_HERSHEY_COMPLEX,1, (150,0,0),3)   # 300->X axis , 200 -> Y axis 1-->scale 


cv2.imshow("image ", img)


cv2.waitKey (0)
 