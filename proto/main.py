#!/usr/bin/env python
import sys
from structs.report import Report
from utils import parseFile


# ################ #
#       Main       #
# ################ #
def main():
    # Get cli arguments count
    argc = len(sys.argv)

    # Handle incorrect number of arguments.
    if argc != 2:
        print("Usage: python %s [file]" % sys.argv[0])
        return

    # Set the file name.
    file_name = sys.argv[1]

    # Open the file as an input stream and parse the file for the records.
    with open(file_name, 'rb') as fin:
        records = parseFile(fin)

    # Once records are parsed, iterate through each record and process it.
    user_id = 2456938384156277127
    answers = Report()
    for record in records:
        # 0x00: Debit
        if record.category == 0:
            answers.debits += record.amount_in_dollars
            if record.user_id == user_id:
                print(user_id, record.amount_in_dollars)
                answers.balance_of_user -= record.amount_in_dollars
        # 0x01: Credit
        if record.category == 1:
            answers.credits += record.amount_in_dollars
            if record.user_id == user_id:
                print(user_id, record.amount_in_dollars)
                answers.balance_of_user += record.amount_in_dollars
        # 0x02: StartAutopay
        if record.category == 2:
            answers.autopays_started += 1
        # 0x03: EndAutopay
        if record.category == 3:
            answers.autopays_ended += 1

    # Print the answers.
    print("The total amount in dollars of debit is $%.2f." % answers.debits)
    print("The total amount in dollars of debit is $%.2f." % answers.credits)
    print("%d autopays were started." % answers.autopays_started)
    print("%d autopays were ended." % answers.autopays_ended)
    print("The balance of user ID %d is $%.2f." % (user_id, answers.balance_of_user))

if __name__ == '__main__':
    main()
