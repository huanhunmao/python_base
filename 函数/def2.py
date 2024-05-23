# 函数参数和 js 一样可设置默认值
def new_func(x, y = 2):
    print(x * y)
new_func(2) # 4
new_func(2,5) # 10