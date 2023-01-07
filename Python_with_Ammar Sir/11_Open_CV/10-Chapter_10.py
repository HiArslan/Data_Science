# Converting cam into different colors

import cv2 as cv
from cv2 import imshow
from cv2 import THRESH_BINARY
import numpy as np

cam = cv.VideoCapture(1)

while (cam.isOpened()):
    (ret , frame) = cam.read()
    # Converting cam into gray
    gray_frame = cv.cvtColor(frame , cv.COLOR_BGR2GRAY) # We are connverting frames into video thats why we put frame 
                                                        # in ()
    # Converting cam into black and white
    (tresh , binary) = cv.threshold(gray_frame , 127 , 255 , cv.THRESH_BINARY )
    # Displaying original cam
    imshow("Original_Cam" , frame)
    # Displaying gray cam
    imshow("Gray_Cam" , gray_frame)
    # Displaying black and white cam
    imshow("Black and White" , binary)
    # To quit cam with q
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv.destroyAllWindows() 



