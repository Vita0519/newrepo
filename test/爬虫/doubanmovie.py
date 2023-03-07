import urllib.parse
import urllib.request

url='https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20'

# data={
#     'Cookie': 'll="118282"; bid=Wtfpi6mKq4k; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1673569818%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3D0cdDLiSYVsspOq1qZbnYf9vfRBkycivxMySoQnsaQburRahv44GMHhjNvlK-P5WG%26wd%3D%26eqid%3D948cfb9900095e870000000663c0a611%22%5D; _pk_ses.100001.4cf6=*; ap_v=0,6.0; __utma=30149280.281427536.1673569818.1673569818.1673569818.1; __utmb=30149280.0.10.1673569818; __utmc=30149280; __utmz=30149280.1673569818.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=223695111.1376909907.1673569818.1673569818.1673569818.1; __utmb=223695111.0.10.1673569818; __utmc=223695111; __utmz=223695111.1673569818.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __yadk_uid=FgHcIUtGNjxEXvyuJt9TEWyZPwPo6Zrs; _vwo_uuid_v2=DC76B27E0427D7D2335BCDD012F972EFD|ea4cb527ca929fa0c49d882af97ac335; __gads=ID=00e45b08be109010-22555a0b40d900f2:T=1673569813:RT=1673569813:S=ALNI_MZdsXGpS5Eja2HoQu6lKO7c182Zpw; __gpi=UID=00000ba31c28edbf:T=1673569813:RT=1673569813:S=ALNI_MZu8tWCY7c0Q5x_gMjGjzfhrJanMA; Hm_lvt_16a14f3002af32bf3a75dfe352478639=1673569833; Hm_lpvt_16a14f3002af32bf3a75dfe352478639=1673569833; _pk_id.100001.4cf6=706c51b3e33746f6.1673569818.1.1673570316.1673569818.
# '}


headers={
   'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76'
}

#请求对象的定制
request=urllib.request.Request(url=url,headers=headers)

#请求url响应
reponse=urllib.request.urlopen(request)
content=reponse.read().decode('utf-8')

#数据下载到本地
fp=open('douban.json','w',encoding='utf-8')
fp.write(content)
