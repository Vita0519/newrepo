import os
import ddddocr
from time import sleep
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By


class GetVerificationCode:
    def __init__(self):
        self.res = None

    url = '要登录的地址'
    self.driver = webdriver.Chrome()
    self.driver.maximize_window()  # 将浏览器最大化
    self.driver.get(url)

    # 获取验证码信息


def getVerification(self):
    # 获取当前文件的位置、并获取保存截屏的位置
    current_location = os.path.dirname(__file__)
    screenshot_path = os.path.join(current_location, "..", "VerificationCode")
    # 截取当前网页并放到自定义目录下，并命名为printscreen，该截图中有我们需要的验证码
    sleep(1)
    self.driver.save_screenshot(screenshot_path + '//' + 'printscreen.png')
    sleep(1)
    # 定位验证码
    imgelement = self.driver.find_element(By.XPATH, '验证码图片的Xpath定位')
    # 获取验证码x,y轴坐标
    location = imgelement.location
    # 获取验证码的长宽
    size = imgelement.size
    # 写成我们需要截取的位置坐标
    rangle = (int(location['x'] + 430),
              int(location['y'] + 200),
              int(location['x'] + size['width'] + 530),
              int(location['y'] + size['height'] + 250))
    # 打开截图
    i = Image.open(screenshot_path + '//' + 'printscreen.png')
    # 使用Image的crop函数，从截图中再次截取我们需要的区域
    fimg = i.crop(rangle)
    fimg = fimg.convert('RGB')
    # 保存我们截下来的验证码图片，并读取验证码内容
    fimg.save(screenshot_path + '//' + 'code.png')
    ocr = ddddocr.DdddOcr()
    with open(screenshot_path + '//' + 'code.png', 'rb') as f:
        img_bytes = f.read()
    self.res = ocr.classification(img_bytes)
    print('识别出的验证码为：' + self.res)

    # 判断验证码错误时的提示信息是否存在


def isElementPresent(self, by, value):
    try:
        element = self.driver.find_element(by=by, value=value)
    except NoSuchElementException:
        pass
        # 发生了NoSuchElementException异常，说明页面中未找到该元素，返回False
        return False
    else:
        # 没有发生异常，表示在页面中找到了该元素，返回True
        return True

    # 登录


def login(self):
    self.getVerification()
    self.driver.find_element(By.XPATH, '用户名输入框Xpath定位').send_keys('用户名')
    self.driver.find_element(By.XPATH, '密码输入框Xpath定位').send_keys('密码')
    self.driver.find_element(By.XPATH, '验证码输入框Xpath定位').send_keys(self.res)
    sleep(1)
    self.driver.find_element(By.XPATH, '登录按钮Xpath定位').click()
    sleep(2)
    isFlag = True


while isFlag:
    try:
        isPresent = self.isElementPresent(By.XPATH, '验证码错误时的提示信息Xpath定位')
        if isPresent is True:
            codeText = self.driver.find_element(By.XPATH, '验证码错误时的提示信息Xpath定位').text
            if codeText == "验证码不正确":
                self.getVerification()
                sleep(2)
                self.driver.find_element(By.XPATH, '验证码输入框Xpath定位').clear()
                sleep(1)
                self.driver.find_element(By.XPATH, '验证码输入框Xpath定位').send_keys(self.res)
                sleep(1)
                self.driver.find_element(By.XPATH, '登录按钮Xpath定位').click()
                sleep(2)
            tips = self.driver.find_element(By.XPATH,
                                            '未输入验证码时的提示信息Xpath定位').text
            if tips == "请输入验证码":
                self.getVerification()
                sleep(2)
                self.driver.find_element(By.XPATH, '验证码输入框Xpath定位').click()
                sleep(1)
                self.driver.find_element(By.XPATH, '验证码输入框Xpath定位').send_keys(self.res)
                sleep(1)
                self.driver.find_element(By.XPATH, '登录按钮Xpath定位').click()
                sleep(2)
            continue
        else:
            print("验证码正确，登录成功！")
    except NoSuchElementException:
        pass
    else:
        isFlag = False

sleep(5)
self.driver.quit()

if __name__ == '__main__':
    GetVerificationCode().login()
