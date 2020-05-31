import urllib.request
import base64
import os


def open_url(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                 'Chrome/81.0.4044.138 Safari/537.36')
    response = urllib.request.urlopen(req)
    html = response.read()
    return html


def get_page(url):
    html = open_url(url).decode('utf-8')
    start = html.find('current-comment-page') + 23
    end = html.find(']', start)
    return int(html[start: end])


def find_imgs(url):
    html = open_url(url).decode('utf-8')
    img_addrs = []
    start = html.find('img src=')
    while start != -1:
        end = html.find('.jpg', start, start + 255)
        if end != -1:
            img_addrs.append('http:' + html[start + 9: end + 4])
        else:
            end = start + 9
        start = html.find('img src=', end)

    return img_addrs


def save_imgs(folder, img_addrs):
    for each in img_addrs:
        filename = each.split('/')[-1]
        with open(filename, 'wb') as f:
            img = open_url(each)
            f.write(img)


def download_pic(folder='img', pages=10):
    os.mkdir(folder)
    os.chdir(folder)
    url = 'http://jandan.net/ooxx/'
    page_num = get_page(url)
    for i in range(pages):
        page_num -= i
        print(page_num)
        page = "20200522-" + str(page_num)
        print(page)
        page_url = url + str(base64.b64encode(page.encode('utf-8')))[2:17] + '#comments'
        print(page_url)
        img_addrs = find_imgs(page_url)
        save_imgs(folder, img_addrs)


if __name__ == '__main__':
    download_pic()