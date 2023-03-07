
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import random

# 创建浏览器对象
path = '../chromedriver.exe'
browser = webdriver.Chrome(path)

# url
url = 'https://data.gdgov.cn/index/#/portal-relation/doc_download'
browser.get(url)

import time

time.sleep(2)

# 点击标准规范
button = browser.find_element(By.XPATH,"//li[@class='doc-card'][2]/div[@class='doc-card-header']/h2/span[1]")
button.click()
time.sleep(2)

#获取到当前页面
browser.switch_to.window(browser.window_handles[1])

# button1 = browser.find_element(By.XPATH,"//div[@class='container']//div[@class='doc-item'][1]//*[name()='svg'][1]")
# #悬停后点击
# ActionChains(browser).move_to_element(button1).move_by_offset(5,5).click().perform()
# time.sleep(5)

Aa= browser.find_elements(By.XPATH,"//div[@class='container']//div[@class='doc-item']")
for a in Aa:
    time.sleep(2)
    button2 = a.find_element(By.XPATH,".//*[name()='svg'][1]")
    time.sleep(6 * random.random())  # 在两次请求之间间隔0~6秒的随机时间
    button2.click()

browser.save_screenshot('handless1.png')

time.sleep(10)

# 滑到底部
# js_bottom = 'document.documentElement.scrollTop=100000'
# browser.execute_script(js_bottom)
# # 回到上一页
# browser.back()
# # 回去
# browser.forward()
# 退出
# browser.quit()