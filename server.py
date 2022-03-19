import receiver
import constants

server_receiver = receiver.Receiver(constants.HOST_ADDRESS)

if __name__ == "__main__":

    while True:

        server_receiver.get_frames()