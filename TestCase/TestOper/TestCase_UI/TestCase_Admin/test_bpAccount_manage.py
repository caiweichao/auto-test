# -*- coding: utf-8 -*-
# @Author  : caiweichao
# @explain : 结算账户列表页的用例合集

import allure
import pytest
from pytest_assume.plugin import assume

from PageObject.Oper.Admin.es_admin_bpAccount_manage_page import BpAccountManagePage
from PageObject.Oper.Admin.es_admin_menu_page import EsAdminMenuPage


@pytest.mark.usefixtures("kill_driver")
@pytest.mark.usefixtures("case_teardown_admin")
@pytest.mark.usefixtures("case_basis_admin")
@allure.story("结算账户列表页的用例合集")
@pytest.mark.run(order=3)
class TestBpAccountManage:
    @allure.title("批量编辑结算账户时上传文件为空")
    def test_batch_edit_accoount_file_is_null(self, case_basis_admin):
        EsAdminMenuPage(case_basis_admin).get_BpAccountManagePage()
        BpAccountManagePage(case_basis_admin).click_batch_settings_button()
        BpAccountManagePage(case_basis_admin).click_start_import_button()
        assert BpAccountManagePage(case_basis_admin).check_error_msg() == "请选择导入文件"

    # @allure.title("创建结算账户")
    # def test_add_settlement_account(self, case_basis_admin):
    #     EsAdminMenuPage(case_basis_admin).get_BpAccountManagePage()
    #     BpAccountManagePage(case_basis_admin).click_add_account_button()
    #     BpAccountManagePage(case_basis_admin).add_account_select_partner()
    #     account_name = BpAccountManagePage(case_basis_admin).add_account_input_account_name()
    #     BpAccountManagePage(case_basis_admin).choice_corp()
    #     BpAccountManagePage(case_basis_admin).choice_partrne_corp()
    #     BpAccountManagePage(case_basis_admin).save_account()
    #     assert BpAccountManagePage(case_basis_admin).check_query_result(test_result=account_name) is True

    @allure.title("企业名称搜索")
    def test_partren_name_query(self, case_basis_admin):
        EsAdminMenuPage(case_basis_admin).get_BpAccountManagePage()
        partren_name = BpAccountManagePage(case_basis_admin).select_partren_name()
        BpAccountManagePage(case_basis_admin).click_query_button()
        assert BpAccountManagePage(case_basis_admin).check_query_result(test_result=partren_name) is True

    @allure.title("账户名称搜索")
    def test_account_name_query(self, case_basis_admin):
        EsAdminMenuPage(case_basis_admin).get_BpAccountManagePage()
        account_name = BpAccountManagePage(case_basis_admin).input_account_name(account_name="cwc基础查询账户")
        BpAccountManagePage(case_basis_admin).click_query_button()
        assert BpAccountManagePage(case_basis_admin).check_query_result(test_result=account_name) is True

    @allure.title("企业名称+账户名称组合搜索")
    def test_combination_search(self, case_basis_admin):
        EsAdminMenuPage(case_basis_admin).get_BpAccountManagePage()
        partren_name = BpAccountManagePage(case_basis_admin).select_partren_name()
        account_name = BpAccountManagePage(case_basis_admin).input_account_name(account_name="cwc组合查询账户")
        BpAccountManagePage(case_basis_admin).click_query_button()
        assume(BpAccountManagePage(case_basis_admin).check_query_result(test_result=partren_name))
        assume(BpAccountManagePage(case_basis_admin).check_query_result(test_result=account_name))

    @allure.title("账户状态改为禁止支付")
    def test_account_prohibits_payment_button(self, case_basis_admin):
        BpAccountManagePage(case_basis_admin).basic_step(account_name="禁付测试结算账户")
        BpAccountManagePage(case_basis_admin).click_prohibit_payment_button_for_account()
        assume(BpAccountManagePage(case_basis_admin).check_query_result(test_result="禁止支付") is True)
        BpAccountManagePage(case_basis_admin).click_enable_button_for_account()
        assume(BpAccountManagePage(case_basis_admin).check_query_result(test_result="可用") is True)

    @allure.title("账户状态改为停用")
    def test_account_deactivate_button(self, case_basis_admin):
        BpAccountManagePage(case_basis_admin).basic_step(account_name="停用测试结算账户")
        BpAccountManagePage(case_basis_admin).click_deactivate_button_for_account()
        assume(BpAccountManagePage(case_basis_admin).check_query_result(test_result="停用") is True)
        BpAccountManagePage(case_basis_admin).click_enable_button_for_account()
        assume(BpAccountManagePage(case_basis_admin).check_query_result(test_result="可用") is True)

    @allure.title("账户状态改为启用")
    def test_account_enable_button(self, case_basis_admin):
        BpAccountManagePage(case_basis_admin).basic_step(account_name="启用测试结算账户")
        BpAccountManagePage(case_basis_admin).click_enable_button_for_account()
        assume(BpAccountManagePage(case_basis_admin).check_query_result(test_result="可用") is True)
        BpAccountManagePage(case_basis_admin).click_deactivate_button_for_account()
        assume(BpAccountManagePage(case_basis_admin).check_query_result(test_result="停用") is True)

    @allure.title("创建结算账户时不选择法人")
    def test_add_settlement_account_not_choice_corp(self, case_basis_admin):
        EsAdminMenuPage(case_basis_admin).get_BpAccountManagePage()
        BpAccountManagePage(case_basis_admin).click_add_account_button()
        BpAccountManagePage(case_basis_admin).add_account_select_partner()
        BpAccountManagePage(case_basis_admin).add_account_input_account_name()
        assert BpAccountManagePage(case_basis_admin).save_account(error_case=True) == "请选择法人"

    @allure.title("创建结算账户时不选择企业")
    def test_add_settlement_account_not_choice_partner(self, case_basis_admin):
        EsAdminMenuPage(case_basis_admin).get_BpAccountManagePage()
        BpAccountManagePage(case_basis_admin).click_add_account_button()
        BpAccountManagePage(case_basis_admin).add_account_input_account_name()
        assert BpAccountManagePage(case_basis_admin).save_account(error_case=True) == "企业名称必填"

    @allure.title("创建结算账户时不填写账户名称")
    def test_add_settlement_account_not_choice_corp(self, case_basis_admin):
        EsAdminMenuPage(case_basis_admin).get_BpAccountManagePage()
        BpAccountManagePage(case_basis_admin).click_add_account_button()
        BpAccountManagePage(case_basis_admin).add_account_select_partner()
        assert BpAccountManagePage(case_basis_admin).save_account(error_case=True) == "账户名称必填"

    @allure.title("创建账户时直接编辑法人")
    def test_add_settlement_account_directly_edit_corp(self, case_basis_admin):
        EsAdminMenuPage(case_basis_admin).get_BpAccountManagePage()
        BpAccountManagePage(case_basis_admin).click_add_account_button()
        BpAccountManagePage(case_basis_admin).choice_corp()
        assert BpAccountManagePage(case_basis_admin).check_error_msg() == "请先选择企业！"

    @allure.title("修改结算账户名称")
    def test_edit_settlement_account_name(self, case_basis_admin):
        BpAccountManagePage(case_basis_admin).basic_step(account_name="编辑测试账户")
        BpAccountManagePage(case_basis_admin).click_edit_button_for_account()
        BpAccountManagePage(case_basis_admin).add_account_input_account_name(name="编辑测试账户")
        BpAccountManagePage(case_basis_admin).save_account()
        assert BpAccountManagePage(case_basis_admin).check_query_result(test_result="编辑测试账户") is True

    @allure.title("修改结算账户授信额度")
    def test_edit_settlement_account_credits_amount(self, case_basis_admin):
        BpAccountManagePage(case_basis_admin).basic_step(account_name="授信修改账户")
        BpAccountManagePage(case_basis_admin).click_edit_button_for_account()
        # 获取新的授信额度
        amount = BpAccountManagePage(case_basis_admin).edit_credit_amount()
        BpAccountManagePage(case_basis_admin).save_account()
        assert BpAccountManagePage(case_basis_admin).check_query_result(test_result=amount) is True

    @allure.title("修改结算账户的类型")
    def test_edit_account_type(self, case_basis_admin):
        BpAccountManagePage(case_basis_admin).basic_step(account_name="类型修改结算账户")
        BpAccountManagePage(case_basis_admin).click_edit_button_for_account()
        type_name = BpAccountManagePage(case_basis_admin).random_choice_account_type()
        BpAccountManagePage(case_basis_admin).save_account()
        assert BpAccountManagePage(case_basis_admin).check_query_result(test_result=type_name) is True

    @allure.title("可用金额小于警戒金额时账户颜色是否为红色")
    def test_account_whether_red(self, case_basis_admin):
        BpAccountManagePage(case_basis_admin).basic_step(account_name="红色状态测试账户")
        assert BpAccountManagePage(case_basis_admin).account_whether_red() is True

    @allure.title("可用金额小于警戒金额时账户颜色是否为白色")
    def test_account_whether_white(self, case_basis_admin):
        BpAccountManagePage(case_basis_admin).basic_step(account_name="白色状态测试账户")
        assert BpAccountManagePage(case_basis_admin).account_whether_red() is False

    @allure.title("结算模式为平台时结算账户是否无法编辑")
    def test_platform_model_can_not_edit(self, case_basis_admin):
        BpAccountManagePage(case_basis_admin).basic_step(account_name="平台结算测试账户")
        BpAccountManagePage(case_basis_admin).click_checkout_configuration_button_for_account()
        url = BpAccountManagePage(case_basis_admin).get_current_url_path()
        assert "readOnly=true" in url
