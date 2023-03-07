from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
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
time.sleep(1)

#获取网页源码,第一页
page_list=[browser.page_source]

for i in range(3):
    browser.maximize_window()
    # 滑动到最底部
    import pyautogui
    pyautogui.scroll(-200)
    #点击下一页
    button1 = browser.find_element(By.XPATH,'//div/div[3]/div/div[3]/div/button[2]').click()
    time.sleep(2)
    time.sleep(500)
    page_list.append(browser.page_source)

for x in page_list:
    Aa = browser.find_elements(By.XPATH, "//div[@class='container']//div[@class='doc-item']")
    for a in Aa:
        time.sleep(2)
        button2 = a.find_element(By.XPATH, ".//*[name()='svg'][1]")
        time.sleep(6 * random.random())  # 在两次请求之间间隔0~6秒的随机时间
        button2.click()










# Aa= browser.find_elements(By.XPATH,"//div[@class='container']//div[@class='doc-item']")
# for a in Aa:
#     time.sleep(2)
#     button2 = a.find_element(By.XPATH,".//*[name()='svg'][1]")
#     time.sleep(6 * random.random())  # 在两次请求之间间隔0~6秒的随机时间
#     button2.click()
#
# browser.save_screenshot('handless1.png')
#
# time.sleep(10)

