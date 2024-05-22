
fruit = ['orange', 'apple', 'other']
foods = ['apple', 'orange', 'hahah']

fruit_count = 0
for food in foods:
    if food not in fruit:
        print('not  fruit')
        continue
    fruit_count += 1
    print('found a fruit')

print('Total count: ',fruit_count)
# found a fruit
# found a fruit
# not fruit
# Total count:  2


# break
mainfest = [('bananas', 15), ('apple', 50), ('orange', 30), ('other', 40), ('ppx', 40)]

weight = 0
items = []
for cargo in mainfest:
    # 每次添加货物之前判断添加该货物后是否会超重，如果会超重则停止添加，从而确保weight不会超过100
    if weight + cargo[1] > 100:
        break
    else:
        items.append(cargo[0])
        weight += cargo[1]

print(weight)
print(items)

# 95
# ['bananas', 'apple', 'orange']