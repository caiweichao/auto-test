# -*- coding: utf-8 -*-
# @Author  : caiweichao
# @explain : 企业来款页面用例合集

import allure
import pytest
from pytest_assume.plugin import assume

from PageObject.Oper.Admin.es_admin_businessMoneyIn_page import BusinessMoneyInPage
from PageObject.Oper.Admin.es_admin_menu_page import EsAdminMenuPage


@allure.feature('企业来款页面用例合集')
@pytest.mark.usefixtures('case_basis_admin')
@pytest.mark.usefixtures('kill_driver')
@pytest.mark.usefixtures('case_teardown_admin')
@pytest.mark.run(order=1)
class TestBusinessMoneyIn:

    @allure.title('不填写收款账户直接保存')
    def test_not_input_record_incoming_payments(self, case_basis_admin):
        EsAdminMenuPage(case_basis_admin).get_BusinessMoneyInPage()
        BusinessMoneyInPage(case_basis_admin).click_record_incoming_payments()
        BusinessMoneyInPage(case_basis_admin).input_payment_title()
        BusinessMoneyInPage(case_basis_admin).input_incoming_amount(money=2000)
        BusinessMoneyInPage(case_basis_admin).input_summary_incoming_amount()
        BusinessMoneyInPage(case_basis_admin).input_payment_date()
        BusinessMoneyInPage(case_basis_admin).input_serial_number()
        BusinessMoneyInPage(case_basis_admin).input_remark()
        BusinessMoneyInPage(case_basis_admin).click_define_button()
        assert BusinessMoneyInPage(case_basis_admin).money_in_error_msg_check(error_msg='收款账户必填') is True

    @allure.title('不填写来款抬头直接保存')
    def test_not_input_payment_title(self, case_basis_admin):
        EsAdminMenuPage(case_basis_admin).get_BusinessMoneyInPage()
        BusinessMoneyInPage(case_basis_admin).click_record_incoming_payments()
        BusinessMoneyInPage(case_basis_admin).input_cash_accounts()
        BusinessMoneyInPage(case_basis_admin).input_incoming_amount(money=2000)
        BusinessMoneyInPage(case_basis_admin).input_summary_incoming_amount()
        BusinessMoneyInPage(case_basis_admin).input_payment_date()
        BusinessMoneyInPage(case_basis_admin).input_serial_number()
        BusinessMoneyInPage(case_basis_admin).input_remark()
        BusinessMoneyInPage(case_basis_admin).click_define_button()
        assert BusinessMoneyInPage(case_basis_admin).money_in_error_msg_check(error_msg='来款抬头必填') is True

    @allure.title('不填写金额直接保存')
    def test_not_input_incoming_amount(self, case_basis_admin):
        EsAdminMenuPage(case_basis_admin).get_BusinessMoneyInPage()
        BusinessMoneyInPage(case_basis_admin).click_record_incoming_payments()
        BusinessMoneyInPage(case_basis_admin).input_cash_accounts()
        BusinessMoneyInPage(case_basis_admin).input_payment_title()
        BusinessMoneyInPage(case_basis_admin).input_summary_incoming_amount()
        BusinessMoneyInPage(case_basis_admin).input_payment_date()
        BusinessMoneyInPage(case_basis_admin).input_serial_number()
        BusinessMoneyInPage(case_basis_admin).input_remark()
        BusinessMoneyInPage(case_basis_admin).click_define_button()
        assert BusinessMoneyInPage(case_basis_admin).money_in_error_msg_check(error_msg='金额必填') is True

    @allure.title('不填写日期直接保存')
    def test_not_input_payment_date(self, case_basis_admin):
        EsAdminMenuPage(case_basis_admin).get_BusinessMoneyInPage()
        BusinessMoneyInPage(case_basis_admin).click_record_incoming_payments()
        BusinessMoneyInPage(case_basis_admin).input_cash_accounts()
        BusinessMoneyInPage(case_basis_admin).input_payment_title()
        BusinessMoneyInPage(case_basis_admin).input_incoming_amount(money=2000)
        BusinessMoneyInPage(case_basis_admin).input_summary_incoming_amount()
        BusinessMoneyInPage(case_basis_admin).input_serial_number()
        BusinessMoneyInPage(case_basis_admin).input_remark()
        BusinessMoneyInPage(case_basis_admin).click_define_button()
        assert BusinessMoneyInPage(case_basis_admin).money_in_error_msg_check(error_msg='日期必填') is True

    @allure.title('不填写交易流水号直接保存')
    def test_not_input_serial_number(self, case_basis_admin):
        EsAdminMenuPage(case_basis_admin).get_BusinessMoneyInPage()
        BusinessMoneyInPage(case_basis_admin).click_record_incoming_payments()
        BusinessMoneyInPage(case_basis_admin).input_cash_accounts()
        BusinessMoneyInPage(case_basis_admin).input_payment_title()
        BusinessMoneyInPage(case_basis_admin).input_incoming_amount(money=2000)
        BusinessMoneyInPage(case_basis_admin).input_summary_incoming_amount()
        BusinessMoneyInPage(case_basis_admin).input_payment_date()
        BusinessMoneyInPage(case_basis_admin).input_remark()
        BusinessMoneyInPage(case_basis_admin).click_define_button()
        assert BusinessMoneyInPage(case_basis_admin).money_in_error_msg_check(error_msg='交易流水号必填') is True

    @allure.title('填写重复的交易流水号')
    def test_input_repeat_serial_number(self, case_basis_admin):
        EsAdminMenuPage(case_basis_admin).get_BusinessMoneyInPage()
        BusinessMoneyInPage(case_basis_admin).click_record_incoming_payments()
        BusinessMoneyInPage(case_basis_admin).input_cash_accounts()
        BusinessMoneyInPage(case_basis_admin).input_payment_title()
        BusinessMoneyInPage(case_basis_admin).input_incoming_amount(money=2000)
        BusinessMoneyInPage(case_basis_admin).input_summary_incoming_amount()
        BusinessMoneyInPage(case_basis_admin).input_payment_date()
        BusinessMoneyInPage(case_basis_admin).input_serial_number(content=111111)
        BusinessMoneyInPage(case_basis_admin).input_remark()
        BusinessMoneyInPage(case_basis_admin).click_define_button(more_click=True)
        assert BusinessMoneyInPage(case_basis_admin).money_in_error_msg_check(error_msg='111111') is True

    @allure.title('新增企业来款信息')
    def test_new_corporate_payment(self, case_basis_admin):
        EsAdminMenuPage(case_basis_admin).get_BusinessMoneyInPage()
        BusinessMoneyInPage(case_basis_admin).click_record_incoming_payments()
        BusinessMoneyInPage(case_basis_admin).input_cash_accounts()
        title = BusinessMoneyInPage(case_basis_admin).input_payment_title()
        BusinessMoneyInPage(case_basis_admin).input_incoming_amount(money=2000)
        BusinessMoneyInPage(case_basis_admin).input_summary_incoming_amount()
        BusinessMoneyInPage(case_basis_admin).input_payment_date()
        serial_number = BusinessMoneyInPage(case_basis_admin).input_serial_number()
        BusinessMoneyInPage(case_basis_admin).input_remark()
        BusinessMoneyInPage(case_basis_admin).click_define_button()
        BusinessMoneyInPage(case_basis_admin).list_page_input_payment_title(title=title)
        BusinessMoneyInPage(case_basis_admin).click_select_button()
        assert BusinessMoneyInPage(case_basis_admin).check_business_money_scuess() == serial_number

    @allure.title('企业来款查看详情')
    def test_corporate_payment_details(self, case_basis_admin):
        EsAdminMenuPage(case_basis_admin).get_BusinessMoneyInPage()
        payment_title = BusinessMoneyInPage(case_basis_admin).basic_step()
        BusinessMoneyInPage(case_basis_admin).list_page_input_payment_title(title=payment_title)
        BusinessMoneyInPage(case_basis_admin).click_select_button()
        BusinessMoneyInPage(case_basis_admin).click_check_button()
        assert BusinessMoneyInPage(case_basis_admin).check_text(value=payment_title) == payment_title

    @allure.title('企业来款查看详情点击返回')
    def test_corporate_payment_details_return(self, case_basis_admin):
        EsAdminMenuPage(case_basis_admin).get_BusinessMoneyInPage()
        payment_title = BusinessMoneyInPage(case_basis_admin).basic_step()
        BusinessMoneyInPage(case_basis_admin).list_page_input_payment_title(title=payment_title)
        BusinessMoneyInPage(case_basis_admin).click_select_button()
        BusinessMoneyInPage(case_basis_admin).click_check_button()
        BusinessMoneyInPage(case_basis_admin).click_return_button()
        assert BusinessMoneyInPage(case_basis_admin).check_search_result(parameter=payment_title) is True

    @allure.title('企业来款编辑-来款金额')
    def test_edit_payment_details_return(self, case_basis_admin):
        EsAdminMenuPage(case_basis_admin).get_BusinessMoneyInPage()
        payment_title = BusinessMoneyInPage(case_basis_admin).basic_step()
        BusinessMoneyInPage(case_basis_admin).list_page_input_payment_title(title=payment_title)
        BusinessMoneyInPage(case_basis_admin).click_select_button()
        BusinessMoneyInPage(case_basis_admin).click_edit_button()
        BusinessMoneyInPage(case_basis_admin).input_incoming_amount(money=3000)
        BusinessMoneyInPage(case_basis_admin).click_define_button()
        BusinessMoneyInPage(case_basis_admin).click_check_button()
        assert BusinessMoneyInPage(case_basis_admin).check_search_result(parameter='3,000.00') is True

    @allure.title('作废来款-作废')
    def test_invalid_payment(self, case_basis_admin):
        EsAdminMenuPage(case_basis_admin).get_BusinessMoneyInPage()
        payment_title = BusinessMoneyInPage(case_basis_admin).basic_step()
        BusinessMoneyInPage(case_basis_admin).list_page_input_payment_title(title=payment_title)
        BusinessMoneyInPage(case_basis_admin).click_select_button()
        BusinessMoneyInPage(case_basis_admin).click_invalid_payment_button(value=payment_title)
        BusinessMoneyInPage(case_basis_admin).click_invalid_payment_button_determine()
        assert BusinessMoneyInPage(case_basis_admin).check_search_result(parameter='已废弃') is True

    @allure.title('作废来款-取消作废')
    def test_invalid_payment_cancel(self, case_basis_admin):
        EsAdminMenuPage(case_basis_admin).get_BusinessMoneyInPage()
        payment_title = BusinessMoneyInPage(case_basis_admin).basic_step()
        BusinessMoneyInPage(case_basis_admin).list_page_input_payment_title(title=payment_title)
        BusinessMoneyInPage(case_basis_admin).click_select_button()
        BusinessMoneyInPage(case_basis_admin).click_invalid_payment_button(value=payment_title)
        BusinessMoneyInPage(case_basis_admin).click_invalid_payment_button_cancel()
        assert BusinessMoneyInPage(case_basis_admin).check_search_result(parameter='待认领') is True

    @allure.title('列表页收款账户筛选')
    def test_list_page_select_cash_accounts(self, case_basis_admin):
        EsAdminMenuPage(case_basis_admin).get_BusinessMoneyInPage()
        cash_accounts = BusinessMoneyInPage(case_basis_admin).input_cash_accounts(mode='list')
        BusinessMoneyInPage(case_basis_admin).click_select_button()
        assert BusinessMoneyInPage(case_basis_admin).check_search_result(parameter=cash_accounts) is True

    @allure.title('列表页来款抬头搜索')
    def test_list_page_select_payment_title(self, case_basis_admin):
        EsAdminMenuPage(case_basis_admin).get_BusinessMoneyInPage()
        payment_title = BusinessMoneyInPage(case_basis_admin).basic_step()
        BusinessMoneyInPage(case_basis_admin).list_page_input_payment_title(title=payment_title)
        BusinessMoneyInPage(case_basis_admin).click_select_button()
        assert BusinessMoneyInPage(case_basis_admin).check_search_result(parameter=payment_title,
                                                                         mode='len_check') is True

    @allure.title('列表页来款日期搜索')
    def test_list_page_select_payment_date(self, case_basis_admin):
        EsAdminMenuPage(case_basis_admin).get_BusinessMoneyInPage()
        payment_date = BusinessMoneyInPage(case_basis_admin).list_page_input_payment_date()
        BusinessMoneyInPage(case_basis_admin).click_select_button()
        assert BusinessMoneyInPage(case_basis_admin).check_search_result(parameter=payment_date) is True

    @allure.title('列表页认领状态筛选')
    def test_select_claim_status(self, case_basis_admin):
        EsAdminMenuPage(case_basis_admin).get_BusinessMoneyInPage()
        claim_status = BusinessMoneyInPage(case_basis_admin).select_claim_status()
        BusinessMoneyInPage(case_basis_admin).click_select_button()
        assert BusinessMoneyInPage(case_basis_admin).check_search_result(parameter=claim_status) is True

    @allure.title('列表页多条件查询账户日期')
    def test_list_page_complex_select(self, case_basis_admin):
        EsAdminMenuPage(case_basis_admin).get_BusinessMoneyInPage()
        cash_accounts = BusinessMoneyInPage(case_basis_admin).input_cash_accounts(mode='list')
        payment_date = BusinessMoneyInPage(case_basis_admin).list_page_input_payment_date()
        BusinessMoneyInPage(case_basis_admin).click_select_button()
        assume(BusinessMoneyInPage(case_basis_admin).check_search_result(parameter=payment_date) is True)
        assume(BusinessMoneyInPage(case_basis_admin).check_search_result(parameter=cash_accounts) is True)
