import re
import random as r
import os

# 正则匹配name
print(re.search(r'name', 'My name is HarlanHu'))

# find方法匹配 无法使用通配符
print('My name is HarlanHu'.find('name'))

# 通配符 .
print(re.search(r'g.....', 'www.google.com'))
print(re.search(r'g.....\.com', 'www.google.com'))

# 通配符 \d,\.  等等
print(re.search(r'\d\.\d{2}', 'PI约等于3.1415926'))

# 字符类 [str] 区别大小写
print(re.search(r'[ilvyo]', 'I love you'))

# 匹配次数 {num}
print(re.search(r'go{2,5}gle', 'www.gooogle.com'))

# 匹配 0-255
num = str(r.randint(0, 255))
print(num + ':', re.search(r'25[0-5]|2[0-4]\d|1?\d{1,2}', num))

# 匹配ip
ip = str(r.randint(0, 255)) + '.' + str(r.randint(0, 255)) + '.' + str(r.randint(0, 255)) + '.' + str(r.randint(0, 255))
print(ip + ':', re.search(r'((1?\d{1,2}|2[0-4]\d|25[0-5])\.){3}(1?\d{1,2}|2[0-4]\d|25[0-5])', ip))

# 元字符： .(通配符) |(逻辑或) ^(脱字符：必须出现在首位或取反) $(必须出现在结尾) \ [...] {M,N}(匹配次数) *(0次或多次) +(1次或多次) ?(0次或1次)
str1 = 'hello world!'
str2 = 'hello world.'
print(re.search(r'world(!|.)', str1))
print(re.search(r'world(!|.)', str2))

print(re.search(r'^hello', str1))
print(re.search(r'world!$', str1))

print(re.findall(r'[^!]', str1))

# 贪婪匹配： *? +? ??
html = '<html><title>Google</title></html>'
print(re.search(r'<.+>', html))
# 非贪婪匹配 <html>
print(re.search(r'<.+?>', html))

# \A(匹配起始位置) \z(匹配结束位置) \b(匹配单词边界) \B(匹配非单词边界) \d(匹配任何一个数字) \D(匹配非数字) \s(匹配空白字符) \S(非空白) \w(匹配单词字母) \W(非单词字母)
str3 = 'hello world! hello world! hello world!'
print(re.findall(r'\bhello\b', str3))
print(re.findall(r'\Bell\B', str3))
print(re.findall(r'\w', str3))

# compile编译正则表达式
r = re.compile(r'[a-z]')
r.search(str3)
r.findall(str3)

# group() 子组分类
r = re.search(r'(\w+) (\w+)', str3)
print(r.group(1))
print(r.group(2))
