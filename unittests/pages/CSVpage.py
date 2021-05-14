# -*- coding: utf-8 -*-
# @Time : 2021/3/5 15:13
# @Author : Mr.WANG
# @Version : 
# @Function :封装CSV函数
import os
import xlrd
import xlwt
from xlutils.copy import copy

basepath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 获取项目路径
datapath = os.path.join(basepath, 'data')  # 获取测试数据文件路径
reportpath = os.path.join(basepath, 'report')
logpath = os.path.join(basepath, 'log')
pagepath = os.path.join(basepath, 'pages')
testcasepath = os.path.join(basepath, 'testcase')
utilspath = os.path.join(basepath, 'utils')


def getdata(file):  # 读取csv文件数据
    datas = []
    d = xlrd.open_workbook(file)
    table = d.sheet_by_index(0)
    hs = table.nrows
    for i in range(1, hs):
        datas.append(table.row_values(i))
    return datas


def setdata(file, data, row, column):  # 写入csv文件数据
    """

    :param file: 文件路径
    :param data: 写入数据
    :param row: 行号
    :param column: 列号
    :return:
    """
    if os.path.exists(file):
        r_xls = xlrd.open_workbook(file)  # 读取excel文件
        excel = copy(r_xls)  # 将xlrd的对象转化为xlwt的对象
        table = excel.get_sheet(0)  # 获取要操作的sheet
        table.write(row, column, data)  # 括号内分别为行数、列数、内容
        excel.save(file)  # 保存并覆盖文件

    else:
        wa = xlwt.Workbook()
        b=wa.add_sheet('sheet')
        wa.save(file)
        setdata(file, data, row, column)


if __name__ == '__main__':
    file = datapath + '/logindata.csv'
    data = getdata(file)
    print(data)
    for i in data:
        print(i)
