# Writing videos from cam
import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

#writing format , codec(Convert something) , video writer object and file output
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# fourcc('M','J','P','G') is a motion-jpeg codec etc
# fps Framerate of the created video stream (10 in our case) if we will increase no of frames per sec our video will be smooth
# frameSize Size of the video frames. (frame_width and height)
# isColor If it is not zero, the encoder will expect and encode color frames, otherwise it will work with grayscale frames
# when we will convert cam into b&w or gray then we have to give the command iscolor=False

out = cv.VideoWriter("Resources/Cam_video.avi" , cv.VideoWriter_fourcc('M' , 'J' , 'P' , 'G') , 30 , (frame_width , frame_height))

while (True) :

    (ret , frame) = cap.read()
    # gray_frame = cv.cvtColor(frame , cv.COLOR_BGR2GRAY) # Converting into grey
    # To show video 
    if ret==True: 
        out.write(frame)
        cv.imshow("Video" , frame)
        # To quit video with q
        if cv.waitKey(1) & 0xFF == ord('q') :
            break
    else:
        break

cap.release()
out.release()
cv.destroyAllWindows()