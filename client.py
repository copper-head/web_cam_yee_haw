import cv2
import constants
import sender
import numpy as np



client_sender = sender.Sender(('10.1.10.100', 60000))
video_cap = cv2.VideoCapture(0)

while True:

    success, frame = video_cap.read()

    if not success:
        print("Unable to fetch video frame.")
        client_sender.close_socket()
        break
    
    client_sender.send_img(frame)

    cv2.imshow("frame", frame)

    if cv2.waitKey(1) == ord('q'):
        break



client_sender.close_socket()