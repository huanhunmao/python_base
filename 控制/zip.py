# zip 方法 可以 进行 组合 非常 强大
items = ['apple', 'orange', 'cheeses']
weights = [15, 26, 99, 66]

for item, weight in zip(items,weights):
    print(item, weight)
    # apple
    # 15
    # orange
    # 26
    # cheeses
    # 99

# 还可以  * 拆分
mainfest = [('bananas', 15), ('apple', 50), ('orange', 30), ('other', 40), ('ppx', 40)]
item1, weight1 = zip(*mainfest)
print(item1) # ('bananas', 'apple', 'orange', 'other', 'ppx')
print(weight1) # (15, 50, 30, 40, 40)

#  拿到和索引对应的值
items2 = ['hahah', 'ppx', 'clg', 'ggc']
for i, item in enumerate(items2):
    print(i, item)
    # 0 hahah
    # 1 ppx
    # 2 clg
    # 3 ggc