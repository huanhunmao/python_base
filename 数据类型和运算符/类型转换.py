int_var = 666
print(str(type(str(int_var))))  # <class 'str'>
print(float(int_var)) # 666.0

float_var = '999'
print(type(int(float_var))) # <class 'int'>


# 注意⚠️ 不同类型不能相加  和 js 不一样 js 会连成字符串
print(777 + 'op') # TypeError: unsupported operand type(s) for +: 'int' and 'str'