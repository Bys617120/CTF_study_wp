# -*- coding:utf-8 -*-
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
