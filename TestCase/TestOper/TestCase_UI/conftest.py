# -*- coding: utf-8 -*-
# @Author  : caiweichao
# @explain : 公共基础的conftest
import platform
import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager

from Commons.read_ymal import ReadYaml
from ConfigFile import contants_test

user = ReadYaml().get_every_config("Account")


# 代码提取
# def get_drvier(model=None):
def get_drvier(model="debug"):
    global driver
    # 判断系统是否是linux如果是就返回true
    ishandless = True if platform.system() == 'Linux' else False
    # 服务器使用或者远程调试
    if model == "debug" or ishandless:
        option = webdriver.ChromeOptions()
        option.add_argument('--headless')
        option.add_argument('--no-sandbox')
        option.add_argument('--disable-gpu')
        option.add_argument('--disable-dev-shm-usage')
        option.add_argument('--hide-scrollbars')
        option.add_argument('--window-size=1920,1080')
        option.add_experimental_option('useAutomationExtension', False)
        option.add_experimental_option('excludeSwitches', ['enable-automation'])
        driver = webdriver.Remote(command_executor='http://172.22.0.7:5555/wd/hub',
                                  desired_capabilities=DesiredCapabilities.CHROME, options=option)
        # driver.implicitly_wait(contants_test.ALL_TIMEOUT)
    # 本地调试使用
    else:
        path = ChromeDriverManager(cache_valid_range=7).install()
        driver = webdriver.Chrome(executable_path=path)
        driver.maximize_window()
    return driver


@pytest.fixture(scope='session')
def kill_driver():
    yield None
    driver.close()
    driver.quit()
    # os.system("ps aux | grep chromedriver | grep -v grep | awk '{print $2}' | xargs kill -9")


if __name__ == '__main__':
    pass
