def mean(num_list):
    return sum(num_list) / len(num_list)

def add_five(num_list):
    return [num + 5 for num in num_list]


# 这样写的部分 只会在本文件执行
if __name__ == '__main__':
    print('hahahaha  , I am main func')
