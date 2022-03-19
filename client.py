import cv2
import constants
import sender


video_cap = cv2.VideoCapture(0)
client_sender = sender.Sender()


while True:

    success, frame = video_cap.read()

    if not success:
        print("Unable to fetch video frame.")
        client_sender.close_socket()
        break

    scaled_frame = frame.resize(100, 100)

    # Send frame accross client_sender
    client_sender.send_img(scaled_frame)


client_sender.close_socket()