import requests
from bs4 import BeautifulSoup

html_doc = requests.get('https://zh.wikipedia.org/wiki/Main_Page')
soup = BeautifulSoup(html_doc.text, 'html.parser')
print(soup.title) # <title>首页 - 维基百科，自由的百科全书</title>
print(soup.p) # <p><b>首页</b>或<b>主页</b>（英語：<span lang="en">home page或homepage</span>）是<a href="/wiki/%E7%94%B5%E5%AD%90%E8%AE%A1%E7%AE%97%E6%9C%BA" title="电子计算机">计算机</a><a href="/wiki/%E6%9C%AF%E8%AF%AD" title="术语">术语</a>，各<a class="mw-redirect" href="/wiki/%E7%BD%91%E7%AB%99" title="网站">网站</a>的主要<a class="mw-redirect" href="/wiki/%E7%BD%91%E9%A1%B5" title="网页">网页</a>——一般是指访问一个应用程序启动时始终显示在网站或<a href="/wiki/%E7%BD%91%E9%A1%B5%E6%B5%8F%E8%A7%88%E5%99%A8" title="网页浏览器">网页浏览器</a>中的一个或多个初始网页等画面存在的站点，在这种解释里亦稱<b>起始页</b>（英語：<span lang="en">start page</span>）。从更广泛的意义上说，主页被视为<a href="/wiki/%E4%BA%92%E8%81%94%E7%BD%91" title="互联网">互联网</a>网站的一个名称，专指网站本身。
# </p>
print(soup.p.a) # <a href="/wiki/%E7%94%B5%E5%AD%90%E8%AE%A1%E7%AE%97%E6%9C%BA" title="电子计算机">计算机</a>