# 比较复杂 布尔判断
weight = 55
height = 1.64 # 米


if 18.5 <= weight / height ** 2 < 25:
    print("BMI is considered 'normal'") # BMI is considered 'normal'

has_time = True
has_money = True

if has_time and has_money:
    print('Hahahahh') # Hahahahh
else:
    print('Not good')


spend = False
location = 'USA'
# 这个 not 相当于 js ！ 非
if not spend and (location == 'USA' or location == 'CH'):
    print('good') # good
else:
    print('bad')