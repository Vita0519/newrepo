import requests
from lxml import etree

url='https://tophub.today/'

s=requests.Session()
headers={
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.50"
}

response=s.get(url=url,headers=headers).text

tree=etree.HTML(response)

a_list=[]
#爬取微博排行榜
news_name=tree.xpath('//*[@id="node-1"]/div/div[1]/div[1]/a/div/span/text()')[0]
# #热点新闻链接
# new_links=tree.xpath('//*[@id="node-1"]/div/div[2]/div[1]/a')
# for link in new_links:
#     new_next=link.xpath('./@href')[0]
#     a_list.append(new_next)
#微博热点新闻
new_list=tree.xpath('//*[@id="node-1"]/div/div[2]/div[1]/a')
for new in new_list:
    next_text=new.xpath('./div/span[2]/text()')[0]
    new_next = new.xpath('./@href')[0]
    a="热点："+next_text+","+"链接："+new_next
    a_list.append(a)

print(a_list)
#爬取知乎排行榜
zhihu=tree.xpath('//*[@id="node-6"]/div/div[1]/div[1]/a/div/span/text()')[0]

zh_list=tree.xpath('//*[@id="node-6"]/div/div[2]/div[1]/a')
for zh in zh_list:
    zh_text=zh.xpath('./div/span[2]/text()')[0]
    print(zh_text)

