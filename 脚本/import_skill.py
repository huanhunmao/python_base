# 导入文件技巧  重命名
# import multiprocessing as mt
# print(mt.cpu_count()) # 12


# 导入其中某一块
# from collections import defaultdict, namedtuple
# defaultdict()
# namedtuple()

# 导入后 重新命名 避免冲突
from csv import reader as csvreader

# 全部导入 别这样使用 ❌
from random import *
print(random())

# 如果想导入 一些 用
# random.xxxx

