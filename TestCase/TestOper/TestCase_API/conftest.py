# -*- coding: utf-8 -*-
# @Author  : caiweichao
# @explain : API测试夹具


import pytest

from Commons.json_util import JsonUtil
from Commons.read_ymal import ReadYaml
from Commons.request import Requset
from Commons.temp_data import BasicData


# 制造登录的cookie
@pytest.fixture(scope='session')
def get_cookies_es_H5():
    conf = ReadYaml().get_every_config("Api_test_data")
    _get_cookieurl = conf.get("_get_cookieurl")
    # 获取登录是需要的 ECkey
    get_EC = Requset(method='get', url=conf.get("_pass_port_es_Url"))
    client_key = JsonUtil.jsonToOneValue(get_EC.get_json(), "$.clientKey")
    setattr(BasicData, 'cookies_es',
            Requset('get', conf.get('_get_cookieurl') + f"KI4SO_CLIENT_EC={client_key}").get_cookies())


if __name__ == '__main__':
    pass
