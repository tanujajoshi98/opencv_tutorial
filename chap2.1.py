# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 20:07:33 2020

@author: acer
"""

import cv2 
import numpy as np

img = cv2.imread("lambo.jpg")
print(img.shape)

imgResize = cv2.resize(img,(400,300))    #width,height

print (imgResize.shape)
imgCropped =  img[0:200,0:100]             #height,width

cv2.imshow("image",img)

cv2.imshow("image_resized",imgResize)

cv2.imshow("img_Cropped ", imgCropped)

cv2.waitKey(0)

