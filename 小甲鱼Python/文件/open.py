import os

file = open('text.txt', encoding='utf-8')
try:
    os.makedirs('output')
except FileExistsError as reason:
    print(reason)
once_text = []
count = 1

for line in file:
    if line[:1].isdigit():
        file_name = './output/第' + str(count) + '首.txt'
        file_tang = open(file_name, 'w')
        file_tang.writelines(once_text)
        file_tang.close()
        once_text = []
        count += 1
    else:
        once_text.append(line)
file.close()
