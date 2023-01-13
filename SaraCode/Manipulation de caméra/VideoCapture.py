import cv2 
from cv2 import VideoWriter
from cv2 import VideoWriter_fourcc

#-------- Ouvrir la caméra -------
webcam=cv2.VideoCapture(0)

#---- open output video file stream
video = VideoWriter('webcam.avi', VideoWriter_fourcc(*'MP42'),25.0, (640, 480))

#---------main loop ------
while(True):
    #-- ----get teh frame from the webcam
    ret, frame = webcam.read()
    if webcam:
    #------ display current frame
       cv2.imshow('webcam',frame)

       #------write frame to the video file---------
       video.write(frame)

    #------ escape condition 
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

#-------- Clean ups--------
cv2.destroyAllWindows()
#----------- release web camera stream
webcam.release()
#release video putput file stream
video.release()
