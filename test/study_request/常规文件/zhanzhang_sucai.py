#爬取站长素材前10页风景图片
import urllib.request
from lxml import etree

#请求资源路径
# url="https://sc.chinaz.com/tupian/fengjing.html"    #第一页网址
# url="https://sc.chinaz.com/tupian/fengjing_2.html"  #第二页网址
# url="https://sc.chinaz.com/tupian/fengjing_3.html"  #第三页网址

def create_request(page):
    if page==1:
        url="https://sc.chinaz.com/tupian/fengjing.html"
    else:
        data="https://sc.chinaz.com/tupian/fengjing_"
        url=data+str(page)+".html"
   
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
    }

    request=urllib.request.Request(url=url,headers=headers)

    return request
        
def get_content(request):
    respense=urllib.request.urlopen(request)
    content=respense.read().decode('utf-8')
    return content


def down_load(content):
    #解析下载图片的地址
    tree=etree.HTML(content)

    name_list=tree.xpath('//div[@class="item masonry-brick"]//img/@alt')

    src_list=tree.xpath('//div[@class="item masonry-brick"]//img/@src')

    for i in range(len(name_list)):
        name=name_list[i]
        src=src_list[i]
        url="https:"+src

        urllib.request.urlretrieve(url=url,filename='./picture/' + name + '.jpg')




if __name__=='__main__':
    start_page=int(input("请输入起始页："))
    end_page=int(input("请输入结束页："))
                       
    for page in range(start_page,end_page+1):
        #请求对象的定制
        request=create_request(page)
        #获取响应内容
        content=get_content(request)
        #下载图片
        down_load(content)
 
