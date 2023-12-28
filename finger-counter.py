import cv2 
import mediapipe as mp
import time 
import handtrackingmodule as htm
import numpy as np
import os
wcam , hcam = 640 , 480
cap = cv2.VideoCapture(0)
cap.set(3 , wcam)
cap.set(4 , hcam)
ptime =0

folderpath = "finger images"
myList=os.listdir(folderpath)
print(myList)
while True :
    success , img = cap.read()
    ctime = time.time()
    fps=1/(ctime-ptime)
    ptime=ctime
    cv2.putText(img, f'FPS:{int(fps)}', (20, 40), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 255, 0), 3)
    cv2.imshow("Image" , img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
