#获取豆瓣电影排行，动作电影的前十页

import urllib.request
import urllib.parse

#获取请求资源路径
#第一页url
# url="https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&
# start=0&limit=20"
# #第二页url
# url="https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=
# &start=20&limit=20"

#
def create_request(page):
    base_url="https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&"
    data={
        'start':(page-1)*20,
        'limit':20
    }
    data=urllib.parse.urlencode(data)

    url=base_url+data

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
    }
    request=urllib.request.Request(url=url,headers=headers)
    return request

def get_content(request):
     respense=urllib.request.urlopen(request)
     content=respense.read().decode('utf-8')
     return content


def down_load(page,content):
    with open('douban_' + str(page) + '.json','w',encoding='utf-8')as fp:
        fp.write(content)




if __name__=='__main__':
    start_page=int(input("请输入起始页："))
    end_page=int(input("请输入结束页："))

    for page in range(start_page,end_page+1):

        #定制请求资源路径
        request=create_request(page)

        #获取响应内容
        content=get_content(request)

        #下载内容 
        down_load(page,content)

    



