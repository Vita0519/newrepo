import xml.dom.minidom
from xml.dom.minidom import parse

# 对book.xml新增一个子元素english，并删除math元素
xml_file = './书籍.xml'

# 拿到根节点
domTree = parse(xml_file)
rootNode = domTree.documentElement

# rootNode.removeChild(rootNode.getElementsByTagName('book')[0])
# print(rootNode.toxml())

# 在内存中创建一个空的文档
doc = xml.dom.minidom.Document()

book = doc.createElement('book')
book.setAttribute('语言', 'c++')

# 子元素中嵌套子元素，并添加文本节点
name = doc.createElement('name')
name.appendChild(doc.createTextNode('c++基础'))
price = doc.createElement('价格')
price.appendChild(doc.createTextNode('200元'))
number = doc.createElement('number')
number.appendChild(doc.createTextNode('剩余300本'))

#  将子元素添加到boot节点中
book.appendChild(name)
book.appendChild(price)
book.appendChild(number)

math_book = rootNode.getElementsByTagName('book')[0]

# insertBefore方法  父节点.insertBefore(新节点，父节点中的子节点)
rootNode.insertBefore(book, math_book)

# appendChild将新产生的子元素在最后插入
rootNode.appendChild(book)

print(rootNode.toxml())

with open(xml_file, 'w', encoding='utf-8') as fh:
    domTree.writexml(fh, indent='', addindent='\t', newl='', encoding='utf-8')
