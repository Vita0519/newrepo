import requests

from lxml import etree

s=requests.Session()
url='https://www.qb5.tw/login.php?do=submit'

headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.50"
}

#获取验证码图片链接
r=s.get(url=url,headers=headers,params={'do': 'submit'}).text
tree=etree.HTML(r)
code_link="https://www.qb5.tw"+tree.xpath('//*[@id="main"]/div[1]/form/fieldset/p[3]//@src')[0]
print(code_link)
#下载验证码图片
code_img=s.get(url=code_link,headers=headers).content
with open('code.png','wb') as fp:
    fp.write(code_img)
#利用ddddocr识别验证码
import ddddocr

ocr = ddddocr.DdddOcr()
with open('code.png', 'rb') as f:
    img_bytes = f.read()
res = ocr.classification(img_bytes)
print('识别出的验证码为：' + res)
code=res
data={
    "username":"13733560730",
    "password": "13733560730",
    "checkcode": code,
    "usecookie": "315360000",
    "action": "login",
    "submit": "(无法对值进行解码)"
}
response=s.post(url=url,headers=headers,data=data).text

with open('qb.html','w',encoding='utf_8') as fp:
    fp.write(response)



