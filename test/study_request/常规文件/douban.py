
#爬取豆瓣电影排行榜
import urllib.request
import json

#请求资源路径
url="https://movie.douban.com/chart"

#请求头
headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.55"
}

#定制请求对象
request=urllib.request.Request(url=url,headers=headers)

#模拟浏览器向服务器发送请求
response=urllib.request.urlopen(request)

#获取响应的数据
content=response.read().decode("utf-8")

print(content)

# #使用json下载查看数据
# obj=json.loads(content)

# #打印
# print(obj)