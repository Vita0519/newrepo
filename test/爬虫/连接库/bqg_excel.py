import requests
from lxml import etree
import json
import xlwt

url="https://www.bbiquge.net/top/monthvisit/"

headers={
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.78",
    "cookie":"Hm_lvt_007bc30c1abb0ffb7a93b4f3c8e10c5e=1675822949; __gads=ID=d1a8b3b3b9c80e45-221df6fd90d900f1:T=1675823870:RT=1675823870:S=ALNI_MZvfau8teos-W_oi2DkLvHJ0ngI6w; __gpi=UID=00000bb7a84952a5:T=1675823870:RT=1675953461:S=ALNI_Mahob6Yo27D6iGdTSKFupGzskNPuw; Hm_lpvt_007bc30c1abb0ffb7a93b4f3c8e10c5e=1675997074"
}

bqg = requests.get(url=url,headers=headers).text

tree=etree.HTML(bqg)

base_list=tree.xpath("//div[@id='articlelist']/ul[2]/li")

# #etree解析返回的是list形式
# with open("bqg.txt", 'w', encoding="utf-8") as fp:
#         for li in base_list:
#             category = li.xpath("./span[@class='l1']/text()")
#             book_name = li.xpath("./span[@class='l2']/a/text()")
#             author=li.xpath("./span[@class='l3']/text()")
#             recommend=li.xpath("./span[@class='l6']/text()")
#             link=li.xpath("./span[@class='l2']/a/@href")
#             # fp.write(str(category)+' '+str(book_name)+' '+str(author)+' '+str(link)+' '+str(recommend) + '\n')
#             fp.write(str(category+book_name+author+link+recommend)+"\n")


# 设置文件输出名
place = '笔趣阁'
output_type = '热门小说'
file_name = place + output_type + '.xls'

# 创建表格
workbook = xlwt.Workbook(encoding = 'utf-8')
worksheet = workbook.add_sheet('Sheet 1')

#写表头
worksheet.write(0,0,'category')
worksheet.write(0,1,'book_name')
worksheet.write(0,2,'author')
worksheet.write(0,3,'recommend')
worksheet.write(0,4,'link')
#行数  worksheet.write(行,列,内容)
i=1
#获取数据
for li in base_list:
        worksheet.write(i,0,li.xpath("./span[@class='l1']/text()"))
        worksheet.write(i,1,li.xpath("./span[@class='l2']/a/text()"))
        worksheet.write(i, 2, li.xpath("./span[@class='l3']/text()"))
        worksheet.write(i, 3, li.xpath("./span[@class='l6']/text()"))
        worksheet.write(i, 4, li.xpath("./span[@class='l2']/a/@href"))
        i = i + 1

workbook.save(file_name)
print("文件保存成功，请至爬虫所在目录下查看文件。")