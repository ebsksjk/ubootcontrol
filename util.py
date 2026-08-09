import socket
import struct

class Command:
    def __init__(self, req):
        self.request = req


class LAN_GET_SERIAL_NUMBER(Command):
    def __init__(self):
        super().__init__(bytes([0x04,0x00,0x10,0x00]))

    def make_request(self, ip, port, sock) -> int:
        sock.sendto(self.request, (ip, port))
        data = sock.recv(4096)
        res = struct.unpack("<cccci", data)

        return res[4]

class LAN_X_GET_VERSION(Command):
    def __init__(self):
        super().__init__(bytes([0x07,0x00,0x40,0x00,0x21,0x21,0x00]))

    def make_request(self, ip, port, sock):
        sock.sendto(self.request, (ip, port))
        data = sock.recv(1024)
        res = struct.unpack("<9c", data)
        return res

class LAN_X_GET_STATUS(Command):
    def __init__(self):
        super().__init__(bytes([0x07,0x00,0x40,0x00,0x21,0x24,0x05]))

    def make_request(self, ip, port, sock):
        sock.sendto(self.request, (ip, port))
        data = sock.recv(1024)

        return data
        res = struct.unpack("<9c", data)
        return res

class LAN_X_SET_TRACK_POWER_OFF(Command):
    def __init__(self):
        super().__init__(bytes([0x07,0x00,0x40,0x00,0x21,0x80,0xa1]))

    def make_request(self, ip, port, sock):
        sock.sendto(self.request, (ip, port))
        data = sock.recv(1024)

        return data
        res = struct.unpack("<9c", data)
        return res
