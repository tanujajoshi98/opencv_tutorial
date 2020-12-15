

#.......Face detection......

import cv2


faceCascade=cv2.CascadeClassifier ("haarcascades/haarcascade_frontalface_default.xml")
img = cv2.imread("lena.jpg")
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray,1.1,4)    #1.1==scale   4== minimum neighbours

#put rectangles around the face detected

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)


cv2.imshow("Iamge",img)





cv2.waitKey(0)
