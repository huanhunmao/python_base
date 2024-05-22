# 求 0-8 乘方
squares = []
for x in range(9):
    squares.append(x ** 2)
print(squares) # [0, 1, 4, 9, 16, 25, 36, 49, 64]

# 推导式写法 ✍️
squares1 = [x ** 2 for x in range(9)]
print(squares1) # [0, 1, 4, 9, 16, 25, 36, 49, 64]

# 再加个条件 只要 偶数
squares2 = [x ** 2 for x in range(9) if x % 2 == 0]
print(squares2) # [0, 4, 16, 36, 64]

# 如果再加个 else 需要写在前面
squares3 = [x ** 2 if x % 2 == 0 else x + 3 for x in range(9)]
print(squares3) # [0, 4, 4, 6, 16, 8, 36, 10, 64]