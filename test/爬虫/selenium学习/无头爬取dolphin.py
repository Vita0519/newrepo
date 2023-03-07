from selenium import webdriver
from selenium.webdriver.chrome.options import Options
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

#此链接要在vpn条件下才能打开
url = 'http://19.105.194.188:12345/dolphinscheduler/ui/projects/7890446543488/workflow/instances'


browser.get(url)
# time.sleep(10)
# browser.save_screenshot('baidu.png')
a=browser.current_window_handle
browser.switch_to.window(a)

