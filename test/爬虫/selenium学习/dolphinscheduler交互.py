
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import random

# 创建浏览器对象
path = '../chromedriver.exe'
browser = webdriver.Chrome(path)

# url
url = 'http://19.105.194.188:12345/dolphinscheduler/ui/projects/7890446543488/workflow/instances'
browser.get(url)

import time
time.sleep(1)

# 获取文本框的对象
input = browser.find_element(By.XPATH," //input[@type='text']").send_keys('szjt_user')

time.sleep(0.5)


# 获取密码的按钮
button = browser.find_element(By.XPATH," //input[@type='password']").send_keys("szjt123456")

time.sleep(0.5)

#获取登录按钮
button1 = browser.find_element(By.XPATH,"//button[@type='button']")
# 点击登录按钮
button1.click()

time.sleep(0.5)


# 获取创建项目的按钮
button2 = browser.find_element(By.XPATH,"//div[@role='none' and @class='n-menu-item-content n-menu-item-content--selected']")

# 点击按钮
button2.click()

time.sleep(0.5)
#获取测试的按钮
button3 = browser.find_element(By.XPATH,"//tr[@class='n-data-table-tr items'][2]/"
                                        "td[@class='n-data-table-td project-name']/"
                                        "button[@class='n-button n-button--default-type "
                                        "n-button--medium-type _button-link_cj1bz_17']"
                                        "/span[@class='n-button__content']/span[@class='n-ellipsis']/span")

# 点击按钮
button3.click()

time.sleep(0.5)

#获取创建项目的按钮
button4 = browser.find_element(By.XPATH,"//div[@class='n-submenu'][1]/div[@class='n-submenu-children']/"
                                        "div[@class='n-menu-item'][2]/div[@class='n-menu-item-content']/div[@class='n-menu-item-content-header']")
# 点击按钮
button4.click()

time.sleep(0.5)

#获取创建工作流的按钮
button5 = browser.find_element(By.XPATH,"//button[@class='n-button n-button--primary-type "
                                        "n-button--small-type btn-create-process']/span[@class='n-button__content']")
# 点击按钮
button5.click()
time.sleep(0.5)

# #当前页
# action=ActionChains(browser)
browser.maximize_window()
time.sleep(2*random.random())
#拖拽sql处理数据
div1= browser.find_element(By.XPATH,"//div[@class='_content_f8taq_22']"
                                       "/div[@class='_sidebar_f8taq_59']/div[@class='_draggable_f8taq_75 task-item-SQL']")


# ActionChains(browser).drag_and_drop(div1,div2).perform()
# ActionChains(browser).click_and_hold(div1).move_by_offset(550, 300).release().perform()
# action.drag_and_drop_by_offset(div1,535,300).perform()

# start=div1.location
# finish=div2.location
# ActionChains(browser).click_and_hold(div1).move_by_offset(535, 300).release().perform()
# print(start,finish)

time.sleep(0.5)

# 截图
# browser.save_screenshot('handless1.png')

# 滑到底部
# js_bottom = 'document.documentElement.scrollTop=100000'
# browser.execute_script(js_bottom)
# # 回到上一页
# browser.back()
# # 回去
# browser.forward()
# 退出
# browser.quit()

import pyautogui
# # 定位起始元素
# source = driver.find_element_by_xpath('')
# # 让鼠标移动到起点元素上
# pyautogui.moveTo(source .location['x']+20, source .location['y']+125)
# # 定位要拖拽到的位置元素
# target= driver.find_element_by_xpath('')
# # 实现拖拽功能
# pyautogui.dragTo(target.location['x']+20, target.location['y']+155, duration=1)
# 让鼠标移动到起点元素上
pyautogui.moveTo(div1.location['x']+350, div1 .location['y']+550)
# 获取鼠标位置
# x,y = pyautogui.position()
# print(x,y)
# 实现拖拽功能
# div2= browser.find_element(By.XPATH,"//div[@class='x6-graph-scroller']")
# pyautogui.dragTo(div2.location['x']+1000, div2.location['y']+700, duration=1)
pyautogui.dragTo(div1.location['x']+1000, div1.location['y']+700, duration=0.5)

time.sleep(0.5)

#填写节点名称
button6 = browser.find_element(By.XPATH,"//div/div[3]/div[2]/div/div/form/div/div[1]/div/div[1]/div/div[1]/div/input").send_keys("sql测试")
time.sleep(0.5)
# 填写描述信息
button7= browser.find_element(By.XPATH,"//div/div/form/div/div[3]/div/div[1]/div/div[1]/div/textarea").send_keys("无")
time.sleep(10000)