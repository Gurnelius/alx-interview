#!/usr/bin/python3
'''
This script reads stdin line by line and computes metrics
'''


import sys
import signal


def print_msg(dict_sc, total_file_size):
    """
    Method to print statistics
    Args:
        dict_sc: dict of status codes
        total_file_size: total of the file sizes
    Returns:
        Nothing
    """
    print("File size: {}".format(total_file_size))
    for key in sorted(dict_sc.keys()):
        if dict_sc[key] > 0:
            print("{}: {}".format(key, dict_sc[key]))


def signal_handler(sig, frame):
    """
    Handle the keyboard interrupt (CTRL + C) and print stats.
    """
    print_msg(dict_sc, total_file_size)
    sys.exit(0)


# Initialize variables
total_file_size = 0
counter = 0
dict_sc = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

# Register the signal handler for keyboard interruption
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) < 9:
            continue

        try:
            file_size = int(parts[-1])
            status_code = parts[-2]
        except (ValueError, IndexError):
            continue

        if status_code in dict_sc:
            dict_sc[status_code] += 1
            total_file_size += file_size
            counter += 1

        if counter == 10:
            print_msg(dict_sc, total_file_size)
            counter = 0

finally:
    print_msg(dict_sc, total_file_size)
