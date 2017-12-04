# -*-coding:utf-8-*-
# 爬取妹子图
import os
import re
import sys
import time
from lxml import html

import requests

# 域名
base_url = 'http://www.mzitu.com'
# 保存根目录
base_path = 'D:\\Picture\\'
# 请求头
headers = {
    'Accept': 'image/webp,image/*,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Host': 'i.meizitu.net',
    'If-Modified-Since': 'Wed, 29 Nov 2017 14:18:50 GMT',
    'If-None-Match': '5a1ec1ca-183f5',
    'Referer': 'http://www.mzitu.com/110621',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'
}
# 等待时间
wait_time = 0.1


# 下载图片
def download(pic_dir, pic):
    if pic:
        target_path = pic_dir + os.path.splitext(pic)[1]
        print('下载图片：\t' + pic + '\t' + target_path)
        r = requests.get(pic, headers=headers)
        pic_obj = open(target_path, "wb")
        try:
            pic_obj.write(r.content)
        finally:
            pic_obj.close()


# 爬取图片信息
def get_pic(index_url):
    while index_url:
        print('爬取图片：\t' + index_url)
        pic_html = html.fromstring(requests.get(index_url).content)
        pic = pic_html.xpath('//div[@class="main-image"]/p/a/img/@src')
        pic_str = re.split('（|）', pic_html.xpath('//h2[@class="main-title"]')[0].text_content())
        pic_dir = base_path + re.sub(':|<|>|\?|\||"|\'|,|\*', '', pic_str[0])
        if not os.path.exists(pic_dir):
            os.makedirs(pic_dir)
        download(pic_dir + '\\' + (pic_str[1] if pic_str.__len__() > 1 else '1'), pic[0])
        last = pic_html.xpath('//div[@class="pagenavi"]/a[last()]/@href')[0]
        if last:
            index_url = last
        time.sleep(wait_time)


if __name__ == '__main__':
    if sys.argv[1]:
        base_path = sys.argv[1] + '\\'
    if sys.argv[2]:
        wait_time = float(sys.argv[2])
    get_pic(base_url + '/110293')
