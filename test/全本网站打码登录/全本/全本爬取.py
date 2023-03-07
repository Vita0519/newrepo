import urllib.request

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import random

# 创建浏览器对象
path = '../chromedriver.exe'
browser = webdriver.Chrome(path)

url='https://www.qb5.tw/'
browser.get(url)

time.sleep(2*random.random())
button=browser.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/a[2]').click()
time.sleep(2*random.random())
den=browser.find_element(By.XPATH,'//*[@id="username"]').send_keys('13733560730')
time.sleep(2*random.random())
mima=browser.find_element(By.XPATH,'//*[@id="password"]').send_keys('13733560730')
time.sleep(3*random.random())


#获取当前页面源码
page=browser.page_source

from lxml import etree
import urllib.request
#获取验证码图片链接   验证码设置了随机函数，链接相同，图片也会改变
tree=etree.HTML(page)
code_link="https://www.qb5.tw"+tree.xpath('//*[@id="main"]/div[1]/form/fieldset/p[3]//@src')[0]
cd=urllib.request.urlretrieve(code_link,'code.png')

#利用ddddocr识别验证码
import ddddocr
ocr = ddddocr.DdddOcr()
with open('code.png', 'rb') as f:
    img_bytes = f.read()
res = ocr.classification(img_bytes)
print('识别出的验证码为：' + res)

code=browser.find_element(By.XPATH,'//*[@id="main"]/div[1]/form/fieldset/p[3]/input').send_keys(res)
time.sleep(2*random.random())
button1=browser.find_element(By.XPATH,'//*[@id="main"]/div[1]/form/fieldset/div/input[2]').click()


time.sleep(300)





