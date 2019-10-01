import struct

class Record(object):
    def __init__(self, record_type, unix_timestamp, user_id):
        #unpack buffer based on string format
        self.unix_timestamp   = struct.unpack("!I", unix_timestamp)[0]
        self.user_id          = struct.unpack("!Q", user_id)[0]
        # get integer representation of record type
        self.category = ord(record_type)

    def set_amount_in_dollars(self, amount_in_dollars):
        self.amount_in_dollars = struct.unpack("!d", amount_in_dollars)[0]
