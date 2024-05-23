# 迭代器
def my_range(x):
    i = 0
    while i < x:
        yield i
        i += 1
print(my_range(4)) # <generator object my_range at 0x1024300b0>

for item in my_range(4):
    print(item) # 0 1 2 3