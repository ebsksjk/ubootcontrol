import socket
import struct

class Command:
    def __init__(self, req):
        self.request = req

    def make_request(self, ip, port, sock, struct_format=None):
        sock.sendto(self.request, (ip, port))
        data = sock.recv(1024)
        if struct_format:
            return struct.unpack(struct_format, data)
        return data
    def send_request(self, ip, port, sock):
        sock.sendto(self.request, (ip, port))

class LAN_GET_SERIAL_NUMBER(Command):
    def __init__(self):
        super().__init__(bytes([0x04,0x00,0x10,0x00]))

    def make_request(self, ip, port, sock) -> int:
        data = super().make_request(ip, port, sock, struct_format="<cccci")
        return data

class LAN_X_GET_VERSION(Command):
    def __init__(self):
        super().__init__(bytes([0x07,0x00,0x40,0x00,0x21,0x21,0x00]))

    def make_request(self, ip, port, sock):
        data = super().make_request(ip, port, sock, struct_format="<9c")
        return data

class LAN_X_GET_STATUS(Command):
    def __init__(self):
        super().__init__(bytes([0x07,0x00,0x40,0x00,0x21,0x24,0x05]))

    def make_request(self, ip, port, sock):
        # return data for now. i don't know how to unpack it yet
        data = super().make_request(ip, port, sock, struct_format=None)
        return data

class LAN_X_SET_TRACK_POWER_OFF(Command):
    def __init__(self):
        super().__init__(bytes([0x07,0x00,0x40,0x00,0x21,0x80,0xa1]))

    def make_request(self, ip, port, sock):
        # return data for now. i don't know how to unpack it yet
        data = super().make_request(ip, port, sock, struct_format=None)
        return data

class LAN_LOGOFF(Command):
    def __init__(self):
        super().__init__(bytes([0x04,0x00,0x30,0x00]))

    def make_request(self, ip, port, sock):
        # this function does not return anything. just send it
        super().send_request(ip, port, sock)

class LAN_SYSTEMSTATE_GETDATA(Command):
    def __init__(self):
        super().__init__(bytes([0x04,0x00,0x85,0x00]))

    def make_request(self, ip, port, sock):
        # return data for now. i don't know how to unpack it yet
        #struct should be:
        # <cccchhhhHHBBBB

        data = super().make_request(ip, port, sock, struct_format="<cccchhhhHHBBBB")
        return data

class LAN_SET_BROADCASTFLAGS(Command):
    def __init__(self):
        # flags is a 32-bit integer (little endian)
        # for the sake of testing, we will just do them by hand
        flag = 0x00000001 | 0x00010000
        flags_bytes = flag.to_bytes(4, byteorder='little')
        super().__init__(bytes([0x08,0x00,0x50,0x00]) + flags_bytes)

    def make_request(self, ip, port, sock):
        # this function does not return anything. just send it
        super().send_request(ip, port, sock)