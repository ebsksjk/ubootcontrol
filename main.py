import socket
import struct

import util

IP = "192.168.0.111"
PORT = 21105

print("UDP target IP:", IP)
print("UDP target port:", PORT)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # ipv4+UDP

req = util.LAN_GET_SERIAL_NUMBER()
response = req.make_request(IP, PORT, sock)
print(f"serial: {response}")

#req = util.LAN_X_SET_TRACK_POWER_OFF()
#res = req.make_request(IP, PORT, sock)
#print(res)
