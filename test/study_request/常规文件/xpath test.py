#导入必要的库
import requests
from lxml import etree
#URL就是网址，headers看图一
url='https://sh.58.com/ershoufang/'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.7 Safari/537.36'}
#对网站发起请求
page_test=requests.get(url=url,headers=headers).text
# 这里是将从互联网上获取的源码数据加载到该对象中
tree=etree.HTML(page_test)
#先看图二的解释，这里li有多个，所里返回的li_list是一个列表
li_list=tree.xpath('//ul[@class="house-list-wrap"]/li')
#这里我们打开一个58.txt文件来保存我们的信息
fp=open('58.txt','w',encoding='utf-8')
#li遍历li_list
for li in li_list:
	#这里 ./是对前面li的继承，相当于li/div...
    title=li.xpath('./div[2]/h2/a/text()')[0]
    print(title+'\n')
    #把文件写入文件
    fp.write(title+'\n')
fp.close()

