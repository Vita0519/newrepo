import xlwt

data_list = [('小白', '20', '男'), ('小黑', '21', '男'), ('小红', '20', '女')]
# 1. 创建Excel表对象
workbook = xlwt.Workbook(encoding='utf8')
# 2. 新建sheet表
worksheet = workbook.add_sheet('Sheet1')
# 3. 自定义列名
col1 = ('姓名', '年龄', '性别')
# 4. 将列属性元组col写进sheet表单中第一行
for i in range(0, len(col1)):
    worksheet.write(0, i, col1[i])
# 5. 将数据写进sheet表单中
# for i in range(0, len(data_list)):
#     data = data_list[i]
#     for j in range(0, len(col1)):
#         worksheet.write(i + 1, j, data[j])
# 5. 将数据写进sheet表单中
for i in range(0, len(data_list)):
    data = data_list[i]
    for j in range(0, len(col1)):
        worksheet.write(i + 1, j, data[j])
        # 6. 设置行高
        # worksheet.row(i + 1).height_mismatch = True
        # worksheet.row(i + 1).height = 1600  # 设置行高

# 6. 保存文件分两种格式
workbook.save('test.xls')

def body_style():
    # 一、创建一个样式对象，初始化样式 style
    style = xlwt.XFStyle()  # Create Style对象

    # 二、字体风格设置
    font = xlwt.Font()  # Create Font对象
    font.name = "SimSun"  # 设置字体类型，宋体
    font.colour_index = 4  # 设置字体颜色
    font.height = 20 * 12  # 字体大小，12为字号，20为衡量单位
    font.bont = True  # 设置字体加粗
    font.underline = True  # 下划线
    font.italic = True  # 斜体字

    # 二、背景设置
    pattern = xlwt.Pattern()
    pattern.pattern = xlwt.Pattern.SOLID_PATTERN  # May be: NO_PATTERN, SOLID_PATTERN, or 0x00 through 0x12
    pattern.pattern_fore_colour = 4  # 给背景颜色赋值

    # 三、边框设置
    borders = xlwt.Borders()  # 创建边框对象，    # .DASHED：虚线；.NO_LINE：没有
    # 上下左右都添加边框
    borders.left = 1
    borders.right = 1
    borders.top = 1
    borders.bottom = 1
    # 设置边框颜色
    borders.left_colour = 2
    borders.right_colour = 2
    borders.top_colour = 2
    borders.bottom_colour = 2

    # 四、位置设置
    alignment = xlwt.Alignment()
    alignment.horz = 1  # 设置水平位置，0是左对齐，1是居中，2是右对齐
    alignment.wrap = 1  # 设置自动换行

    # 五、设置好之后，全部都加到style上
    style.alignment = alignment
    style.font = font
    style.borders = borders
    return style

    sheet.write(row, column, i)  # 不带格式
    sheet.write(row, column, i, style)  # 有格式



