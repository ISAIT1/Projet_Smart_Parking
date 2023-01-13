import cv2

#----- Ouverture de camera ------
camera=cv2.VideoCapture(0)
img_counter = 0
while True:
    ret , video = camera.read()
    #new_cam = cv2.resize(video,(300,200)) // Redimensionner la fenêtre 
    cv2.imshow('SaraCam', video)
    k=cv2.waitKey(1)
#------- Fermer la fenetre de camera-------
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

    elif k%256 == 32:
        img_name="opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, video)
        print("screenshot taken")
        img_counter+=1
