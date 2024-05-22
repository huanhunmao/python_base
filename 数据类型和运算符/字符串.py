# 单双引号都可以
print('hello')  # hello
print("hey")  # hey


# 混合使用
print("hello, 'Marxu'") # hello, 'Marxu'

# 和 js 一样 可以相加
print('hello' + 'ppx') # helloppx

# 如果需要空格
print('hey' + ' ' + 'hhh') # hey hhh


# 还可以 * 和 js 不一样 会输出 NaN
print('hello' * 5) # hellohellohellohellohello

# 字符串 不支持 / 除法
# print('hello' / 'hey') # TypeError: unsupported operand type(s) for /: 'str' and 'str'

# 长度 len
print(len('hello')) # 5