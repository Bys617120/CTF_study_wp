import binascii

import struct

crcbp = open("misc33.png", 'rb').read()
for i in range(4000):
    for j in range(4000):
        data = crcbp[12:16] + struct.pack('>i', i) + struct.pack('>i', j) + crcbp[24:29]
        crc32 = binascii.crc32(data) & 0xffffffff
        if crc32 == 0x5255A798:  # 根据crc校验修改
            print(i, j)
            print("hex", hex(i), hex(j))
            # 0x76ec1e40 -> 0xec9ccbc6
