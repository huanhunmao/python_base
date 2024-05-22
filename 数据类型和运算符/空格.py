# 空格 并不会 影响 代码执行 但会影响 人的使用
# 更多 请参考 python 代码规范 PEP 8

# Correct:
spam(ham[1], {eggs: 2})
# Wrong:
spam( ham[ 1 ], { eggs: 2 } )

# Correct:
foo = (0,)
# Wrong:
bar = (0, )

# Correct:
if x == 4: print(x, y); x, y = y, x
# Wrong:
if x == 4 : print(x , y) ; x , y = y , x