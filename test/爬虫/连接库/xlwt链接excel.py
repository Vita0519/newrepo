# -*- coding: utf-8 -*-

# 写excel
import xlwt


class WriteExcel:

    # 初始化
    def __init__(self, filename, sheet_name):
        self.work_book = xlwt.Workbook(encoding="UTF-8")
        self.worksheet = self.work_book.add_sheet(sheet_name)
        self.filename = filename
        self.row = 0

    # 保存Excel
    def save(self):
        self.work_book.save(self.filename)

    # 设置样式
    def set_style(self, name, height, bold=False, format_str='', align='center'):
        style = xlwt.XFStyle()  # 初始化样式
        font = xlwt.Font()  # 为样式创建字体
        font.name = name  # 字体
        font.bold = bold
        font.height = height

        borders = xlwt.Borders()  # 为样式创建边框
        borders.left = 1
        borders.right = 1
        borders.top = 1
        borders.bottom = 1

        alignment = xlwt.Alignment()  # 设置排列
        if align == 'center':
            alignment.horz = xlwt.Alignment.HORZ_CENTER
            alignment.vert = xlwt.Alignment.VERT_CENTER
        elif align == 'left':
            alignment.horz = xlwt.Alignment.HORZ_LEFT
            alignment.vert = xlwt.Alignment.VERT_BOTTOM
        else:
            alignment.horz = xlwt.Alignment.HORZ_RIGHT
            alignment.vert = xlwt.Alignment.VERT_BOTTOM

        style.font = font
        style.borders = borders
        style.num_format_str = format_str
        style.alignment = alignment
        return style

    # 设置标题的格式
    def set_title_style(self):
        return self.set_style('黑体', 300, bold=True, format_str='')

    # 设置表头的格式
    def set_head_style(self):
        head_style = self.set_style('Times New Roman', 220, bold=True, format_str='')
        pattern = xlwt.Pattern()  # 一个实例化的样式类
        pattern.pattern = xlwt.Pattern.SOLID_PATTERN  # 固定的样式
        pattern.pattern_fore_colour = xlwt.Style.colour_map['yellow']  # 背景颜色
        head_style.pattern = pattern
        return head_style

    # 设置明细行的格式
    def set_default_style(self):
        return self.set_style('Times New Roman', 200, bold=False, format_str='', align='right')

    # 添加标题
    def add_title(self, title):
        self.worksheet.write_merge(0, 0, 0, 2, title, self.set_title_style())
        self.row += 1

    # 写入文件头
    def add_head(self, key, value):
        # 向单元格中写入内容
        self.worksheet.write(self.row, 0, key)
        self.worksheet.write(self.row, 1, value)
        self.row += 1

    # 写入明细
    def add_list(self, table_head, table_detail):
        self.row += 1
        for i, value in enumerate(table_head):
            self.worksheet.write(self.row, i, value, self.set_head_style())
            self.worksheet.col(i).width = 150 * 30
        for rows in table_detail:
            self.row += 1
            for i, key in enumerate(rows):
                self.worksheet.write(self.row, i, rows[key], self.set_default_style())


if __name__ == "__main__":
    list_head = ["学号", "姓名", "性别"]
    list_detail = [{"student_id": "1001", "name": "张三", "sex": "男"},
                   {"student_id": "1002", "name": "李四", "sex": "女"},
                   {"student_id": "1003", "name": "王五", "sex": "男"}]

    writeExcel = WriteExcel("writeExcel.xlsx", "学生信息")
    writeExcel.add_title("XX班级学生信息表")
    writeExcel.add_head("学院名：", "A学院")
    writeExcel.add_head("班级名：", "B系一班")
    writeExcel.add_head("人数：", "50")
    writeExcel.add_list(list_head, list_detail)
    writeExcel.save()
