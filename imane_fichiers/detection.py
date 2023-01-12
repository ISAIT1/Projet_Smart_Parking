from easyocr import Reader #library responsable de la lecture des chiffres (sur les capture de matricules)
import cv2  #c'est pour appeler la bibliothèque de opencv
from cv2 import VideoWriter #bibliothèque pour les video
from cv2 import VideoWriter_fourcc  #bibliothèque pour les video


camera = cv2.VideoCapture(0) #il s'agit d'ouvrir la caméra numéro 1 c'est la caméra du pc (car le 1er numéro qu'on commence avec est 0,comme pour les tableaux, qui désigne la 1ère caméra)

video = VideoWriter('Vidéo.avi', VideoWriter_fourcc(*'MP42'), 25.0, (640,480)) #code pour créer un fichier de la video avec ses dimensions

# while(camera.isOpened()):
while(True):

    ret, image = camera.read()

    # if ret==True: #si caméra est active

    cv2.imshow('Matricule à capturer', image) #visualiser la caméra

    

    if cv2.waitKey(1) & 0xFF == ord('b'): #pour fermer la caméra: on donne une valeur 1s par exemple pour stopper la caméra lorqu'on clique sur le boutton b du clavier
            break  #break pour fermer le running du code

    cv2.imwrite("C://Users/Destock/SmartParking_projet/capturematricule.png", image)  #enregistrer l'image sous un dossier
    video.write(image) #code pour enregister une video (recording) nommé video.avi   

camera.release()
video.release()

car = cv2.imread('car1.jpg')
car = cv2.resize(car, (800, 600))
gray = cv2.cvtColor(car, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5,5), 0)
edged = cv2.Canny(blur, 10, 200)
contours, _ = cv2.findContours(edged, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours = sorted(contours, key = cv2.contourArea, reverse = True)

for c in contours:
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02 * peri, True)
    if len(approx) == 4:
        n_plate_cnt = approx  #le contour de la plaque
        break

(x, y, w, h) = cv2.boundingRect(n_plate_cnt) #encadrer la plaque retrouvée 
license_plate = gray[y:y + h, x:x + w]

reader = Reader(['en'],gpu=False,verbose=False) #lire le contenu de ce qui est encadré, la langue choisit est english pour arabe faire 'ar'
detection = reader.readtext(license_plate) #lire le text de la plaque
print(detection)  #afficher le text de la plaque lu

if len(detection) == 0:
    text = "Impossible de lire le texte affiché sur la plque de matricule"
    cv2.putText(image, text, (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 3)
    cv2.imshow('Image', image)
    cv2.waitKey(0)
else:
    cv2.drawContours(image, [n_plate_cnt], -1, (0, 255, 0), 3)
    text = f"{detection[0][1]} {detection[0][2] * 100:.2f}%"
    cv2.putText(image, text, (x, y - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2) #mettre le text lu sur l'image mm
    # display the license plate and the output image
    print(text)
    cv2.imshow('license plate', license_plate)
    cv2.imshow('Image', image)
    cv2.waitKey(0)