import pymysql
import requests
from lxml import etree

# 连接数据库
mydb = pymysql.connect(host='192.168.1.6', port=9030, user='szjt', passwd='09+t,KtBuBAgylV3QDGAvtI=6=~Fa7', database='test')

# # 建表语句
# mycursor=mydb.cursor()
# mycursor.execute('CREATE table test.bqg(book_name varchar(128) null comment "书名",link varchar(256) null comment "链接",category varchar(32) null comment "类型",author varchar(64) null comment "作者",recommend bigint null comment "推荐") duplicate key(book_name,link) comment "笔趣阁热门小说" distributed by hash(category) buckets 2 PROPERTIES ("replication_allocation" = "tag.location.default: 3",  "in_memory" = "false", "storage_format" = "V2");')

url="https://www.bbiquge.net/top/monthvisit/2.html"  #想要爬取第几页就改到第几页，也可加入循环连续爬取多页数据

headers={
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.78",
    "cookie":"Hm_lvt_007bc30c1abb0ffb7a93b4f3c8e10c5e=1675822949; __gads=ID=d1a8b3b3b9c80e45-221df6fd90d900f1:T=1675823870:RT=1675823870:S=ALNI_MZvfau8teos-W_oi2DkLvHJ0ngI6w; __gpi=UID=00000bb7a84952a5:T=1675823870:RT=1675953461:S=ALNI_Mahob6Yo27D6iGdTSKFupGzskNPuw; Hm_lpvt_007bc30c1abb0ffb7a93b4f3c8e10c5e=1675997074"
}

bqg = requests.get(url=url,headers=headers).text

tree=etree.HTML(bqg)

base_list=tree.xpath("//div[@id='articlelist']/ul[2]/li")

#etree解析返回的是list形式
for li in base_list:
            book_name = li.xpath("./span[@class='l2']/a/text()")
            link = li.xpath("./span[@class='l2']/a/@href")
            category = li.xpath("./span[@class='l1']/text()")
            author=li.xpath("./span[@class='l3']/text()")
            recommend=li.xpath("./span[@class='l6']/text()")
            mycursor=mydb.cursor()
            sql="insert into bqg values ('{}','{}','{}','{}','{}')".format(book_name[0],link[0],category[0],author[0],recommend[0])
            mycursor.execute(sql)
            mydb.commit()
mydb.close()
