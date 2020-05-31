import urllib.request

req = urllib.request.Request('http://placekitten.com/700/700')
response = urllib.request.urlopen(req)

# response = urllib.request.urlopen('http://placekitten.com/500/500')

file = response.read()

with open('cat_700_700.jpg', 'wb') as f:
    f.write(file)

# 获取链接地址
print(response.geturl())
# 获取head信息
print(response.info())
# 获取http状态
print(response.getcode())
