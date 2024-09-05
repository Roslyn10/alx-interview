#!/usr/bin/python3
"""A function that checks for valid UTF-8 encoding"""


def validUTF8(data):
    """
    A function that determines if a data set represents valid UTF-8 encoding
    """
    bytes_to_process = 0

    mask_1_byte = 0b10000000
    mask_2_bytes = 0b11100000
    mask_3_bytes = 0b11110000
    mask_4_bytes = 0b11111000
    mask_continuation = 0b11000000

    for byte in data:
        byte = byte & 0xFF

        if bytes_to_process == 0:
            if (byte & mask_1_byte) == 0b00000000:
                continue
            elif (byte & mask_2_bytes) == 0b11000000:
                bytes_to_process = 1
            elif (byte & mask_3_bytes) == 0b11100000:
                bytes_to_process = 2
            elif (byte & mask_4_bytes) == 0b11110000:
                bytes_to_process = 3
            else:
                return False
        else:
            if (byte & mask_continuation) != 0b10000000:
                return False
            bytes_to_process -= 1

    return bytes_to_process == 0
