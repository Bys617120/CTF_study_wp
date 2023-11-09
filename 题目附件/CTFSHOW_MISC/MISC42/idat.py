# 导入binascii模块，用于处理二进制和ascii数据
import binascii


# 定义一个函数，用于从png文件中提取idat块的字节数
def get_idat_bytes(png_file):
    # 以二进制模式打开png文件
    with open(png_file, "rb") as f:
        # 读取文件内容
        data = f.read()
        # 将二进制数据转换为十六进制字符串
        hex_data = binascii.hexlify(data).decode()
        # 定义一个空列表，用于存储idat块的字节数
        idat_bytes = []
        # 定义一个变量，用于记录当前的位置
        pos = 0
        # 循环遍历十六进制字符串，直到找到所有的idat块
        while True:
            # 查找idat块的标识符，即49444154
            idat_pos = hex_data.find("49444154", pos)
            # 如果没有找到，说明已经到达文件的末尾，退出循环
            if idat_pos == -1:
                break
            # 如果找到了，计算idat块的起始位置，即标识符前面的四个字节，表示块的长度
            start_pos = idat_pos - 8
            # 计算idat块的结束位置，即标识符后面的四个字节，表示块的校验和
            end_pos = idat_pos + 12
            # 截取idat块的十六进制字符串
            idat_hex = hex_data[start_pos:end_pos]
            # 将idat块的十六进制字符串转换为二进制数据
            idat_data = binascii.unhexlify(idat_hex)
            # 获取idat块的长度，即前四个字节
            idat_length = idat_data[:4]
            # 将idat块的长度添加到列表中
            idat_bytes.append(idat_length)
            # 更新当前的位置，继续查找下一个idat块
            pos = end_pos
        # 返回idat块的字节数列表
        return idat_bytes


# 定义一个函数，用于将字节数转换为ascii码
def bytes_to_ascii(bytes_list):
    # 定义一个空字符串，用于存储ascii码
    ascii_str = ""
    # 循环遍历字节数列表
    for b in bytes_list:
        # 将每个字节转换为十进制整数
        n = int.from_bytes(b, "big")
        # 将每个整数转换为ascii字符
        c = chr(n)
        # 将每个字符拼接到字符串中
        ascii_str += c
    # 返回ascii码字符串
    return ascii_str


# 定义一个png文件的路径，你可以根据你的实际情况修改
png_file = "misc42.png"
# 调用get_idat_bytes函数，从png文件中提取idat块的字节数
idat_bytes = get_idat_bytes(png_file)
# 打印idat块的字节数
print("The bytes of IDAT chunks are:")
for b in idat_bytes:
    print(b)
# 调用bytes_to_ascii函数，将idat块的字节数转换为ascii码
ascii_str = bytes_to_ascii(idat_bytes)
# 打印ascii码
print("The ASCII code of IDAT chunks is:")
print(ascii_str)
