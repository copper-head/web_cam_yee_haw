import numpy as np
import cv2
import socket
import asyncio
from collections import deque
import constants

class Receiver:

    def __init__(self):
        
        # This will eventually hold data
        self.deque = deque()

        self.receiver = socket.socket()
        self.receiver.bind(constants.HOST_ADDRESS)
        #self.receiver.connect(local_address)
        self.receiver.listen()
        self.sock, self.remote_addr = self.receiver.accept()
    
    def get_frames(self):

        while True:
            print("waiting for data...")
            data = self.receiver.recv(1024)
            print(data)


