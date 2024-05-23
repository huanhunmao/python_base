# 默认 就是读文件
# f = open('some_file.txt')
f = open('some_file.txt','r') # 默认就是 r read
data_file = f.read()
f.close() # 记得及时关闭  否则开启太多会导致 后续 无法打开

print(data_file) # 可以打印出读取文件内容

# 写文件 write 新建 会删除之前的内容
f1 = open('another_file.txt', 'w')
f1.write('hahahhahaha  ppx')
f1.close()

print(f1)

# 写文件 write 新建 不会删除之前的内容 append
f2 = open('another_file.txt', 'a')
f2.write(' append some thing')
f2.close()

print(f2)