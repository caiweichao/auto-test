# -*- coding: utf-8 -*-
# @Author  : caiweichao
# @explain : 读取excel中的测试用例

import json

import openpyxl

from Commons.logs import Log
from ConfigFile import contants_file


class ReadExcel:
    def __init__(self):
        try:
            self.file_name = contants_file.TEST_DATA_PATH + 'TestCase.xlsx'
            Log.debug(f'打开测试用例数据文件：{self.file_name}')
            self.workbook = openpyxl.load_workbook(filename=self.file_name)
        except Exception:
            Log.error(f'打开测试用例数据文件异常{Exception}')
            raise Exception("文件打开异常请检查！")

    # 读取指定sheet页的数据放入testcase对象
    def get_testcase(self, sheetname: str):
        sheet = self.workbook[sheetname]
        max_row = sheet.max_row
        testcases: list = []
        for row in range(2, max_row + 1):
            # 构造测试用例
            testcase: dict = {'case_id': sheet.cell(row=row, column=1).value,
                              'case_title': sheet.cell(row=row, column=2).value,
                              'url': sheet.cell(row=row, column=3).value,
                              'data': json.loads(sheet.cell(row=row, column=4).value),
                              'method': sheet.cell(row=row, column=5).value,
                              'expected': sheet.cell(row=row, column=6).value,
                              'check': sheet.cell(row=row, column=7).value}
            # 将用例加入测试用例容器
            testcases.append(testcase)
        return testcases

    def get_title(self, sheet_name):
        sheet = self.workbook[sheet_name]
        max_row = sheet.max_row
        titles = []
        for row in range(2, max_row + 1):
            title = sheet.cell(row=row, column=2).value
            titles.append(title)
        return titles


if __name__ == '__main__':
    workbook = ReadExcel().get_testcase(sheetname='OederControl')
    print(workbook)
