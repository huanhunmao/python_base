# 变量 函数 也存在和 js 一样的作用域
ans = 10
def show_number():
    print(ans)
show_number() # 10


# 找数字
def find_number(numbers, target):
    answer = 0
    for number in numbers:
        if number == target:
            answer += 1
    return answer

print(find_number([1,2,4,4],4)) # 2

# 另外一个函数
def nearst_square(limit):
    answer = 0
    while(answer + 1) ** 2 < limit:
        answer += 1
    return answer ** 2
print(answer) # 定义在函数内的 函数外 无法使用到 
nearst_square(9) # NameError: name 'answer' is not defined