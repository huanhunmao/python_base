# 更加通用的方式 发现结构一样 有统一的 id
import requests
from bs4 import BeautifulSoup

html_doc = requests.get('https://zh.wikipedia.org/wiki/Main_Page')
soup = BeautifulSoup(html_doc.text, 'html.parser')
# print(soup.find(id="mw-content-text").p.a) # <a href="/wiki/%E7%94%B5%E5%AD%90%E8%AE%A1%E7%AE%97%E6%9C%BA" title="电子计算机">计算机</a>
print((soup.find(id="mw-content-text").p.a.get('href'))) # /wiki/%E7%94%B5%E5%AD%90%E8%AE%A1%E7%AE%97%E6%9C%BA  拿到这个 a 标签 href
