# Convert image into black and white image

import cv2 as cv
import numpy as np
img = cv.imread("Resources/pexels-alex-qian-2343468.jpg")
img = cv.resize(img , (800,600))
gray = cv.cvtColor(img , cv.COLOR_RGBA2GRAY)
(thresh , binary) = cv.threshold(gray , 127 , 255 , cv.THRESH_BINARY)
cv.imshow("Original Image",img)
cv.imshow("Gray Image",gray)
cv.imshow("Black & White Image",binary)
cv.waitKey(0)
cv.destroyAllWindows()