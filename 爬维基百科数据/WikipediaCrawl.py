import time


def continue_crawl(search_history, target_url, max_steps=25):
    if search_history[-1] == target_url:
        print('good, we find it')
        return False
    if len(search_history) > max_steps:
        print('too lang!')
        return False
    if search_history[-1] == search_history[:-1]:
        print('has searched!')
        return False
    else:
        return True

# while continue_crawl(article_chain, target_url):
#     first_link = first_first_link(article_chain[-1])
#     article_chain.append(first_link)
#     time.sleep(2)