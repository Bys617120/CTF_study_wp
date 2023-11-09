# jpg爆破宽

import os
import struct
output_dir = "output"

os.makedirs(output_dir, exist_ok=True)
filename = "misc35.jpg"
with open(filename, 'rb') as f:
    all_b = f.read()

    for i in range(901, 1200):
        name = os.path.join(output_dir, str(i) + ".jpg")
        f1 = open(name, "wb")
        im = all_b[:159] + struct.pack('>h', i) + all_b[161:]
        f1.write(im)
        f1.close()
