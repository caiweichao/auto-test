# -*- coding: utf-8 -*-
# @Author  : caiweichao
# @explain : admin 测试夹具

import pytest

from Commons.read_ymal import ReadYaml
from ConfigFile import contants_test
from PageObject.Oper.Admin.es_admin_index_page import EsAdminIndexPage
from TestCase.TestOper.TestCase_UI import conftest


# admin的登录
@pytest.fixture(scope='session')
def case_basis_admin():
    user = ReadYaml().get_every_config("Account")
    global _driver
    # 绕过验证码需要使用定期更新
    cookies = {'name': 'LC__ADA9E98C91287BB035AB0763F55984EC', 'value': 'AC20B1FF3B97F56372E378A08E218ED3'}
    _driver = conftest.get_drvier()
    _driver.get(contants_test.ADMIN_URL)
    _driver.add_cookie(cookie_dict=cookies)
    # 添加cookies 必须要重新访问一次保证cookie正确添加
    _driver.get(contants_test.ADMIN_URL)
    _driver.find_element_by_id('input-username').send_keys(user.get('username'))
    _driver.find_element_by_xpath('//input[@type="password"]').send_keys(user.get('password'))
    _driver.find_element_by_xpath('//button[@class="btn btn-info login-btn"]').click()
    if EsAdminIndexPage(_driver).check_login() is True:
        yield _driver


# 用例执行完毕截图 后台的所有都不需要回首页不测试链接跳转功能
@pytest.fixture()
def case_teardown_admin():
    yield None
    EsAdminIndexPage(_driver).set_img_case()


if __name__ == '__main__':
    pass
