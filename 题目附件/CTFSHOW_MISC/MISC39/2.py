s="00111000001011001100100011000010111001000000010000000100100101010011011000111100111010011010011001001100110001101000110100101000110010011101100100000111010011010100110110010011000111001101110001101001001100110000111101000110001101000111010011100001111010011111001011100101010001100000010"
flag=""
for i in range(41):
    flag += chr(int(s[7*i:7*(i+1)],2))
print(flag)
