# -*- coding: utf-8 -*-
# @Author  : caiweichao
# @explain : 钉钉机器人通知

from Commons.read_ymal import ReadYaml
from Commons.request import Requset
from ConfigFile.contants_file import DING_CONFIG


class DingRobot:
    # 方法初始化的时候读取指定的机器人
    def __init__(self, robot_name):
        try:
            self.res_url = ReadYaml(file_url=DING_CONFIG).get_every_config(key=robot_name).get('url')
        except KeyError:
            raise KeyError(f'值{robot_name}错误请与配置文件核对')
        except Exception:
            raise Exception('未知异常请检查')

    # 对指定的机器人发起请求
    def res_dingding(self, error_msg=None, msg=None, is_at=None,is_scuess=False):

        # 构建请求数据
        header = {"Content-Type": "application/json", "Charset": "UTF-8"}
        if is_scuess:
            msg_ding = {"msgtype": "text",
                        "text": {"content": f'【线上监控】:{msg}'},
                        }
        else:
            if is_at is None:
                msg_ding = {"msgtype": "text",
                            "text": {"content": f'【线上报警】:\n{error_msg}\n{msg}'},
                            }
            else:
                msg_ding = {"msgtype": "text",
                            "text": {"content": f'【线上报警】:\n{error_msg}\n{msg}'},
                            "at": {
                                "atMobiles": [f"{is_at}"]
                            }
                            }
        Requset(method='post', url=self.res_url, data=msg_ding, headers=header)

    def res_allure_report(self, job_name, report_url,username="nbyy",pwd="ZTnbyy123456!"):
        header = {"Content-Type": "application/json", "Charset": "UTF-8"}
        msg_ding = {
            "msgtype": "link",
            "link": {
                "text": f"点击查看:\n  登录账号密码：{username}/{pwd}",
                "title": f"【{job_name}自动化日常巡检完成】",
                "picUrl": "",
                "messageUrl": report_url

            }
        }
        Requset(method='post', url=self.res_url, data=msg_ding, headers=header)


if __name__ == '__main__':
    pass
