# -*-coding:utf-8-*-
import requests
from lxml import html

# 域名
base_url = 'https://www.qisuu.com'


# 下载电子书
def download(title, book):
    print('下载电子书：', title, book)
    r = requests.get(book)
    with open('F:\\book\\' + title.replace('/', '／').replace('\\', '＼') + '.txt', "wb") as code:
        code.write(r.content)


# 爬取电子书信息
def get_book(url):
    print('爬取电子书信息：', url)
    resp = requests.get(base_url + url)
    root = html.fromstring(resp.content)
    title = root.xpath('//div[@class="detail_right"]/h1')[0].text
    book = root.xpath('//div[@class="showDown"]/ul/li[last()-1]/a/@href')
    download(title, book[0])


# 爬取电子书列表
def get_book_list():
    print('爬取电子书列表...')
    resp = requests.get(base_url + '/s/hot/')
    root = html.fromstring(resp.content)
    for l in root.xpath('//div[@class="listBox"]/ul/li/a/@href'):
        get_book(l)


if __name__ == '__main__':
    get_book_list()
