from selenium import webdriver
#这个是浏览器自带的 不需要我们再做额外的操作
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


def share_browser():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')

    # path是你自己的chrome浏览器的文件路径
    path = r'C:\Users\15457\AppData\Local\Google\Chrome\Application\chrome.exe'
    chrome_options.binary_location = path

    browser = webdriver.Chrome(chrome_options=chrome_options)
    return browser

browser = share_browser()

browser.get('http://19.105.194.188:12345/dolphinscheduler/ui/projects/7890446543488/workflow/instances')

time.sleep(2)

# 获取文本框的对象
input = browser.find_element(By.XPATH," //input[@type='text']").send_keys('szjt_user')
time.sleep(2)

# 获取密码的按钮
button = browser.find_element(By.XPATH," //input[@type='password']").send_keys("szjt123456")
time.sleep(2)

#获取登录按钮
button1 = browser.find_element(By.XPATH,"//button[@type='button']")
# 点击登录按钮
button1.click()
time.sleep(2)
browser.save_screenshot('handless1.png')

# 获取创建项目的按钮
button2 = browser.find_element(By.XPATH,"//div[@role='none' and @class='n-menu-item-content n-menu-item-content--selected']")

# 点击按钮
button2.click()
time.sleep(2)
#获取测试的按钮
button3 = browser.find_element(By.XPATH,"//span[@class='n-button__content']/span[@class='n-ellipsis']/span")
# 点击按钮
button3.click()
time.sleep(2)

#获取创建项目的按钮
button4 = browser.find_element(By.XPATH,"//div[@class='n-submenu'][1]/div[@class='n-submenu-children']/div[@class='n-menu-item'][2]/div[@class='n-menu-item-content']/div[@class='n-menu-item-content-header']")
# 点击按钮
button4.click()
time.sleep(2)

#获取创建工作流的按钮
button5 = browser.find_element(By.XPATH,"//button[@class='n-button n-button--primary-type n-button--small-type btn-create-process']/span[@class='n-button__content']")
# 点击按钮
button5.click()
browser.save_screenshot('handless1.png')
time.sleep(100000)
# # 滑到底部
# js_bottom = 'document.documentElement.scrollTop=100000'
# browser.execute_script(js_bottom)

# # 回到上一页
# browser.back()
# # 回去
# browser.forward()
# 退出
# browser.quit()