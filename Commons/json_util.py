# -*- coding: utf-8 -*-
# @Author  : caiweichao
# @explain : json数据解析


import json

import jsonpath

from Commons.logs import Log


class JsonUtil:
    @staticmethod
    def load_json(data):
        return json.loads(data)

    @staticmethod
    def dumps_josn(data):
        return json.dumps(data)

    @staticmethod
    def jsonToOneValue(json: str, rule, mode=None):
        try:
            value = jsonpath.jsonpath(json, rule)
            if mode == "more":
                return value
            else:
                return value[0]
        except Exception as e:
            Log.error(f"无法正常获取json内容请检查解析表达式{rule}\n{e}")


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
