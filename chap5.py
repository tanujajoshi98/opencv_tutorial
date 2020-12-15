# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 10:45:40 2020

@author: acer
"""
#................Warp  Perspective.....................


import cv2 
import numpy as np

img = cv2.imread("cards.png")

width,height = 250,350
pts1 = np.float32([[130,12],[244,44],[88 ,168],[201, 199]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

matrix= cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))


cv2.imshow("Image",img)

cv2.imshow("ImageWarp",imgOutput)
cv2.waitKey(0)





#....chk the function.......

#130,12   244 44  88 168  201 199