import cv2 as cv

capture=cv.VideoCapture('Resources/Videos/dog.mp4')

while True:
    isTrue,frame=capture.read() #captures the video frames by frame, isTrue is a boolean which checks whether the frame has captured or not
    cv.imshow('Video',frame)  # shows the frames 
    
    if cv.waitKey(20) & 0xFF==ord('d'):  # exits on pressing 20 or d
        break;
capture.release()
cv.destroyAllWindows()