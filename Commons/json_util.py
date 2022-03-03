# -*- coding: utf-8 -*-
# @Author  : caiweichao
# @explain : json数据解析


import json

import allure
import jsonpath
import jsonschema

from Commons.logs import Log


class JsonUtil:
    @staticmethod
    def load_json(data):
        return json.loads(data)

    @staticmethod
    def dumps_josn(data):
        return json.dumps(data)

    @staticmethod
    def jsonToOneValue(json: str, rule: str, mode=None):
        try:
            value = jsonpath.jsonpath(json, rule)
            if mode == "more":
                return value
            else:
                return value[0]
        except Exception as e:
            Log.error(f"无法正常获取json内容请检查解析表达式{rule}\n{e}")

    @staticmethod
    def assert_jsonschema(response: dict, schema):
        """
        jsonschema与实际结果断言方法
        :param response: 实际响应结果
        :param schema: jsonschema
        :return:
        """
        try:
            Log.info("jsonschema校验开始")
            jsonschema.validate(instance=response, schema=schema, format_checker=jsonschema.draft7_format_checker)
            Log.info("jsonschema校验通过")
            allure.step(f"jsonschema校验通过")
        except jsonschema.exceptions.ValidationError or jsonschema.exceptions.SchemaError as e:
            Log.error(f"jsonschema校验失败，报错信息为： {e}")
            allure.step(f"jsonschema校验失败,报错信息为： {e}")
            raise e


if __name__ == '__main__':
    json1 = """{
    "invoiceItems":[
        {
            "insurance":"DING_E",
            "invoiceCorp":"1517:171",
            "serviceFee":"ZHI_ZHI_ZENG_PU",
            "flight":"ZHI_ZHI_ZENG_PU",
            "intlFlight":"ZHI_ZHI_ZENG_PU",
            "intlHotel":"ZHI_ZHI_ZENG_PU",
            "general":"ZHI_ZHI_ZENG_PU",
            "trainTicketService":"ZHI_ZHI_ZENG_PU",
            "car":"NON_INVOICE",
            "hotel":"ZHI_ZHI_ZENG_PU",
            "receiptCorps":"172,397,1619",
            "flightRefundFee":"DIAN_ZHI_ZENG_PU",
            "flightCheap":"ZHI_ZHI_ZENG_PU",
            "train":"NON_INVOICE"
        }
    ],
    "invoiceCategory":"SINGLE_CORP"
}"""
    print(JsonUtil.jsonToOneValue(JsonUtil.load_json(json1), rule='$.invoiceItems[0].receiptCorps'))
