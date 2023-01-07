# Settting of camera or video
import cv2 as cv
from cv2 import imshow
import numpy as np

cam = cv.VideoCapture(0) # Here 0 is for PC camera and 1 is for Ivcam app(this app is not changeable can't change brightness etc)


cam.set(10 , 100) # 10 is the key to set brightness
cam.set(3 , 200) # 3 is width key
cam.set(4 , 480) # 4 is height key
while (True):
    (ret , frame) = cam.read()
    if ret == True :
        imshow("Original cam" , frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

cam.release()
cv.destroyAllWindows()
    
