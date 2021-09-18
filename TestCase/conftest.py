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


@pytest.fixture(scope='class')
def connect_oms():
    account = ReadYaml().get_mysql_config(mysql_name="Mysql_oms")
    db = pymysql.Connect(host=account.get('host'),
                         user=account.get('user'),
                         password=account.get('password'),
                         database=None,
                         port=int(account.get('port')))
    cursor = db.cursor()
    yield cursor
    cursor.close()
    db.close()


@pytest.fixture(scope='class')
def connect_ota():
    account = ReadYaml().get_mysql_config(mysql_name="Mysql_ota")
    db = pymysql.Connect(host=account.get('host'),
                         user=account.get('user'),
                         password=account.get('password'),
                         database=None,
                         port=int(account.get('port')))
    cursor = db.cursor()
    yield cursor
    cursor.close()
    db.close()


if __name__ == '__main__':
    sql = "select sum(BP_PAY_AMOUNT) from tem_oms.ota_order_traveller where ORDER_ID = 116743856484608"
    DB = connect_oms()
    DB.execute(sql)
    print(DB.fetc())
