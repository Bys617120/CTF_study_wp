flag=""
for i in range(1,69):
    f = open("apngframe" + str(i) + ".txt")
    s = f.read()
    flag += chr(int(s.split("/")[0][6:]))
print(flag)
