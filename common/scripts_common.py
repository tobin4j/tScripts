import operator
import math
from enum import Enum
from functools import reduce


# 判断两张图相似度
def image_same_val(img1, img2):
    h1 = img1.histogram()
    h2 = img2.histogram()
    a = math.sqrt(reduce(operator.add, list(map(lambda a, b: (a - b) ** 2, h1, h2))) / len(h1))
    return a


# 通用选择输入方法
def common_input_switch(dic):
    type_val = 0
    for key in dic.keys():
        print(key, ":", dic[key], "\n")

    while type_val not in range(1, len(dic) + 1):
        print("请选择类型:")
        try:
            type_val = int(input())
            if type_val not in range(1, len(dic) + 1):
                print('输入错误..')
        except:
            print('输入错误..')
    print('已选择:', dic[type_val])
    return type_val


# 通用睡眠时长
class Sleep(Enum):
    VERY_SHORT = 0.1
    SHORT = 0.5
    MIDDLE = 1
    MIDDLE_LONG = 3
    LONG = 5
