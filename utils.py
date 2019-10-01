from structs.header import Header
from structs.record import Record

def parseFile(fin):
    # Read the header section.
    fileInfo = Header(fin.read(4), fin.read(1), fin.read(4))
    
    # As per README, parse records using information from header
    records = []
    for _ in range(fileInfo.total_records):
        # Read the record type, Unix timestamp, and user ID.
        record = Record(fin.read(1), fin.read(4), fin.read(8))

        # For record types of 0 or 1, read the amount in dollars.
        if record.category == 0 or record.category == 1:
            record.set_amount_in_dollars(fin.read(8))

        # Add record to list of records.
        records.append(record)

    # Return the parsed data.
    return records