# JPEG文件结构*

> 转载自http://www.cnblogs.com/bandy/p/4956086.html

JPEG文件由八个部分组成，每个部分的标记字节为两个，首字节固定为：0xFF，当然，准许在其前面再填充多个0xFF，以最后一个为准。下面为各部分的名称和第二个标记字节的数值，用ultraedit的16进制搜索功能可找到各部分的起始位置，在嵌入式系统中可用类似的数值匹配法定位。

段结构：段标识（FF）+段类型（D8）+段长度+段内容,段长度:2byte,包括段内容和段长度本身,不包括段标识和段类型。

### 段类型表

- **名称   标记码    说明**
- SOI     D8    文件头
- EOI     D9   文件尾
- SOF0  C0    帧开始（标准JPEG）
- SOF1  C1    同上
- DHT   C4   定义Huffman表（霍夫曼表）
- SOS   DA   扫描行开始
- DQT   DB   定义量化表
- DRI   DD   定义重新开始间隔
- APP0  E0   定义交换格式和图像识别信息
- COM   FE   注释

 

### 一、图像开始SOI(Start of Image)标记，数值0xD8

![img](https://cdn.nlark.com/yuque/0/2023/png/39298680/1698479092249-45a779ec-1ec9-4ba7-8864-d772e7a0b5cb.png)

### 二、APP0标记(Marker)，数值0xE0

#### 1、APP0长度(length)                            2byte

#### 2、标识符(identifier)                     5byte

#### 3、版本号(version)                        2byte

#### 4、X和Y的密度单位(units=0：无单位；units=1：点数/英寸；units=2：点数/厘米)                        1byte

#### 5、X方向像素密度(X density)                      2byte

#### 6、Y方向像素密度(Y density)                       2byte

#### 7、缩略图水平像素数目(thumbnail horizontal pixels)                       1byte

#### 8、缩略图垂直像素数目(thumbnail vertical pixels)                            1byte

#### 9、缩略图RGB位图(thumbnail RGB bitmap)，由前面的数值决定，取值3n，n为缩略图总像素   3n byte

![img](https://cdn.nlark.com/yuque/0/2023/png/39298680/1698479092286-4af21cdc-09c7-4961-b6ac-1d6ccd78d8fb.png)

### 三、APPn标记(Markers)，其中n=1～15，数值对应0xE1～0xEF

#### 1、APPn长度(length)

#### 2、应用细节信息(application specific information)

参考：http://www.cppblog.com/lymons/archive/2010/02/23/108266.aspx

### 四、一个或者多个量化表DQT(difine quantization table)，数值0xDB

#### 1、量化表长度(quantization table length)

#### 2、量化表序号(quantization table number)

#### 3、量化表(quantization table)

![img](https://cdn.nlark.com/yuque/0/2023/png/39298680/1698479092295-34702e46-5142-4fd8-a417-9bdfb3701f7f.png)

### 五、帧图像开始SOF0(Start of Frame)，数值0xC0

#### 1、帧开始长度(start of frame length)

#### 2、精度(precision)，每个颜色分量每个像素的位数(bits per pixel per color component)

#### 3、图像高度(image height)

#### 4、图像宽度(image width)

#### 5、颜色分量数(number of color components)

#### 6、对每个颜色分量(for each component)

#### 包括：ID、垂直方向的样本因子(vertical sample factor)、水平方向的样本因子(horizontal sample factor) 、量化表号(quantization table#)

![img](https://cdn.nlark.com/yuque/0/2023/png/39298680/1698479092220-f568cd06-f2e2-4cab-8976-44da4bc37e5e.png)

### 六、一个或者多个霍夫曼表DHT(Difine Huffman Table)，数值0xC4

#### 1、霍夫曼表的长度(Huffman table length)

#### 2、类型、AC或者DC(Type, AC or DC)

#### 3、索引(Index)

#### 4、位表(bits table)

#### 5、值表(value table)

#### ①JPEG文件里有２类Haffman表：一类用于DC（直流量），一类用于AC（交流量）。一般有４个表：亮度的DC和AC，色度的DC和AC。最多可有６个。

#### ②一个DHT段可以包含多个HT表,每个都有自己的信息字节③HT表是一个按递增次序代码长度排列的符号表。

![img](https://cdn.nlark.com/yuque/0/2023/png/39298680/1698479092224-dd222ae6-cd18-4482-ba9b-5fdc795c4dbc.png)

### 七、扫描开始SOS(Start of Scan)，数值0xDA

#### 1、扫描开始长度(start of scan length)

#### 2、颜色分量数(number of color components)

#### 3、每个颜色分量

#### 包括：ID、交流系数表号(AC table #)、直流系数表号(DC table #)

#### 4、压缩图像数据(compressed image data)

![img](https://cdn.nlark.com/yuque/0/2023/png/39298680/1698479093444-74b30768-4e29-40d8-82cf-0aa075fb691a.png)

### 八、图像结束EOI(End of Image)，数值0xD9