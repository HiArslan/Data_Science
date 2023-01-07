## Greyscale conversion of  image 
# Importing libraries 
import cv2 as cv
import numpy as np # numpy is used to resize pics and videos
img = cv.imread("Resources/pexels-alex-qian-2343468.jpg")
# Resizing image
img = cv.resize(img , (800,600)) # 800 * 600 is the new size of image
# conversion
gray_img = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
#display code
cv.imshow("Pehli tasveer" , img) # Unsize image
cv.imshow("Gray tasveer" , gray_img) # Grey image
#delay code
cv.waitKey(0)
cv.destroyAllWindows() # closes all windows
