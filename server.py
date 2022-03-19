import cv2
import receiver

server_reciever = receiver.Receiver()

if __name__ == "__main__":

    while True:

        # GET_FRAMES
        frame = "frame here"

        # Display image
        cv2.imshow("image", frame)

        #if cv2.waitKey(1) & 0xFF == ord('q'):
        #  break