# -*- coding: utf-8 -*-
# @Author  : caiweichao
# @explain : 测试夹具

import pymysql
import pytest

from Commons.read_ymal import ReadYaml


def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的item的name和nodeid的中文显示在控制台上
    :return:
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")

