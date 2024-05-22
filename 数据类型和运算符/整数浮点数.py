from decimal import Decimal
print(4/7) # 0.5714285714285714
print(16/4) # 4.0

print(type(10/2)) # <class 'float'>

print(3 + 3.5) # 6.5

x = 5

print(type(x)) # <class 'int'>

# 整数 / 服点数 转化
print(int(67.29)) # 67  转整数直接截断 不进行四舍五入
print(float(99)) # 99.0  整数后直接 加小数点


# 相加 精度 会有问题
print(0.1+ 0.1 + 0.1) # 0.30000000000000004

print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1'))
# 0.3 Decimal 提供了更高的精度和对十进制数的精确表示

