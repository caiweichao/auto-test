# -*- coding: utf-8 -*-
# @Author  : caiweichao
# @explain : 优化后日志类
import logging

from Commons import log_process
from ConfigFile.contants_file import *
from ConfigFile.contants_test import *

# 日志收集器
logger = logging.getLogger("Log")
# 定义输出级别
logger.setLevel(LOG_LEVEL)


def set_handler(levels):
    if levels == 'error':  # 判断如果是error就添加error的handler
        logger.addHandler(Log.error_handle)
    else:  # 其他添加到infohandler
        logger.addHandler(Log.handler)
    logger.addHandler(Log.ch)  # 全部输出到console


def remove_handler(levels):
    if levels == 'error':
        logger.removeHandler(Log.error_handle)
    else:
        logger.removeHandler(Log.handler)
    logger.removeHandler(Log.ch)


class Log:
    __obj = None

    @staticmethod
    def __new__(cls, *args, **kwargs):
        if not cls.__obj:
            cls.__obj = super().__new__(cls)
            return cls.__obj
        else:
            return cls.__obj

    # 实例化文件管理类
    log_process = log_process.LogProcess()
    # 调用创建文件,传参确认文字日志
    log_dir = log_process.get_log_dir()
    # 指定输出文件
    log_file = os.path.join(log_dir[0], 'logs.log')
    # 设置日志输出格式
    formatter = logging.Formatter(fmt=FORMATTER)
    # 指定输出渠道
    # 控制台输出
    ch = logging.StreamHandler()
    ch.setLevel(LOG_LEVEL_CONSILE)
    ch.setFormatter(formatter)
    # INFO日志输出
    handler = logging.FileHandler(filename=log_file, encoding='utf-8')
    handler.setLevel('DEBUG')
    handler.setFormatter(formatter)
    # 错误日志输出
    error_handle = logging.FileHandler(filename=log_file, encoding='utf-8')
    error_handle.setLevel('ERROR')
    error_handle.setFormatter(formatter)

    @staticmethod
    def debug(msg):
        set_handler('debug')
        logger.debug(msg)
        remove_handler('debug')

    @staticmethod
    def info(msg):
        set_handler('info')
        logger.info(msg)
        remove_handler('info')

    @staticmethod
    def error(msg):
        set_handler('error')
        # 同时输出异常信息
        logger.error(msg, exc_info=True)
        remove_handler('error')
