# Converting a video into gray/black video and saving
import cv2 as cv

cap = cv.VideoCapture("Resources/Video.mp4")

#writing format , codec(Convert something) , video writer object and file output
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
out = cv.VideoWriter("Resources/Out_video.avi" , cv.VideoWriter_fourcc('M' , 'J' , 'P' , 'G') , 10 , (frame_width , frame_height) , isColor=False)

while (True) :

    (ret , frame) = cap.read()
    gray_frame = cv.cvtColor(frame , cv.COLOR_BGR2GRAY) # Converting into grey
    # To show video 
    if ret==True: 
        out.write(gray_frame)
        cv.imshow("Video" , gray_frame)
        # To quit video with q
        if cv.waitKey(1) & 0xFF == ord('q') :
            break
    else:
        break

cap.release()
out.release()
cv.destroyAllWindows()