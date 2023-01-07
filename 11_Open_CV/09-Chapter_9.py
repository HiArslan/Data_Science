# How to give webcam as input in python

# step-1 import libraries
import cv2 as cv
import numpy as np
cam = cv.VideoCapture(1) # This 0,1,2,3... menas numbers of webcames you are using in my case my PC camera is not right so i'm using IV_cam app 
                         # as webcame whose input is 1    

# read until the end
while (cam.isOpened)():
    # capture frame by frame
    (ret , frame) = cam.read()
    if ret==True: 
        # To display cam 
        cv.imshow("Frame" , frame)
        # To quit cam with q
        if cv.waitKey(1) & 0xFF == ord('q') :
            break
    else: # If camera is not present
        break

cam.release()
cv.destroyAllWindows()


