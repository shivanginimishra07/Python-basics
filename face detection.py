# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 12:34:44 2021

@author: itssh
"""
import cv2
import sys
imagepath=sys.argv[1]
cascPath="haarcascade_frontalface_default.xml"
face_cascade= cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
image=cv2.imread(imagepath)
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
faces=face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.2,
    minNeighbors=5,
    minSize=(30,30)
    )
print("Found {0} faces".format(len(faces)))
for(x,y,w,h) in faces:
    cv2.rectangle(image, (x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow("Faces found",image)
    cv2.waitKey(0)
    $ python face_detect.py abba.png