import socket
# SERVER ADDRESS AND PORT
#HOST_ADDRESS = ("10.1.10.213", 67000)
HOST_ADDRESS = (str(socket.gethostbyname(socket.gethostname())), 60000)
SOURCE_ADDRESS = ("10.1.10.100", 25570)