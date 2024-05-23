import requests

r = requests.get('https://zh.wikipedia.org/wiki/%E7%BF%BB%E8%AF%91')
print(type(r.text)) # <class 'str'> 拿到页面 html 结构



