# -*- coding: utf-8 -*-

import cv2
import numpy as np 

img = cv2.imread("lena.jpg")

kernal = np.ones ((5,5),np.uint8) 
                  # convert to grey sca;e 

imgGray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur= cv2.GaussianBlur(imgGray,(7,7),0)

#edge detector 

imgCanny = cv2.Canny (img,100,100)
imgDialation = cv2.dilate(imgCanny,kernal, iterations = 1 ) 
imgEroded = cv2.erode(imgDialation,kernal,iterations = 1)

cv2.imshow("gray_image",imgGray)
cv2.imshow("blur_image",imgBlur)
cv2.imshow("canny_image",imgCanny)
cv2.imshow("dilate_image",imgDialation)
cv2.imshow("erode_image",imgEroded)
       
cv2.waitKey(0)