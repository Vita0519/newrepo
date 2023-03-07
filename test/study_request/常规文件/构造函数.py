from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()



class People():
    name = "人"

    def __init__(self, n="非洲人"):
        self.name = n
        print("我是构造函数", self.name)  # 重写构造函数

    def __del__(self):
        print("我是析构函数", self.name)  # 重写析构函数


zhangsan = People()
lisi = People("欧美人")
zhangsan.__del__()  # 调用析构函数
print(zhangsan)
del zhangsan
