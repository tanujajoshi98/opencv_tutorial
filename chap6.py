# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 11:05:58 2020

@author: acer
"""
#................Joining Images ..............

import cv2 
import numpy as np 

img = cv2.imread("lena.jpg")

#stack img on itself

imgHor =np.hstack((img,img))
imgVer = np.vstack ((img,img))




cv2.imshow("Image", img )
cv2.imshow("Image_horizontal", imgHor )
cv2.imshow("Img_Vertical",imgVer)
cv2.waitKey(0)