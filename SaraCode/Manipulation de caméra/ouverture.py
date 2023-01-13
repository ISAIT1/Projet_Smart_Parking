import cv2

#----- Ouverture de camera ------
camera=cv2.VideoCapture(0)
img_counter = 0
while True:
    ret , video = camera.read()
    #new_cam = cv2.resize(video,(300,200))
    cv2.imshow('SaraCam', video)
    k=cv2.waitKey(1)
