#用百度网页爬取周杰伦的信息

import urllib.request
import urllib.parse

#请求资源路径
url="https://www.baidu.com/s?wd="

#使用parse.quote方法对单个参数进行unicode编码
data=urllib.parse.quote("周杰伦")

#完整的资源路径
url=url+data

#请求头headers
headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.55"
}

#请求对象的定制
request=urllib.request.Request(url=url,headers=headers)

#模拟浏览器向服务器发送请求
response=urllib.request.urlopen(request)

#获取响应的数据
content=response.read().decode("utf-8")

#打印数据
print(content)


