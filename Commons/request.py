# -*- coding: utf-8 -*-
# @Author  : caiweichao
# @explain : 封装http请求类


import allure
import requests

from Commons.logs import Log


class Requset:
    """
    请求的基础类
    :param method: 请求方式
    :param url: 请求的url
    :param data: 请求的参数
    :param cookies: 请求中带的cookie
    :param headers: 请求头
    """

    @allure.step("发起请求")
    def __init__(self, method: str, url: str, data=None, cookies=None, headers=None):
        try:
            Log.info(f'开始发起请求: 请求方式{method}， 请求url={url}，cookies{cookies}，请求头header={headers} ,\n请求参数={data}')
            if method.upper() == "GET":
                self._res = requests.get(url=url, params=data, headers=headers, cookies=cookies)
            elif method.upper() == "POST":
                self._res = requests.post(url=url, json=data, headers=headers, cookies=cookies)
            else:
                Log.error(f"请求类未添加对应请求方式{method}")
            with allure.step(f"响应结果{self._res.json()}"):
                pass
        except Exception:
            Log.error(Exception)
            raise Exception("请求错误请检查参数")

    # 获取请求的cookies
    def get_cookies(self):
        return self._res.cookies

    # 获取接口返回的json对象
    def get_json(self):
        return self._res.json()

    # 获取接口的返回的code
    def get_code(self):
        return self._res.status_code

    # 获取接口的全部响应时间
    def get_response_time(self):
        return self._res.elapsed.total_seconds()


if __name__ == '__main__':
    rest = Requset(method="post",
                   url="http://api.lemonban.com/futureloan/member/register",
                   data={"mobile_phone": 13248231300,
                         "pwd": 100000000},
                   headers={"Content-Type": "application/json",
                            "X-Lemonban-Media-Type": "lemonban.v1"})
    print(rest.get_json())
