
import requests
import os
import json
from lxml import etree
import pandas as pd
import time
# 导入字体解密模块
from fontTools.ttLib import TTFont


'''
小说数据的爬取及其数据化分析
'''
results = {
    'title': [],  # 文章标题
    'author': [],  # 小说作者
    'classifies': [],  # 小说类别
    'describes': []   # 小说的描述
    # 'detail': [],  # 文章详情地址
    # 'wordcount': []  # 文字统计
}

class novel:
    def __init__(self, value):
        self.header = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4464.5 Safari/537.36',
        }
        self.page = value
        self.url = 'https://www.qidian.com/rank/recom?dateType=1&page={}'.format(self.page)
        self.foreach(value)
    # 页面请求
    def dataAnalysis(self):
        res = requests.get(self.url, headers=self.header).text
        return res
    # 页面解析
    def etreehtml(self):
        # 使用etree.Html方法
        lists = etree.HTML(self.dataAnalysis())
        # print(lists)
        content = lists.xpath('//*[@id="rank-view-list"]/div/ul/li')
        return content
        # self.dataAnalysis()
    # 对加密字体进行解密处理
    def decodeTtf(self):
        font = TTFont('UdygXvZa.ttf')
        font.saveXML('fft.xml')
        # 获取字体映射关系
        font_cmap = font['cmap'].getBestCmap()
        print(font_cmap)

    # 对数据进行遍历分析
    def foreach(self,value):
        for i in self.etreehtml():
            # 小说标题
            title = i.xpath('./div[2]/h4/a/text()')[0].replace('\n', '')
            results['title'].append(title)
            # 小说作者
            author = i.xpath('./div[2]/p[1]/a[1]/text()')[0].replace('\n', '')
            results['author'].append(author)
            # 小说类别
            classifies = i.xpath('./div[2]/p[1]/a[2]/text()')[0].replace('\n', '')
            results['classifies'].append(classifies)
            # 小说描述
            describes = i.xpath('./div[2]/p[2]/text()')[0].replace(" ", '').replace('\n', '').replace('\t', '').replace('\r', '')
            results['describes'].append(describes)
        print('第%s个页面已爬取完成------' % value)
    def buildcsv(self):
        # 创建表格
        df = pd.DataFrame(results)
        # 将解码方式改为ANSI  打开可以解决中文乱码的问题
        df.to_csv('qidian1.csv', encoding='utf8')
        print('------表格数据创建完成！！！')
        #     # 文章详情页面
        #     detail = i.xpath('./div[3]/p/a[1]/@href')[0].replace('\n', '')  # 将获取到的换行数据取消，并且导入到新的数组中
        #     results['detail'].append(detail)
        #     # print(results)
        #     # 进入子页面对页面的数据进行爬取遍历分别爬取
        # print(results['detail'])
        # for i in results['detail']:
        #     url = 'https:%s' % i
        #     res = requests.get(url, headers=self.header).text
        #     # 对子页面进行解析
        #     childPage = etree.HTML(res)
        #     # numcount = childPage.xpath('/html/body/div/div[6]/div[1]/div[2]/p[3]/em')
        #     # 字数tongj
        #     wordcount = childPage.xpath('/html/body/div/div[6]/div[1]/div[2]/p[3]/em[1]/span/text()')
        #     # 将字数统计加入到wordcounts当前数组中
        #     results['wordcount'].append(wordcount)
        # print(results['wordcount'])

if __name__ == '__main__':
    # 也可以使用for i range(1,6) 将所有的数据爬取出来
    # novel(value=input('请输入爬取的页面1-5：'))
    # 选择单页爬取或者多页爬取
    for a in range(1, 6):
        p = novel(str(a))
        time.sleep(1.5)
    print("------开始创建表格信息")
    p.buildcsv()
