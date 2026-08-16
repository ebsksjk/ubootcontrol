import socket
import struct
import util
import threading

class broadcast_listener:
    def __init__(self):
        self.broadcast_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # ipv4+UDP
        self.broadcast_sock.bind(('', 22999)) # hehe. 229

        # listen for broadcasts in a separate thread
        self.listener_thread = threading.Thread(target=self.listen_for_broadcasts, args=(self.broadcast_sock,), daemon=True)

    def start(self):
        # set up broadcast socket by sending a request to the device to enable broadcasts
        req = util.LAN_SET_BROADCASTFLAGS()
        req.make_request("129.168.0.111", 21105, self.broadcast_sock)

        self.listener_thread.start()

    def listen_for_broadcasts(self, socket):
        while True:
            data, addr = socket.recvfrom(1024)
            if not data: break
            print(f"received a packet from {addr}")
            if(data):
                print("raw data:")
                for b in data:
                    print(f"{b:02x}", end=" ")
                print()  # Print a newline after each packet
