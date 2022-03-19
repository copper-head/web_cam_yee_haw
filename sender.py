import socket
import numpy as np
import constants
from io import BytesIO

class Sender:

    def __init__(self, remote_address):

        self._socket = socket.create_connection(remote_address, source_address=constants.SOURCE_ADDRESS)
        

    '''
    async def parse(self):
        with self.conn as conn:
            print(f"Connected by {self.addr}")
            while True:
                self.data = conn.recv(1024)
                if self.data is not 
    '''

    def send_img(self, frame):        
        
        # Create a byte stream to send data
        bytes_stream = BytesIO()
        np.save(bytes_stream, frame)
        self._socket.sendall(bytes_stream.getvalue())
    
    # Close socket
    def close_socket(self):

        self._socket.close()
