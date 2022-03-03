# -*- coding: utf-8 -*-
# @Author  : caiweichao
# @explain : 通过jenkins发送allure测试报告
import jenkins

from Commons.res_dingding import DingRobot
from ConfigFile import contants_test


def send_report(name, job_name):
    # jenkins登录地址
    jenkins_url = "http://192.168.1.227:8080"
    # 实例化jenkins对象
    jenkins_server = jenkins.Jenkins(url=contants_test.JENKINS_URL,
                                     username=contants_test.J_USERNAME,
                                     password=contants_test.J_PWD)
    # 获取job最后一次的构建内容
    job_last_bulid = jenkins_server.get_info(job_name)["lastBuild"]["url"]
    # 测试报告地址
    report_url = job_last_bulid + "allure/"
    # 发送报告
    DingRobot(robot_name="oper_dingding_robot").res_allure_report(job_name=name, report_url=report_url)


if __name__ == '__main__':
    send_report(name='内部运营组', job_name='job/oper_test/', )
