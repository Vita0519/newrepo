#爬取doris使用文档
#get请求方法
#url=https://doris.apache.org/zh-CN/docs/dev/lakehouse/multi-catalog/hive/
# #headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
#     }


import urllib.request
import urllib.parse

#1.请求资源路径url
url='https://doris.apache.org/zh-CN/docs/dev/lakehouse/multi-catalog/hive/'

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
    }
#2.定制请求对象

request=urllib.request.Request(url=url,headers=headers)

#3.模拟浏览器向服务器发送请求
response=urllib.request.urlopen(request)

#4.获取响应数据
content=response.read().decode("utf-8")

#5.打印数据
print(content)
print(type(headers))