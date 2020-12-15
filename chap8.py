# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 11:11:55 2020

@author: acer
"""

#.......... counters and shape detection .........

import cv2
import numpy as np 



def getContours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area=cv2.contourArea(cnt)
        print(area)
        if area>500:
            cv2.drawContours(imgContour,cnt,-1,(255,0,0),3)   #-1==contour index(draw all contours ,color = blue , 3= thickness)    
            peri = cv2.arcLength(cnt,True)
            #print(peri)
            approx=cv2.approxPolyDP(cnt,0.02*peri,True)
            print(len(approx))
            objCor = len(approx)     #create object corner to draw a line between them 
            x, y, w, h = cv2.boundingRect(approx)
            
            if objCor==3: objectType="Tri"
            elif objCor == 4:
                aspRatio=w/float(h)
                if aspRatio>0.95 and aspRatio<1.05: objectType="Square"
                else:objectType="Rectangle"
            elif objCor>4: objectType= "Circle"
                
            else:objectType="None"
        
            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2)    #bounding boxes around each of the shape 
            cv2.putText(imgContour,objectType,(x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),2)
            
            
            
img = cv2.imread("shapes2.png")
imgContour=img.copy()
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur= cv2.GaussianBlur(imgGray,(7,7),1)     #here 1= sigma, higher value of sigma the more blur pic 

##........Edge Detection  (Canny edge detection ) ......

imgCanny=cv2.Canny(imgBlur,50,50)
getContours(imgCanny)


imgBlank= np.zeros_like(img)

cv2.imshow("image", img )
cv2.imshow("imageGray", imgGray )
cv2.imshow("imageBlur", imgBlur )
cv2.imshow("imageCanny", imgCanny )
cv2.imshow("imageBlank", imgBlank)
cv2.imshow("imageContour", imgContour)
cv2.waitKey(0)