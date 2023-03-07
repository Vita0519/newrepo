import requests
from lxml import etree
import random

#创建session对象，保存cookie，解决动态cookie
s=requests.Session()

url="https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx"

headers={
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.41",
}
params={"from":" http://so.gushiwen.cn/user/collect.aspx"}

#解析图片验证码参数
code_img=s.get(url=url,params=params,headers=headers).text
tree=etree.HTML(code_img)

#拼接验证码图片链接地址
img_link="https://so.gushiwen.cn"+tree.xpath('//*[@id="imgCode"]/@src')[0]

#下载验证码图片
img_data=s.get(img_link,headers=headers).content
with open("code.png", "wb") as fp:
    fp.write(img_data)

code=input("请输入验证码：")
#解决动态参数问题
VIEWSTATE=tree.xpath("//*[@id='__VIEWSTATE']/@value")[0]
VIEWSTATEGENERATOR=tree.xpath('//*[@id="__VIEWSTATEGENERATOR"]/@value')[0]
data={
        "__VIEWSTATE":VIEWSTATE,
        "__VIEWSTATEGENERATOR":VIEWSTATEGENERATOR,
        "from": "http://so.gushiwen.cn/user/collect.aspx",
        "email": "13733560730",
        "pwd": "meng19980116",
        "code": code,
        "denglu": "登录"
}
#ip代理池
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

#post模拟登录
index=s.post(url=url,data=data,headers=headers,proxies=random.choice(ip_list))
#获取登陆后的页面源码
detial_url="https://so.gushiwen.cn/user/collect.aspx"
response=s.get(url=detial_url,headers=headers).text
with open("gushiwen.html", 'w', encoding='utf_8') as tp:
    tp.write(response)

