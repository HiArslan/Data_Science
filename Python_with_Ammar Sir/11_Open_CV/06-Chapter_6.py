# Reading a video
import cv2 as cv

cap = cv.VideoCapture("Resources/Video.mp4")

# indicators
if (cap.isOpened() == False): # This if will tell us if there will be any error in uploading our video
    print("Error in uploading the video")

# Reading and playing video

while(cap.isOpened()): # We use while loop to play our video
    ret , frame = cap.read() # If file/video is opened then return(ret) captured video and we save it in frame variable
    if ret==True: # When if will be true our video will be played
        cv.imshow("Video" , frame)
        if cv.waitKey(1) & 0xFF == ord('q') : # Means when video will be played we will press q to stop it or to break while loop
            break
    else:
        break
cap.release()
cv.destroyAllWindows()