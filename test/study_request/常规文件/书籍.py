import xml.dom.minidom

# 1、在内存中创建一个空的文档
doc = xml.dom.minidom.Document()

# 2、创建根元素
root = doc.createElement('collection ')
# print('添加的xml标签为：',root.tagName)

# 3、设置根元素的属性
root.setAttribute('type', 'New Arrivals')

# 4、将根节点添加到文档对象中
doc.appendChild(root)

# 5、创建子元素
book = doc.createElement('book')

# 6、添加注释
book.appendChild(doc.createComment('这是一条注释'))

# 7、设置子元素的属性
book.setAttribute('语言', 'java')

# 8、子元素中嵌套子元素，并添加文本节点
name = doc.createElement('name')
name.appendChild(doc.createTextNode('java基础'))
price = doc.createElement('价格')
price.appendChild(doc.createTextNode('99元'))
number = doc.createElement('number')
number.appendChild(doc.createTextNode('剩余100本'))

# 9、将子元素添加到boot节点中
book.appendChild(name)
book.appendChild(price)
book.appendChild(number)

# 10、将book节点添加到root根元素中
root.appendChild(book)

# 创建子元素
book = doc.createElement('book')

# 设置子元素的属性
book.setAttribute('语言', 'python')

# 子元素中嵌套子元素，并添加文本节点
name = doc.createElement('name')
name.appendChild(doc.createTextNode('python基础'))
price = doc.createElement('价格')
price.appendChild(doc.createTextNode('50元'))
number = doc.createElement('number')
number.appendChild(doc.createTextNode('剩余20本'))

#  将子元素添加到boot节点中
book.appendChild(name)
book.appendChild(price)
book.appendChild(number)

# 将book节点添加到root根元素中
root.appendChild(book)

print(root.toxml())

fp = open('./书籍.xml', 'w', encoding='utf-8')  # 需要指定utf-8的文件编码格式，不然notepad中显示十六进制
doc.writexml(fp, indent='', addindent='\t', newl='\n', encoding='utf-8')
fp.close()

