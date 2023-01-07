# Converting a video into gray/black video
import cv2 as cv
from cv2 import cvtColor

cap = cv.VideoCapture("Resources/Video.mp4")

while (True) :
    (ret , frame) = cap.read()
    gray_frame = cv.cvtColor(frame , cv.COLOR_BGR2GRAY) # Converting into grey
    (thresh , binary) = cv.threshold(gray_frame , 127 , 255 , cv.THRESH_BINARY ) # converting into black and white
    # To show video 
    if ret==True: 
        cv.imshow("Video" , frame) 
        cv.imshow("Video" , gray_frame)
        cv.imshow("Video" , binary)
        # To quit video with q
        if cv.waitKey(1) & 0xFF == ord('q') :
            break
    else:
        break

cap.release()
cv.destroyAllWindows()