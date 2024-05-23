# 可以 使用 with 方式 不用手动关闭 会自动关闭

with open('another_file.txt', 'r') as f:
    data_file = f.read()

print(data_file) # hahahhahaha  ppx append some thing