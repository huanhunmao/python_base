# 捕获错误 ❌ 和 js 有点不一样  使用的是 try except finally

try:
    x = int(input('Enter a int num: '))
    print(x)
except:
    print('It is a valid num')
finally:
    print('Attempted Input')


# 可以加多个 except
# 可以将 整体放在循环中 ♻️
# except ValueError:
#     print('It is a valid num')
# except KeyboardInterrupt:
#     print('No input')