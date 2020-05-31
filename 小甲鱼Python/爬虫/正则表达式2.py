import urllib.request
import re
import os
import shutil


def open_url(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                 'Chrome/81.0.4044.138 Safari/537.36')
    page = urllib.request.urlopen(req)
    html = page.read().decode('utf-8')
    return html


def open_img_url(img_url):
    req = urllib.request.Request(img_url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                 'Chrome81.0.4044.138 Safari/537.36')
    response = urllib.request.urlopen(req)
    html = response.read()
    return html


def get_img(html):
    p = r'img class="BDE_Image" src="([^"]+\.jpg)"'
    img_list = re.findall(p, html)
    for each in img_list:
        filename = each.split('/')[-1]
        with open(filename, 'wb') as f:
            img = open_img_url(each)
            f.write(img)


def get_content(html):
    p = r'<div id="post_content_\d+" class="d_post_content j_d_post_content " style="display:;">            ([^>]+)<'
    content_list = re.findall(p, html)
    for each in content_list:
        print(each)


if __name__ == '__main__':
    url = 'https://tieba.baidu.com/p/6699462153'
    folder = 'tieba'
    try:
        if folder not in os.listdir('/'):
            os.mkdir(folder)
            os.chdir(folder)
        else:
            shutil.rmtree(folder)
            os.mkdir(folder)
            os.chdir(folder)
    except FileExistsError as reason:
        print(reason)
    get_img(open_url(url))
    get_content(open_url(url))
