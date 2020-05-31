import os

file_name = input('请输入要显示的文件：')

try:
    file = open(file_name)
except OSError as reason:
    print('文件出错！', reason)
else:
    print('内容为：')
    for line in file:
        print(line)
    file.close()