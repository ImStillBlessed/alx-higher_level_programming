#!/usr/bin/python3
"""
Author:
    Oigbochie Blessed
"""


import sys


def print_metrics(total_size, status_codes):
    """
    This script reads lines from stdin, parses the relevant information,
        and computes metrics. It prints the metrics every 10 lines
        and upon a keyboard interruption (CTRL + C).
    Args:
        total_size
        status_codes
    """
    print("File size: {:d}".format(total_size))
    for code, count in sorted(status_codes.items()):
        if count > 0:
            print("{:d}: {:d}".format(code, count))


total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

try:
    for line in sys.stdin:
        line_count += 1
        elements = line.split(" ")
        if len(elements) > 2:
            try:
                status_code = int(elements[-2])
                file_size = int(elements[-1])
                total_size += file_size
                if status_code in status_codes:
                    status_codes[status_code] += 1
            except ValueError:
                pass

        if line_count % 10 == 0:
            print_metrics(total_size, status_codes)

except KeyboardInterrupt:
    print_metrics(total_size, status_codes)
    raise
