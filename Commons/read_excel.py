# -*- coding: utf-8 -*-
# @Author  : caiweichao
# @explain : 读取excel里的测试用例

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
    def get_testcase(self, sheetname: str) -> list:
        # 读取指定的sheet
        sheet = self.workbook[sheetname]
        # 获取对应sheet表单中全部的数据
        caseDatas = list(sheet.rows)
        # 获取第一行作为键
        caseTitle = [title.value for title in caseDatas[0]]
        testCases: list = []
        # 遍历第一行之外的全部数据
        for i in caseDatas[1:]:
            # 获取该行数据的值
            values = [v.value for v in i]
            # 用zip函数压缩后转换为字典
            testCase = dict(zip(caseTitle, values))
            testCases.append(testCase)
        return testCases

    @staticmethod
    def getCaseTitle(testCases: list):
        caseTitle: list = []
        for num in range(len(testCases)):
            caseTitle.append(testCases[num].get("case_title"))
        return caseTitle


if __name__ == '__main__':
    workbook = ReadExcel().get_testcase(sheetname='OederControl')
    print(type(workbook[0].get("data")))
