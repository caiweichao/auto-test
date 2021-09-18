# -*- coding: utf-8 -*-
# @Author  : caiweichao
# @explain : 账单列表用例合集
import allure
import pytest
from PageObject.Oper.Admin.es_admin_menu_page import EsAdminMenuPage
from PageObject.Oper.Admin.es_admin_company_bill_manage_page import CompanyBillManagePage


@allure.feature('账单列表用例合集')
@pytest.mark.usefixtures('case_basis_admin')
@pytest.mark.usefixtures('kill_driver')
@pytest.mark.usefixtures('case_teardown_admin')
@pytest.mark.run(order=4)
class TestCompanyBillManage:
    @allure.title("结算期间筛选")
    def test_select_settlemen_period(self,case_basis_admin):
        EsAdminMenuPage(case_basis_admin).get_CompanyBillManagePage()
        CompanyBillManagePage(case_basis_admin).select_settlemen_period()
        CompanyBillManagePage(case_basis_admin).select_TMC()



# 企业名称筛选（不选择tmc）
# 企业名称筛选
# 账户名称筛选
# 账单状态筛选
# 开票状态筛选
# 清账状态筛选
# 是否有调整项筛选
# 备注检查
# 进入账单详情（有权限）
# 进入账单详情（无权限）
