# -*-coding:utf-8-*-
# 爬取奇书网的电子书
import os
import time
from lxml import html

import requests

# 域名
base_url = 'https://www.qisuu.com'
# 保存根目录
base_path = 'F:\\book\\'
# 当前目录
path = base_path
# 电子书列表
book_list = {}


# 下载电子书
def download(title, book):
    if book:
        print('下载电子书：', title, book)
        r = requests.get(book)
        with open(path + '\\' + title.replace('/', '／').replace('\\', '＼') + '.txt', "wb") as code:
            code.write(r.content)


# 爬取电子书信息
def get_book(url_path):
    print('爬取电子书信息：', url_path)
    book_content = get(base_url + url_path)
    title = book_content.xpath('//div[@class="detail_right"]/h1')[0].text
    book = book_content.xpath('//div[@class="showDown"]/ul/li[last()-1]/a/@href')
    download(title, book[0])
    time.sleep(2)


# 爬取电子书列表
def get_book_list(index_url):
    while index_url:
        print('爬取电子书列表:' + index_url)
        book_root = get(index_url)
        for a_el in book_root.xpath('//div[@class="listBox"]/ul/li/a'):
            book_list[a_el.text_content()] = a_el.xpath('@href')[0]
        index_url = False
        for a_el in book_root.xpath('//div[@class="tspage"]/a'):
            if a_el.text_content() == '下一页':
                index_url = base_url + a_el.xpath('@href')[0]
    print('电子书数量：', book_list.__len__())
    for k in book_list:
        get_book(book_list[k])


# 解析response
def get(url_path):
    return html.fromstring(requests.get(url_path).content)


if __name__ == '__main__':
    root = get(base_url)
    for a in root.xpath('//div[@class="nav"]/a'):
        url = a.xpath('@href')[0]
        if url != '/':
            path = base_path + a.text_content()
            if not os.path.exists(path):
                os.makedirs(path)
            get_book_list(base_url + url)
