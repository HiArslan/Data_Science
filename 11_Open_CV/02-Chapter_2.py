## Resizing the image 
# Importing libraries 
import cv2 as cv
import numpy as np # numpy is used to resize pics and videos
img = cv.imread("Resources/pexels-alex-qian-2343468.jpg")
# Resizing image
img1 = cv.resize(img , (800,600)) # 800 * 600 is the new size of image
cv.imshow("Pehli tasveer" , img) # Unsize image
cv.imshow("Doosri tasveer" , img1) # Resized image
cv.waitKey(0)
cv.destroyAllWindows() # closes all windows