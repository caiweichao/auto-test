# -*- coding: utf-8 -*-
# @Author  : caiweichao
# @explain : 返回年月日的工具类，方便在自动化日期控件时的运用
import datetime
import time
from datetime import timedelta


class ReturnTime:
    @staticmethod
    def get_this_year() -> int:
        """
        :return: 返回今年的年份
        """
        return datetime.datetime.now().year

    @staticmethod
    def get_current_month() -> int:
        """
        :return: 返回当前的月份
        """
        return datetime.datetime.now().month

    @staticmethod
    def get_today() -> int:
        """
        :return: 返回当前日期
        """
        return datetime.datetime.now().day

    @staticmethod
    def get_time():
        """
        :return: 获取当前的的年月日
        """
        return time.strftime('%Y%m%d', time.localtime(time.time()))

    @staticmethod
    def get_Timestamp():
        """
        :return: 获取当前时间戳
        """
        return time.time()

    @staticmethod
    def get_now_time():
        """
        :return: 当前时间
        """
        now = time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time()))
        return now

    @staticmethod
    def time_cal(num, mode, time_delta=None):
        """
        :return: 返回当前时间 + n天
        "%Y-%m-%d %H:%M"
        """
        if time_delta is None:
            res = datetime.datetime.now() + timedelta(days=num)
            return res.strftime(mode)
        elif time_delta == 'hour':
            res = datetime.datetime.now() + timedelta(hours=num)
            return res.strftime(mode)
        elif time_delta == 'min':
            res = datetime.datetime.now() + timedelta(minutes=num)
            return res.strftime(mode)


if __name__ == '__main__':
    x = ReturnTime.get_Timestamp()
    print(str(x) + 'caiwei')
