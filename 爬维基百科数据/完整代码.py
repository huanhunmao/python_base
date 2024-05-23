import time
import urllib

from bs4 import BeautifulSoup
import requests


start_url = "https://en.wikipedia.org/wiki/Special:Random"
target_url = "https://en.wikipedia.org/wiki/Philosophy"
def find_first_link(url):
    request = requests.get(url)
    soup = BeautifulSoup(request.text, 'html.parser')

    content_div = soup.find(id='mw-content-text').find(class_='mw-parser-output')
    article_link = None

    for element in content_div.find_all('p', recursive= False):
        if element.find('a', recursive=False):
            article_link=element.find('a',recursive=False).get('href')
            break

    if not article_link:
        return

    first_link = urllib.parse.urljoin('https://en.wikipedia.org/', article_link)
    return first_link

# 控制爬虫的停止条件，防止爬虫陷入无限循环或者过长的爬取过程
def continue_crawl(search_history, target_url, max_steps=25):
    # search_history 的最后一个元素（即最近访问的页面）等于 target_url
    if search_history[-1] == target_url:
        print("We've found the target article!")
        return False
    elif len(search_history) > max_steps:
        print("The search has gone on suspiciously long, aborting search!")
        return False
    # search_history 的最后一个元素在 search_history 列表的前部分出现过
    elif search_history[-1] in search_history[:-1]:
        print("We've arrived at an article we've already seen, aborting search!")
        return False
    else:
        return True

article_chain = [start_url]

while continue_crawl(article_chain, target_url):
    print(article_chain[-1])

    first_link = find_first_link(article_chain[-1])
    if not first_link:
        print("We've arrived at an article with no links, aborting search!")
        break

    article_chain.append(first_link)

    time.sleep(2)