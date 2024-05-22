
print(88 > 22)  # True

print(99 >= 77)  # True

print(10 > 200)  # False

print(99 == 99)  # True  注意这个地方 没有 === 只有 ==

print(99 != 66)  # True


# and or not  和 js 不一样
age = 14
is_teen = age > 12 and age < 18
is_not_teen = not(age > 12 and age < 18)
print(is_teen)  # True
print(is_not_teen)  # False