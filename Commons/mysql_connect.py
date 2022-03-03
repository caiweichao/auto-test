# -*- coding: utf-8 -*-
# @Author  : caiweichao
# @explain : 建立数据库连接进行查询
import pymysql

from Commons.logs import Log
from Commons.read_ymal import ReadYaml


# 连接数据库建立游标，执行sql，关闭数据库
class Mysql_Util:

    def __init__(self, mysql_name=None):
        read_yaml = ReadYaml()
        host = read_yaml.get_every_config(key='global').upper()
        try:
            if host == 'PRO':
                mysql_config = read_yaml.get_mysql_config(mysql_name)
            else:
                mysql_config = read_yaml.get_mysql_config()
            self.db = pymysql.Connect(host=mysql_config.get('host'),
                                      user=mysql_config.get('user'),
                                      password=mysql_config.get('password'),
                                      database=None,
                                      port=int(mysql_config.get('port')))

        except TimeoutError as e:
            Log.error(f'数据库链接超时请检查：{e}')
            raise TimeoutError(f'数据库链接超时请检\n{e}')
        except IndentationError as e:
            Log.error('数据库链接用户名不存在请检查')
            raise IndentationError(f"数据库链接用户名不存在请检查\n{e}")
        except pymysql.err.OperationalError as e:
            Log.error(f'用户名或密码错误请检查\n{e}')
            raise pymysql.err.OperationalError('用户名或密码错误请检查')
        self.cursor = self.db.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.db.close()

    # 查询单条数据并且返回 可以通过sql查询指定的值 也可以通过索引去选择指定的值
    def fetch_one(self, sql, name=None):
        # 修改返回值为数组键值对
        # cursor=self.db.cursors.DictCursor()
        cursor = self.db.cursor()
        try:
            # 按照sql进行查询
            cursor.execute(sql)
            if name is None:
                # 返回一条数据 还有 all size（自己控制）
                sql_data = cursor.fetchone()
                return sql_data
            elif name is not None:
                sql_data = cursor.fetchone()
                return sql_data[name]
        except pymysql.err.ProgrammingError as e:
            Log.error("请检查sql是否正确 sql={}".format(sql))
            raise e

    def fetch_all(self, sql):  # 查询多条数据并且返回
        # 修改返回值为数组键值对 cursor=pymysql.cursors.DictCursor
        cursor = self.db.cursor()
        try:
            # 按照sql进行查询
            cursor.execute(sql)
            # 返回一条数据 还有 all size（自己控制）
            sql_data = cursor.fetchall()
        except pymysql.err.ProgrammingError as e:
            Log.error("请检查sql是否正确 sql={}".format(sql))
            raise e
        return sql_data

    def insert_data(self, sql):
        cursor = self.db.cursor()
        try:
            # 执行sql
            cursor.execute(sql)
            # 提交到数据库执行
            self.db.commit()
        except pymysql.err.ProgrammingError as e:
            Log.error("请检查sql是否正确 sql={}".format(sql))
            raise e

    def update_data(self, sql):
        cursor = self.db.cursor()
        try:
            # 执行sql
            cursor.execute(sql)
            # 提交到数据库执行
            self.db.commit()
        except pymysql.err.ProgrammingError as e:
            Log.error("请检查sql是否正确 sql={}".format(sql))
            raise e


if __name__ == '__main__':
    sql = "select ID from tem_platform_uat.ip_district where P_ID = 10801;"
    with Mysql_Util(mysql_name='Mysql_test') as db:
        value = db.fetch_all(sql)
    for x in value:
        print(x[0])
