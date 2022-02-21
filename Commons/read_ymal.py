# -*- coding: utf-8 -*-
# @Author  : caiweichao
# @explain : 读取yaml文件

import yaml

from ConfigFile import contants_file


def check_yaml(func):
    def warpper(*args, **kwargs):
        try:
            res = func(*args, **kwargs)
            return res
        except KeyError:
            raise KeyError("未在配置找到对应的键")
        except Exception:
            raise Exception("读取配置文件发生未知异常")

    return warpper


class ReadYaml:
    # 方法初始化的时候读取yaml文件
    def __init__(self, file_url=None):
        try:
            if file_url is None:
                with open(file=contants_file.YAML_FILE, mode='r', encoding='UTF-8') as file:
                    self.__yaml_data = yaml.load(file.read(), Loader=yaml.FullLoader)
            else:
                with open(file=file_url, mode='r') as file:
                    self.__yaml_data = yaml.load(file.read(), Loader=yaml.FullLoader)
        except Exception:
            raise Exception("yaml文件读取异常")

    @check_yaml
    def get_mysql_config(self, mysql_name=None) -> dict:
        """
        获取数据库配置
        :return: 返回数据库配置字典
        """
        if self.__yaml_data['global'].upper() != 'PRO':
            return self.__yaml_data['Mysql_test']
        else:
            return self.__yaml_data['Mysql_PRO'].get(mysql_name)

    @check_yaml
    def get_every_config(self, key) -> dict:
        """
        获取任意的配置文件内容
        :param key: 配置文件的键
        :return: 返回对的值
        """
        return self.__yaml_data[key]


if __name__ == '__main__':
    user = ReadYaml().get_mysql_config(mysql_name='Mysql_oms')
    print(user)
