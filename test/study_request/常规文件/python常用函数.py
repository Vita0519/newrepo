# import random
#
# print("没有设定种子时")
# for i in range(5):
#     ret = random.randint(1, 10)
#     print(ret, end=" ")
# print()
#
# print("设定种子时")
# random.seed(1)
# for i in range(5):
#     ret = random.randint(1, 10)
#     print(ret, end=" ")

# import time
# a=time.gmtime()
# print(a)
#
# print('今天是{}-{}-{}'.format(time.gmtime()[0],time.gmtime()[1],time.gmtime()[2]))
#
# print(time.ctime())
#
# import datetime
#
# print(datetime.datetime.today())

# import calendar
# print(calendar.prcal(2023))

import calendar
# 设置星期2为每周第一天
# calendar.setfirstweekday(firstweekday=0)
# print(calendar.prcal(2023))

#判断是否平年，true为闰年，false为平年
# print(calendar.isleap(2023))

# import logging
#
# # 默认的日志输出级别为warning
# logging.debug('This is debug log')  # 调试级别
# logging.info('This is info log')  # 信息级别
# logging.warning('This is warning log')  # 警告级别
# logging.error('This is error log')  # 错误级别
# logging.critical('This is critical log')  # 严重错误级别


import json

person = {"name": "小明", "age": 30, "tel": ["888888", "1351111111"], "isonly": True}

json.dump(person, open('data.json', 'w'), sort_keys=True, indent=4, separators=(',', ': '))
