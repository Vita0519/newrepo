import pymysql   #连接数据库
import requests  # 爬虫requests模块
import re  # 正则匹配模块
import json  # 接送模块，能把类字典的字符串干成字典，能把字典字符串干成字典，反正很强大


index_tuple = []  # 建立一个空列表放爬出来的数据
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}  # 复制过来一个'user-agent'让爬虫模拟用户的更逼真一些，还可以用cookie，代理IP（免费的已经用烂了）
rule = r'quote: (.*),'  # 指定正则匹配规则，看一下网页源码数据，自己需求的数据开头是啥，结尾是啥，然后匹配出来
response = requests.get('https://xueqiu.com/S/SH000001', headers=headers)  # 发一个get请求，post请求需要交互参数，比如你要输入一个验证码啥的
result = re.findall(rule, response.text)  # 把我们的结果匹配出来，匹配出来是个['{目标数据}']这个类型
data = result[0]  # 从列表里拿出来'{目标数据}'
data1 = json.loads(data)  # 用json还原成字典，然后根据key就可以获得value，一下就是重复爬虫部分和第一部分的连接
index_tuple.extend([float(data1['current']), data1['amount'] / 100000000])
response = requests.get('https://xueqiu.com/S/SZ399006', headers=headers)
result = re.findall(rule, response.text)
data = result[0]
data1 = json.loads(data)
index_tuple.extend([float(data1['current']), data1['amount'] / 100000000])
index_list = []
asd = round(index_tuple[1] + index_tuple[3], 2)
date = '2023-02-16'
db = pymysql.Connect(host='localhost', port=3306, user='root',  # 连接数据库MySQL
                     passwd='123456', database='test', charset='utf8')


#建表语句
# cursor=db.cursor()
# sql="create table t_index(日期 date, 上证指数 float,创业板指数 float, 2市成交额 float, 创业板成交额 float)"
# cursor.execute(sql)

# print(index_tuple)


cursor = db.cursor()
sql = "insert into t_index(日期, 上证指数, 创业板指数, 2市成交额, 创业板成交额)" \
      " values('%s', '%.2f', '%.2f', '%.2f', '%.2f')" % (date, index_tuple[0], index_tuple[2], asd, index_tuple[3])
cursor.execute(sql)
db.commit()
cursor.close()
db.close()
