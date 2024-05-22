iphone_money = 3
bank_money = 100

# 最基本的 if 语句格式
if iphone_money < 5:
    iphone_money += 10
    bank_money -= 10

print(iphone_money) # 13
print(bank_money) # 90

# if else
n = 13
if n % 2 == 0:
    print('Number' + str(n) + 'is even')
else:
    print('Number ' + str(n) + ' is not even') # Number 13 is not even

# if else if
x = 100
if x > 100:
    print('number is better than 100')
elif x == 100:
    print('number equal to 100') # number equal to 100
else:
    print('number is less than 100')