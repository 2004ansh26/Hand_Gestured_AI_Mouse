# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 09:17:45 2024

@author: Administrator
"""

import os
import cv2
width,height=1200,720
cap=cv2.VideoCapture(0)
cap.set(3,width)
cap.set(4,height)
folderPath="Presentation"
pathImages=sorted(os.listdir(folderPath),key=len)
print(pathImages)
imageNumber=0
while True:
    success,img=cap.read()
    pathFullImage=os.path.join(folderPath,pathImages[imageNumber])
    imgCurrent=cv2.imread(pathFullImage)
    

    cv2.imshow("Video",img)
    cv2.imshow("Slides",imgCurrent)
    key=cv2.waitKey(1)
    if key==ord('q'):
        break