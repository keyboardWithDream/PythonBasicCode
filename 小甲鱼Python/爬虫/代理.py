import urllib.request

url = 'https://www.ip.cn/'
# 代理池
proxy_support = urllib.request.ProxyHandler({'http:': '101.37.118.54:8888'})
# 创建opener
opener = urllib.request.build_opener(proxy_support)
# opener添加heard
opener.addheaders = [('user-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                    'Chrome/81.0.4044.138 Safari/537.36')]
# 安装opener
urllib.request.install_opener(opener)

responses = urllib.request.urlopen(url)
html = responses.read().decode('utf-8')
print(html)