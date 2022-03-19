import receiver
import constants

server_receiver = receiver.Receiver()

if __name__ == "__main__":

    while True:

        server_receiver.get_frames()