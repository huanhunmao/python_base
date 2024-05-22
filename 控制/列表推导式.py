# 常规写法
items = ['ppx', 'haha', 'Mk', 'cc']

new_items = []

for item in items:
    new_items.append(item.title())

print(new_items) # ['Ppx', 'Haha', 'Mk', 'Cc']


# 推导式写法 ✍️  我艹 这写法 相当夸张 甚至 么有 逗号 
items1 = ['ppx', 'haha', 'Mk', 'cc']
new_items1 = [item.title() for item in items1]
print(new_items1)  # ['Ppx', 'Haha', 'Mk', 'Cc']