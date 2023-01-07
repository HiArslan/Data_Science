# Saving an image or writing images

import cv2 as cv
from cv2 import imwrite
import numpy as np
img = cv.imread("Resources/pexels-alex-qian-2343468.jpg")
img = cv.resize(img , (800,600))
gray = cv.cvtColor(img , cv.COLOR_RGBA2GRAY)
(thresh , binary) = cv.threshold(gray , 127 , 255 , cv.THRESH_BINARY)
imwrite("Resources/Gray_Image.png" , gray) # Save or write images
imwrite("Resources/BW_Image.png" , binary)
cv.imshow("Original Image" , gray)
cv.waitKey(0)
cv.destroyAllWindows()