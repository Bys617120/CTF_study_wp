import os
import zlib
import struct

filename = "misc34.png"
output_dir = "output"

# 创建输出目录，如果它还不存在的话
os.makedirs(output_dir, exist_ok=True)

with open(filename, 'rb') as f:
    all_b = f.read()
    for i in range(901,1200):
        # 在文件名前添加输出目录的路径
        name = os.path.join(output_dir, str(i) + ".png")
        with open(name,"wb") as f1:
            im = all_b[:16]+struct.pack('>i',i)+all_b[20:]
            f1.write(im)
