import cv2
import constants
import sender
import numpy as np
from io import BytesIO


video_cap = cv2.VideoCapture(0)
client_sender = sender.Sender(('10.1.10.213', 60000))

success, frame = video_cap.read()
scaled_frame = frame.resize(100, 100)

bytes_stream = BytesIO()
np.save(bytes_stream, scaled_frame)
print(len(bytes_stream.getvalue()))


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