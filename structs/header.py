import struct

class Header(object):
    def __init__(self, magic_string, version_number, total_records):
        self.magic_string = magic_string
        # get integer representation of version number unicode char
        self.version = ord(version_number)
        # unpack the buffer
        self.total_records = struct.unpack("!I", total_records)[0]