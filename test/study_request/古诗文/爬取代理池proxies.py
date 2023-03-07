#爬取快代理
import requests
import random
from lxml import etree

# url="https://www.kuaidaili.com/free/inha/1/"
#
# headers={
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.41",
#     "Cookie":"channelid=0; sid=1675307536235406; _gcl_au=1.1.1254820345.1675307538; Hm_lvt_7ed65b1cc4b810e9fd37959c9bb51b31=1675307538; _ga=GA1.2.925586065.1675307540; _gid=GA1.2.116017790.1676340085; sessionid=2d31aba2020eb2bf0ce79f7bd6c01e1a; _gat=1; Hm_lpvt_7ed65b1cc4b810e9fd37959c9bb51b31=1676340664"
# }
# response=requests.get(url=url,headers=headers).text
# tree=etree.HTML(response)
# ip_list=tree.xpath("//div[@id='list']/table[@class='table table-bordered table-striped']//tr")
#
# with open("proxie.txt",'w',encoding='utf-8') as fp:
#         for li in ip_list:
#             r=li.xpath(".//td/text()")
#             fp.write(str(r[:2])+"\n")



url = 'https://www.kuaidaili.com/free/inha/%d'

headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.41",
    "Cookie":"channelid=0; sid=1675307536235406; _gcl_au=1.1.1254820345.1675307538; Hm_lvt_7ed65b1cc4b810e9fd37959c9bb51b31=1675307538; _ga=GA1.2.925586065.1675307540; _gid=GA1.2.116017790.1676340085; sessionid=2d31aba2020eb2bf0ce79f7bd6c01e1a; _gat=1; Hm_lpvt_7ed65b1cc4b810e9fd37959c9bb51b31=1676340664",
    'Connection':"close"
}

ip_list=[
    {'HTTP': '210.5.10.87:53281'},
    {'HTTP': '202.109.157.63:9000'},
    {'HTTP': '183.236.232.160:8080'},
    {'HTTP': '121.13.252.62:41564'},
    {'HTTP': '112.14.47.6:52024'},
    {'HTTP': '117.114.149.66:55443'},
    {'HTTP': '222.74.73.202:42055'},
    {'HTTP': '116.9.163.205:58080'},
    {'HTTP': '117.41.38.16:9000'},
    {'HTTP': '27.42.168.46:55481'},
    {'HTTP': '121.13.252.61:41564'},
    {'HTTP': '61.216.185.88:60808'},
    {'HTTP': '61.216.156.222:60808'},
    {'HTTP': '121.13.252.58:41564'},
    {'HTTP': '202.109.157.62:9000'},
    {'HTTP': '61.216.185.88:60808'},
    {'HTTP': '61.216.156.222:60808'},
    {'HTTP': '121.13.252.58:41564'},
    {'HTTP': '202.109.157.65:9000'},
    {'HTTP': '121.13.252.60:41564'},
    {'HTTP': '210.5.10.87:53281'},
    {'HTTP': '117.94.116.240:9000'},
    {'HTTP': '183.236.232.160:8080'},
    {'HTTP': '121.13.252.62:41564'},
    {'HTTP': '112.14.47.6:52024'},
    {'HTTP': '117.114.149.66:55443'},
    {'HTTP': '222.74.73.202:42055'},
    {'HTTP': '202.109.157.67:9000'},
    {'HTTP': '116.9.163.205:58080'},
    {'HTTP': '27.42.168.46:55481'},
]

proxy_list_http = []

for page in range(1,10):
    new_url = format(url%page)
    ip_port = random.choice(ip_list)
    page_text = requests.get(url=new_url,headers=headers,proxies=ip_port).text
    tree = etree.HTML(page_text)
    #tbody不可以出现在xpath表达式中
    tr_list = tree.xpath("//div[@id='list']/table[@class='table table-bordered table-striped']//tr")

    for li in tr_list:
        if li == tree.xpath("//div[@id='list']/table[@class='table table-bordered table-striped']//tr")[0]:
            pass
        else:
            ip=li.xpath(".//td/text()")[0]
            port = li.xpath(".//td/text()")[1]
            ips = ip+':'+port
            dic = {
                'HTTP': ips
            }
            proxy_list_http.append(dic)
            print(dic,',')
print(len(proxy_list_http))



