import binascii
import struct


def calculate_crc(chunk_type, data):
    return binascii.crc32(chunk_type + data) & 0xffffffff


def get_chunks(png_file):
    png_file.seek(8)  # Skip the PNG signature

    while True:
        chunk_length = struct.unpack('!I', png_file.read(4))[0]
        chunk_type = png_file.read(4)
        data = png_file.read(chunk_length)
        crc = struct.unpack('!I', png_file.read(4))[0]

        yield chunk_type, data, crc

        if chunk_type == b'IEND':
            break


def check_crc(png_file):
    incorrect_crcs = []

    for chunk_type, data, crc in get_chunks(png_file):
        calculated_crc = calculate_crc(chunk_type, data)

        if calculated_crc != crc and chunk_type == b'IDAT':
            incorrect_crcs.append(hex(crc)[2:])  # Convert to hex and remove "0x"

    return incorrect_crcs


def crc_to_ascii(crc_values):
    ascii_values = []

    for crc in crc_values:
        # Start from the third character, and take every two characters as a hex number
        for i in range(0, len(crc), 2):
            hex_value = crc[i:i + 2]
            ascii_values.append(chr(int(hex_value, 16)))

    return ''.join(ascii_values)


with open('misc43.png', 'rb') as f:
    incorrect_crcs = check_crc(f)
    ascii_values = crc_to_ascii(incorrect_crcs)

print(ascii_values)
