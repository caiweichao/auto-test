# -*- coding: utf-8 -*-
# @Author  : caiweichao
# @explain : 来款认领页面用例合集
import time

import allure
import pytest
from pytest_assume.plugin import assume

from PageObject.Oper.Admin.es_admin_businessMoneyIn_claimList_page import MoneyInClaimListPage
from PageObject.Oper.Admin.es_admin_businessMoneyIn_page import BusinessMoneyInPage
from PageObject.Oper.Admin.es_admin_menu_page import EsAdminMenuPage


@allure.feature('来款认领页面用例合集')
@pytest.mark.usefixtures('case_basis_admin')
@pytest.mark.usefixtures('kill_driver')
@pytest.mark.usefixtures('case_teardown_admin')
@pytest.mark.run(order=2)
class TestBusinessMoneyInClaimList:

    @allure.title('列表页-收款账户筛选')
    def test_list_page_select_cash_accounts(self, case_basis_admin):
        EsAdminMenuPage(case_basis_admin).get_MoneyInClaimList()
        account = MoneyInClaimListPage(case_basis_admin).random_select_cash_accounts()
        MoneyInClaimListPage(case_basis_admin).click_select_button()
        assert MoneyInClaimListPage(case_basis_admin).check_search_result(parameter=account) is True

    @allure.title('列表页-来款抬头筛选')
    def test_list_page_select_payment_title(self, case_basis_admin):
        EsAdminMenuPage(case_basis_admin).get_BusinessMoneyInPage()
        payment_title = BusinessMoneyInPage(case_basis_admin).basic_step()
        # 确保数据创建成功后在跳转新页面
        time.sleep(2)
        EsAdminMenuPage(case_basis_admin).get_MoneyInClaimList()
        MoneyInClaimListPage(case_basis_admin).input_payment_title(paramter=payment_title)
        MoneyInClaimListPage(case_basis_admin).click_select_button()
        assert MoneyInClaimListPage(case_basis_admin).check_search_result(parameter=payment_title) is True

    @allure.title('列表页-来款日期筛选')
    def test_list_page_select_payment_date(self, case_basis_admin):
        EsAdminMenuPage(case_basis_admin).get_MoneyInClaimList()
        payment_date = MoneyInClaimListPage(case_basis_admin).input_payment_date()
        MoneyInClaimListPage(case_basis_admin).click_select_button()
        assert MoneyInClaimListPage(case_basis_admin).check_search_result(parameter=payment_date) is True

    @allure.title('列表页-认领状态筛选')
    def test_list_select_claim_status(self, case_basis_admin):
        EsAdminMenuPage(case_basis_admin).get_MoneyInClaimList()
        claim_status = MoneyInClaimListPage(case_basis_admin).random_select_claim_status()
        MoneyInClaimListPage(case_basis_admin).click_select_button()
        assert MoneyInClaimListPage(case_basis_admin).check_search_result(parameter=claim_status) is True

    @allure.title('列表页-来款业务筛选')
    def test_list_select_payment_business(self, case_basis_admin):
        EsAdminMenuPage(case_basis_admin).get_MoneyInClaimList()
        payment_business = MoneyInClaimListPage(case_basis_admin).random_select_payment_business()
        MoneyInClaimListPage(case_basis_admin).click_select_button()
        assert MoneyInClaimListPage(case_basis_admin).check_search_result(parameter=payment_business) is True

    @allure.title('列表页-指定企业筛选筛选')
    def test_list_select_partne(self, case_basis_admin):
        EsAdminMenuPage(case_basis_admin).get_MoneyInClaimList()
        partner_name = MoneyInClaimListPage(case_basis_admin).select_partner_name()
        MoneyInClaimListPage(case_basis_admin).clear_date()
        MoneyInClaimListPage(case_basis_admin).click_select_button()
        assert MoneyInClaimListPage(case_basis_admin).check_search_result(parameter=partner_name,
                                                                          partner_check=True) is True

    claim_case_data = [
        ['线上-全部认领清账后撤回', False, '01', "已认领"],
        ['线上-部分认领清账后撤回', True, '02', "部分认领"]
    ]

    @pytest.mark.parametrize("title,mode,times,check_data", claim_case_data)
    def test_clear_liquidation(self, case_basis_admin, title, mode, times, check_data):
        allure.title(test_title=title)
        payment_title = MoneyInClaimListPage(case_basis_admin).basis_step()
        MoneyInClaimListPage(case_basis_admin).click_details_button()
        MoneyInClaimListPage(case_basis_admin).click_claim_button()
        MoneyInClaimListPage(case_basis_admin).choose_company_claim_money()
        MoneyInClaimListPage(case_basis_admin).select_bill_date(paramter=times, part=mode, amount=1000)
        # 保证认领接口证正常请求
        time.sleep(0.5)
        assume(MoneyInClaimListPage(case_basis_admin).check_claim_status(payment_title, check_data) is True)
        assume(MoneyInClaimListPage(case_basis_admin).check_search_result(parameter="企业来款") is True)
        MoneyInClaimListPage(case_basis_admin).click_details_button()
        MoneyInClaimListPage(case_basis_admin).click_cancel_liquidation()
        MoneyInClaimListPage(case_basis_admin).click_cancel_claim()
        # 保证撤销正常请求
        time.sleep(0.5)
        assume(MoneyInClaimListPage(case_basis_admin).check_claim_status(payment_title, "待认领") is True)

    @allure.title("线上-认领金额大于来款金额(按照账单认领)")
    def test_claimed_amount_big_than_incoming_payment_amount_bill(self, case_basis_admin):
        MoneyInClaimListPage(case_basis_admin).basis_step()
        MoneyInClaimListPage(case_basis_admin).click_details_button()
        MoneyInClaimListPage(case_basis_admin).click_claim_button()
        MoneyInClaimListPage(case_basis_admin).choose_company_claim_money()
        text = MoneyInClaimListPage(case_basis_admin).select_bill_date(paramter='01', part=True, amount=9999)
        assert text == "认领金额需小于剩余未认领金额"

    @allure.title("线上-认领金额大于来款金额(按照账户认领)")
    def test_claimed_amount_big_than_incoming_payment_amount_acoount(self, case_basis_admin):
        MoneyInClaimListPage(case_basis_admin).basis_step()
        MoneyInClaimListPage(case_basis_admin).click_details_button()
        MoneyInClaimListPage(case_basis_admin).click_claim_button()
        MoneyInClaimListPage(case_basis_admin).choose_company_claim_money()
        text = MoneyInClaimListPage(case_basis_admin).click_custom_amount_claim(amount=9999)
        assert text == "认领金额需小于剩余未认领金额"

    @allure.title("线上-认领后金额后撤销认领")
    def test_revoke_after_claim(self, case_basis_admin):
        payment_title = MoneyInClaimListPage(case_basis_admin).basis_step()
        MoneyInClaimListPage(case_basis_admin).click_details_button()
        MoneyInClaimListPage(case_basis_admin).click_claim_button()
        MoneyInClaimListPage(case_basis_admin).choose_company_claim_money()
        MoneyInClaimListPage(case_basis_admin).click_custom_amount_claim(amount=1000)
        assume(MoneyInClaimListPage(case_basis_admin).check_claim_amount(already_amount="1,000.00",
                                                                         reamin_amount="1,000.00") is True)
        MoneyInClaimListPage(case_basis_admin).click_cancel_claim()
        # 保证撤销正常请求
        time.sleep(0.5)
        assume(MoneyInClaimListPage(case_basis_admin).check_claim_status(payment_title, "待认领") is True)

    @allure.title("线上-认领后修改认领金额")
    def test_update_after_claim(self, case_basis_admin):
        payment_title = MoneyInClaimListPage(case_basis_admin).basis_step()
        MoneyInClaimListPage(case_basis_admin).click_details_button()
        MoneyInClaimListPage(case_basis_admin).click_claim_button()
        MoneyInClaimListPage(case_basis_admin).choose_company_claim_money()
        MoneyInClaimListPage(case_basis_admin).click_custom_amount_claim(amount=1000)
        MoneyInClaimListPage(case_basis_admin).update_custom_amount_claim(update_amount=500)
        assume(MoneyInClaimListPage(case_basis_admin).check_claim_amount(already_amount="500.00",
                                                                         reamin_amount="1,500.00") is True)
        MoneyInClaimListPage(case_basis_admin).click_cancel_claim()
        # 保证撤销正常请求
        time.sleep(0.5)
        assume(MoneyInClaimListPage(case_basis_admin).check_claim_status(payment_title, "待认领") is True)

    @allure.title("线上-认领后再清账")
    def test_clear_account_after_claim(self, case_basis_admin):
        payment_title = MoneyInClaimListPage(case_basis_admin).basis_step()
        MoneyInClaimListPage(case_basis_admin).click_details_button()
        MoneyInClaimListPage(case_basis_admin).click_claim_button()
        MoneyInClaimListPage(case_basis_admin).choose_company_claim_money()
        MoneyInClaimListPage(case_basis_admin).click_custom_amount_claim(amount=2000)
        MoneyInClaimListPage(case_basis_admin).click_clear_account(paramter="03")
        # 保证认领接口证正常请求
        time.sleep(0.5)
        assume(MoneyInClaimListPage(case_basis_admin).check_claim_status(payment_title, "已认领") is True)
        assume(MoneyInClaimListPage(case_basis_admin).check_search_result(parameter="企业来款") is True)
        MoneyInClaimListPage(case_basis_admin).click_details_button()
        MoneyInClaimListPage(case_basis_admin).click_cancel_liquidation()
        MoneyInClaimListPage(case_basis_admin).click_cancel_claim()
        # 保证撤销正常请求
        time.sleep(0.5)
        assume(MoneyInClaimListPage(case_basis_admin).check_claim_status(payment_title, "待认领") is True)

    claer_case_data = [
        ["线下-认领后清账(全清)", "6", "2021/09/01 - 2021/09/01", "已认领"],
        ["线下-认领后清账(部分清账)", "100", "2021/09/02 - 2021/09/02", "部分认领"]
    ]

    @pytest.mark.parametrize("title,money,data_time,status", claer_case_data)
    def test_offline_clear_account_after_claim(self, case_basis_admin, title, money, data_time, status):
        allure.title(test_title=title)
        payment_title = MoneyInClaimListPage(case_basis_admin).basis_step(money=money)
        MoneyInClaimListPage(case_basis_admin).click_details_button()
        MoneyInClaimListPage(case_basis_admin).click_claim_button()
        MoneyInClaimListPage(case_basis_admin).select_offline_business(times=data_time)
        # 保证认领接口证正常请求
        time.sleep(0.5)
        assume(MoneyInClaimListPage(case_basis_admin).check_claim_status(payment_title, status) is True)
        assume(MoneyInClaimListPage(case_basis_admin).check_search_result(parameter="订单线下收款") is True)
        MoneyInClaimListPage(case_basis_admin).click_details_button()
        MoneyInClaimListPage(case_basis_admin).click_cancel_claim()
        # 保证撤销正常请求
        time.sleep(0.5)
        assume(MoneyInClaimListPage(case_basis_admin).check_claim_status(payment_title, "待认领") is True)
