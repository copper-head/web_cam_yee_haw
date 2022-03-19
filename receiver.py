import numpy as np
import socket
from collections import deque
import constants

class Receiver:

    def __init__(self):
        
        # This will eventually hold data
        self.deque = deque()

        self.receiver = socket.socket()
        self.receiver.bind(("10.1.10.213", 60000))
        print(constants.HOST_ADDRESS)
        self.receiver.listen()
        self.sock, self.remote_addr = self.receiver.accept()
    
    def get_frames(self):

        while True:
            print("waiting for data...")
            data = self.receiver.recv(1024)
            print(data)


