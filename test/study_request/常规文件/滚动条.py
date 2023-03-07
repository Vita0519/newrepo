from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.maximize_window()
sleep(5)
driver.find_element(By.ID, 'kw').send_keys('python')
driver.find_element(By.ID, 'su').click()
sleep(2)
js="var q=document.documentElement.scrollTop=5000"
driver.execute_script(js)

sleep(50)