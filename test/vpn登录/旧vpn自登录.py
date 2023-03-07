import requests
import ddddocr
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By

# 创建浏览器对象
path = '../chromedriver.exe'
browser = webdriver.Chrome(path)

s=requests.Session()

url='https://dgvpn.dg.cn/prx/000/http/dxyzm.dg/weblogin'
browser.get(url)

headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.50"
}

time.sleep(2*random.random())

button1=browser.find_element(By.XPATH,"//*[@id='uname']").send_keys('13733560730')
time.sleep(2*random.random())
button2=browser.find_element(By.XPATH,'//*[@id="pwd"]').send_keys('403420')
time.sleep(2*random.random())

#下载验证码图片，首先要点击刷新才能获取图片链接
button3=browser.find_element(By.XPATH,'//*[@id="captchaImage"]').click()
time.sleep(2*random.random())
#图片链接
code_link=browser.find_element(By.XPATH,'//*[@id="captchaImage"]').get_attribute("src")  #获取属性值 .text可以获取文本内容
print(code_link)

#切换窗口
a=browser.current_window_handle
browser.execute_script('window.open()')
browser.switch_to.window(browser.window_handles[1])
browser.get(code_link)

button4=browser.find_element(By.XPATH,'/html/body/div/div[2]/table/tbody/tr[2]/td/form/table/tbody/tr/td[3]/input').click()

# 切换窗口
b=browser.current_window_handle
browser.execute_script('window.open()')
browser.switch_to.window(browser.window_handles[2])
browser.get(code_link)

#下载验证码图片
browser.save_screenshot('code.png')

ocr = ddddocr.DdddOcr()
with open('code.png', 'rb') as f:
    img_bytes = f.read()
res = ocr.classification(img_bytes)
print('识别出的验证码为'+res)

#切换回第一个窗口
browser.switch_to.window(a)

input=browser.find_element(By.XPATH,'//*[@id="captchaCode"]').send_keys(res)

button5=browser.find_element(By.XPATH,'//*[@id="userForm"]/button').click()

#启动连接vpn
button6=browser.find_element(By.XPATH,'//*[@id="vpnOn"]').click()

time.sleep(200)






