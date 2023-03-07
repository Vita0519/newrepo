#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Author  : 寻觅
# @File    : 图片爬取.py
# @Time    : 2020/2/12 13:24
# @Software: PyCharm

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup


class Study:
    def __init__(self):
        self.url = 'https://article.xuexi.cn/articles/index.html?art_id=15308933272663801705&item_id=15308933272663801705&study_style_id=feeds_default&showmenu=true&aid=15308933272663801705&item_type=1&recoid=12578234090040657023_1581240011&cid=&study_comment_disable=1&pid=34682268069627302&ref_read_id=8c1f7cad-22cf-473b-be16-3bf204f50468&ptype=100&source=share&share_to=wx_single&from=singlemessage'
        self.header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0'}
        self.driver = None

    def open_web(self):
        """打开浏览器"""
        driver = webdriver.Firefox()
        # 最小化浏览器
        driver.minimize_window()
        return driver

    def get_url(self):
        """访问url"""
        # 使用requests无法取得完整的页面源码,如下
        # html = requests.get(self.url, headers=self.header)
        # html.encoding = 'utf-8'
        # return html.content
        # 使用selenium
        driver = self.open_web()
        driver.get(self.url)
        # 网页逻辑太差,且图片应该为懒加载,所以需要使用此条件来判断是否加载完成,注释下方两行获取的网页将不完整
        # 隐式等待
        # driver.implicitly_wait(1)
        # driver.find_element_by_css_selector('img[class="xxqg-image"]')
        # 显式等待
        WebDriverWait(driver, 3).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'img[class="xxqg-image"]'))
        )
        return driver.page_source

    def write_html(self, html):
        """写入到本地"""
        with open('河南学习强国.html', 'w') as w:
            w.write(html)

    # extract(提取)
    def data_extract(self, data):
        """数据提取"""
        bs_data = BeautifulSoup(data, 'lxml')
        data = bs_data.select('img[class="xxqg-image"]')
        img_url = []
        for i in data:
            img_url.append(i['data-src'])
        return img_url

    def get_img(self, img_url):
        """将图片链接转为二进制格式的图片"""
        img_data = []
        i = 1
        print('获取的网页中首个图片为:', img_url[0])
        for url in img_url:
            print('\r共有%d张图片。正在下载第%d张图片' % (len(img_url), i), end=" ")
            img = requests.get(url, headers=self.header)
            img_data.append(img)
            i += 1
        return img_data

    def write_img(self, img_data):
        """保存图片"""
        i = 1
        for img in img_data:
            with open(f'图片/第{i}张图片.jpg', 'wb') as w:
                print('\r共有%d张图片。正在保存第%d张图片' % (len(img_data), i), end=" ")
                w.write(img.content)
            i += 1

    def run(self):
        """启动"""
        # 保存网页源码
        html = self.get_url()
        # 保存网页源码
        self.write_html(html)
        # 获取网页源码
        # html = open('河南学习强国.html').read()
        # 提取图片链接
        # print('正在获取图片链接')
        # img_url = self.data_extract(html)
        # 将链接转换为图片
        # print('正在将链接转换为图片')
        # img_data = self.get_img(img_url)
        # 保存图片
        # print('\n正在保存')
        # self.write_img(img_data)
        # print('\n程序完成')

if __name__ == '__main__':
    Study().run()



