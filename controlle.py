import numpy as np
import cv2

def camera_controll():
    # This will return video from the first webcam on your computer.
    cap = cv2.VideoCapture(0)

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'DIVX')
    out = cv2.VideoWriter('video.mp4', fourcc, 20.0, (640, 480))

    # loop runs if capturing has been initialized.
    while (True):
        # reads frames from a camera
        # ret checks return at each frame
        ret, frame = cap.read()

        # Converts to grayscale space, OCV reads colors as BGR
        # frame is converted to gray
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # output the frame
        out.write(frame)

        # The original input frame is shown in the window
        cv2.imshow('Original', frame)

        # The window showing the operated video stream
        cv2.imshow('frame', gray)

        # Wait for 'a' key to stop the program
        i = 1
        if cv2.waitKey(1) & 0xFF == ord('a'):
            cv2.imwrite('capture' + str(i) + '.jpg', frame)
            i += 1
            continue

        elif cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.imwrite('lastCapture.jpg', frame)
            break

    # Close the window / Release webcam
    cap.release()

    # After we release our webcam, we also release the out-out.release()

    # De-allocate any associated memory usage
    cv2.destroyAllWindows()
