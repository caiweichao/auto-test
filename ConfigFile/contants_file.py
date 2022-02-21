# -*- coding: utf-8 -*-
# @Author  : caiweichao
# @explain : 路径常量
import os

# 项目根目录
BASIC_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# logs目录
LOGS_DIR = os.path.join(BASIC_DIR, "Result/Logs")
# 配置文件路径
YAML_FILE = os.path.join(BASIC_DIR, "ConfigFile/config.yaml")
# 钉钉机器人配置文件路径
DING_CONFIG = os.path.join(BASIC_DIR, 'ConfigFile/dingding_config.yaml')
# 测试报告路径
REPORT_HTML_PATH = os.path.join(BASIC_DIR, "Result/Report/")
# 截图文件路径
IMG_DIR = os.path.join(BASIC_DIR, "Result/ScreenShot")
# 测试数据路径
TEST_DATA_PATH = os.path.join(BASIC_DIR, 'TestData/')
# 接口格式校验文件路径
SCHEMA_DATA_PAHT = os.path.join(BASIC_DIR, 'TestData/SchemaData')
