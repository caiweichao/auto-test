# -*- coding: utf-8 -*-
# @Author  : caiweichao
# @explain : 自动化测试用到的常量
# -----------日志常量管理-------------------
# 日志存储时间
LOG_TIME = 7
# 最低日志输出级别
LOG_LEVEL = "DEBUG"
# 日志输出格式
FORMATTER = '%(asctime)s-%(filename)s-%(levelname)s-%(message)s'

# driver路径
# DRIVER_PATH = os.path.join(RESOURCES_DIR, 'chromedriver')
# 元素等待超时时间
WAIT_ELEMENT = 15
# 页面轮询元素间隔
POLL_ELEMENT = 0.5
# 全局等待时间
ALL_TIMEOUT = 30
# web端url
PC_URL = "https://www.z-trip.cn"
# h5端url
H5_URL = "https://m.z-trip.cn"
# admin端url
ADMIN_URL = "https://admin.z-trip.cn"
# ADMIN_URL = "https://admin.z-trip.cn/login?_top_=1&gray_env_admin=1"
