## Reading an image displaying it
# Import library
import cv2 as cv
# Read images
img=cv.imread("Resources/pexels-alex-qian-2343468.jpg") # Here you have to give folder name first then slash file name
# show images
cv.imshow("Pehli Tasveer" , img)
# to delay
cv.waitKey(0)