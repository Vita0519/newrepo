#连接数据库
import pymysql

mydb = pymysql.connect(host='localhost',
                       port=3306,
                       user='root',
                       passwd='123456',
                       database='test'
                       )
# #使用 cursor() 方法创建一个游标对象 cursor
# mycursor=mydb.cursor()
# # 使用 execute() 方法执行 SQL，创建表
# mycursor.execute('create table ts1(name varchar(8),age int,sex varchar(1))engine=innodb default charset=utf8')

# #创建book表
# mycursor=mydb.cursor()
# sql='create table book(name varchar(128),src varchar(128))'
# mycursor.execute(sql)

#重命名book的表列名
mycursor=mydb.cursor()
sql="alter table book rename column name to n"
mycursor.execute(sql)

# 查询并打印表数据
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM book")
myresult = mycursor.fetchall()  #用了fetchall() 方法，该方法从最后执行的语句中获取所有行。
for x in myresult:
  print(x)

# #使用 cursor() 方法创建一个游标对象 cursor
# mycursor = mydb.cursor()
# # 使用 execute() 方法执行 SQL
# mycursor.execute("SHOW TABLES")
#
# for x in mycursor:
#   print(x)

# #使用 cursor() 方法创建一个游标对象 cursor
# mycursor = mydb.cursor()
# # 使用 execute() 方法执行 SQL 添加列
# mycursor.execute("ALTER TABLE ts ADD id int(10)")

# mycursor = mydb.cursor()
# # 使用 execute() 方法执行 SQL 删除列
# mycursor.execute("ALTER TABLE test1 drop column id")


# #重命名表
# mycursor = mydb.cursor()
# mycursor.execute("RENAME TABLE ts TO test1")

# 插入数据
# mycursor = mydb.cursor()
# mycursor.execute("insert into test1(name,age,sex) values ('张三',18,'男')")
# mydb.commit() #插入、删除必须要提交

# 插入多行数据
# mycursor = mydb.cursor()
# sql = "INSERT INTO test1 (name,age,sex) VALUES (%s,%s,%s)"
# val = [
#   ('李四',48,'男'),
#   ('王五',38,'女'),
#   ('赵六',19,'男')
# ]
# mycursor.executemany(sql, val) #执行多个任务mycursor.executemany()
# mydb.commit()
# print(mycursor.rowcount,"record was inserted.")  #打印出插入数据条数记录

# try:
#     mycursor = mydb.cursor()
#     sql = "INSERT INTO test1 (name,age,sex) VALUES (%s,%s,%s)"
#     val = [
#         ('田七',26,'女'),
#         ('高启强',36, '男'),
#         ('高启盛',30,'男'),
#         ('程程',26,'女'),
#         ('陈书婷',26,'女'),
#         ('李有田',56,'男'),
#         ('迈克尔.杰克驴',33,'男'),
#         ('麻子',29,'男'),
#         ('徐雷',40,'男'),
#         ('老默',42,'男'),
#         ('高圆圆',38,'女')
#     ]
#     mycursor.executemany(sql, val) #执行多个任务mycursor.executemany()
#     mydb.commit()
#     print(mycursor.rowcount,"record was inserted.")  #打印出插入数据条数记录
# except Exception:
#     print("插入数据失败")


# # 查询并打印表数据
# mycursor = mydb.cursor()
# mycursor.execute("SELECT * FROM test1")
# myresult = mycursor.fetchall()  #用了fetchall() 方法，该方法从最后执行的语句中获取所有行。
# for x in myresult:
#   print(x)

# #选取指定列
# mycursor=mydb.cursor()
# mycursor.execute("select name,age from test1")
# myresult=mycursor.fetchall()

# for X in myresult:
#     print(X)

# #选取指定列的一行数据
# mycursor=mydb.cursor()
# mycursor.execute("select name,age from test1")
# mycursult=mycursor.fetchone()
# print(mycursult)

# #where 筛选数据
# mycursor=mydb.cursor()
# sql="select * from test1 where name='张三'"
# mycursor.execute(sql)
# myresult=mycursor.fetchmany(size=1)  #fetchmany()方法获取指定行数
# for x in myresult:
#     print(x)

#like模糊查询
# mycursor=mydb.cursor()
# sql="select * from test1 where name like '%三'"
# mycursor.execute(sql)
# myresult=mycursor.fetchall()
# for x in myresult:
#     print(x)

# #使用占位符进行转义
# mycursor = mydb.cursor()
# sql = "SELECT * FROM test1 WHERE name = %s"
# nam = ("王五", )   #nam是元组类型，只有一个数据是必须要有”,“
# mycursor.execute(sql,nam)
# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x)
#
# print(type(nam))

#删除重复数据
# try:
#     mycursor=mydb.cursor()
#     sql="select distinct * from test1 "
#     mycursor.execute(sql)
#     myresult=mycursor.fetchall()
#     for x in myresult:
#        print(x)
# except Exception:
#     print("查询失败")

# #排序
# try:
#     mycursor=mydb.cursor()
#     sql="select * from test1 order by age desc"
#     mycursor.execute(sql)
#     myresult=mycursor.fetchall()
#     for x in myresult:
#         print(x)
# except Exception:
#     print("排序失败")

# #删除行数据
# try:
#     mycursor=mydb.cursor()
#     sql="delete from test1 where name='张三'"
#     mycursor.execute(sql)
#     mydb.commit()
#     print(mycursor.rowcount,"record(s) deleted")  #查询删除记录条数
# except Exception:
#     print('删除失败')

#------------------------------------------------------------------------------------
#update更新数据
#方法一
# try:
#     mycursor=mydb.cursor()
#     sql="update test1 set name='王六' where name='王五'"
#     mycursor.execute(sql)
#     mydb.commit()
#     print(mycursor.rowcount,"record(s) affected")  #查询更新记录条数
# except Exception:
#     print('更新失败')

#方法二,利用s%占位符，防止sql注入
# try:
#     mycursor=mydb.cursor()
#     sql="update test1 set name=%s where name=%s"
#     val=("王五","王六")
#     mycursor.execute(sql,val)
#     mydb.commit()
#     print(mycursor.rowcount,'record(s) affected')
# except Exception:
#     print("更新失败")
#--------------------------------------------------------------------------
#limit查询前几条数据
# try:
#     mycursor=mydb.cursor()
#     sql="select * from test1 limit 3"
#     mycursor.execute(sql)
#     myresult=mycursor.fetchall()
#     for x in myresult:
#         print(x)
# except Exception:
#     print("查询失败")
#-------------------------------------------------------
# offset关键字：从另一个位置开始
# try:
#     mycursor=mydb.cursor()
#     sql="select * from test1 limit 5 offset 2"  #offset从另一个位置开始的关键字，此例表示从位置3开始返回5条数据
#     mycursor.execute(sql)
#     myresult=mycursor.fetchall()
#     for x in myresult:
#         print(x)
# except Exception:
#     print("查询失败")


#---------------------------------------------------------------------------------
#新建两个表
#表1，users
# try:
#     mycursor=mydb.cursor()
#     create="create table users(id int(5),name varchar(10),fav int(5))"
#     mycursor.execute(create)
# except Exception:
#     print("创建表失败")

# #更改表users中fav的属性
# mycursor=mydb.cursor()
# sql="alter table users modify fav varchar(5)"
# mycursor.execute(sql)

# mycursor=mydb.cursor()
# sql="insert into users(id,name,fav) values(%s,%s,%s)"
# val=[
#     (1,'John',154),
#     (2,'Peter',154),
#     (3,'Amy',155),
#     (4,'Hannah',['null']),
#     (5,'Michael',['null'])
# ]
# mycursor.executemany(sql,val)
# mydb.commit()
# myrelust=mycursor.fetchall()
#
# for x in myrelust:
#     print(x)

# #查询users数据
# mycursor=mydb.cursor()
# sql="select * from users"
# mycursor.execute(sql)
# myresult=mycursor.fetchall()
# for x in myresult:
#     print(x)

#创建表2,products
# mycursor=mydb.cursor()
# mycursor.execute("create table products(id int(5),name varchar(30))")

# mycursor=mydb.cursor()
# sql="insert into products values(%s,%s)"
# val=[
#     (154,'Chocolate Heaven'),
#     (155,'Tasty Lemons'),
#     (156,'Vanilla Dreams')
# ]
# mycursor.executemany(sql,val)
# mydb.commit()

# mycursor=mydb.cursor()
# mycursor.execute("select * from products")
# myresult=mycursor.fetchall()
# for x in myresult:
#     print(x)


# #连接users表和products表
# mycursor=mydb.cursor()
# sql="select \
# users.name AS user,\
# products.name AS favorite \
# from users \
# inner join products on users.fav = products.id"  #内连接、左连接、右连接
#
# mycursor.execute(sql)
# myresult=mycursor.fetchall()
# for x in myresult:
#     print(x)

#关闭游标
mycursor.close()
#关闭数据库连接
mydb.close()