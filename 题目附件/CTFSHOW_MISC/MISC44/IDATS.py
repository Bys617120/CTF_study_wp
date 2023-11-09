import png
import zlib

def fix_crc(png_file, output_file):
    reader = png.Reader(png_file)
    chunks = list(reader.chunks())

    new_chunks = []
    for chunk in chunks:
        if chunk[0] == b'IDAT':
            data = chunk[1]
            correct_crc = zlib.crc32(data) & 0xffffffff
            new_chunks.append((chunk[0], data, correct_crc))
        else:
            new_chunks.append(chunk)

    with open(output_file, 'wb') as f:
        png.write_chunks(f, new_chunks)

fix_crc('m', 'output.png')
