import requests
from lxml import etree
import random
import selenium


#创建会话存储cookie
session=requests.Session()

url='https://kyfw.12306.cn/otn/resources/login.html'

headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.41",
    "connect":"close"
}

#代理池
ip_list=[
    {'HTTP': '116.9.163.205:58080'},
    {'HTTP': '27.42.168.46:55481'},
    {'HTTP': '121.13.252.61:41564'},
    {'HTTP': '61.216.185.88:60808'},
    {'HTTP': '61.216.156.222:60808'},
    {'HTTP': '113.121.36.199:9999'},
    {'HTTP': '121.13.252.58:41564'},
    {'HTTP': '121.13.252.60:41564'},
    {'HTTP': '210.5.10.87:53281'},
    {'HTTP': '202.109.157.60:9000'},
    {"http": "118.120.251.190:21850"}
]


response=requests.get(url=url,headers=headers,proxies=random.choice(ip_list)).text

tree=etree.HTML(response)







