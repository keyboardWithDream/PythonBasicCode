import urllib.request
import urllib.error

req = urllib.request.Request('http://www.fishc.com/ooxx.html')
try:
    urllib.request.urlopen(req)
except urllib.error.HTTPError as e:
    print('The server could\'t fulfill the request.')
    print('Error code:', e.code)
except urllib.error.URLError as e:
    print('We faild to reach a server.')
    print('Error:', e.reason)
else:
    print('访问成功')