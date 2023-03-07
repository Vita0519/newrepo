import requests

url='https://www.osgeo.cn/scrapy/topics/commands.html'

header={
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.70',

}

key=input("请输入要翻译的内容:")

data={
'kw': key
}

res = requests.post(url=url, data=data, headers=header).text

with open('bd.json','w',encoding='utf-8') as fp:
    fp.write(str(res))


