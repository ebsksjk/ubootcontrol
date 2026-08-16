import socket
from time import sleep, time
import util
import listener
from datetime import datetime
import sys, signal

def signal_handler(signal, frame):
    print("logging off :3")
    # log off :3
    req = util.LAN_LOGOFF()
    req.make_request(IP, PORT, sock)
    sys.exit(0)



IP = "192.168.0.111"
PORT = 21105

signal.signal(signal.SIGINT, signal_handler)

print("UDP target IP:", IP)
print("UDP target port:", PORT)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # ipv4+UDP

broadcast_listener = listener.broadcast_listener()
broadcast_listener.start()

req = util.LAN_GET_SERIAL_NUMBER()
response = req.make_request(IP, PORT, sock)
print(f"serial: {response}")

req = util.LAN_X_GET_VERSION()
response = req.make_request(IP, PORT, sock)
print(f"version: {response}")

req = util.LAN_SYSTEMSTATE_GETDATA()
response = req.make_request(IP, PORT, sock)
print(f"system state: {response}")

while True:
    req = util.LAN_X_GET_STATUS()
    response = req.make_request(IP, PORT, sock)
    print(f"{datetime.now()} - status: {response}")
    # wait for 30 seconds before sending the next request (a client needs to send a request every minute)
    sleep(30) 

