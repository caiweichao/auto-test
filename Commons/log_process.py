# -*- coding: utf-8 -*-
# @Author  : caiweichao
# @explain : 日志文件管理类，创建日志文件夹和定期删除日志文件夹


import os
import shutil

from Commons.return_time import ReturnTime
from ConfigFile import contants_file
from ConfigFile import contants_test


class LogProcess:
    # 获取今天的日期
    today = ReturnTime.get_time()

    # 获取当天的日志存放目录，不存在则创建
    def get_log_dir(self):
        log_dir = str(os.path.join(contants_file.LOGS_DIR, self.today))
        img_dir = str(os.path.join(contants_file.IMG_DIR, self.today))
        try:
            if not os.path.isdir(log_dir):
                os.makedirs(log_dir)
                if not os.path.isdir(img_dir):
                    os.makedirs(img_dir)
            self.delect_dir()
        except FileExistsError:
            raise Exception("文件夹已经存在")
        finally:
            return log_dir, img_dir

    # 删除过于久远的日志文件夹
    def delect_dir(self):
        # 获取日志列表(图片和文件)
        floders_log = os.listdir(contants_file.LOGS_DIR)
        floders_img = os.listdir(contants_file.IMG_DIR)
        # 获取最大的日志存储时间
        max_time = int(self.today) - contants_test.LOG_TIME
        # 删除n天前的日志
        for floder in floders_log:
            if int(floder) < max_time:
                shutil.rmtree(os.path.join(contants_file.LOGS_DIR, floder))
        # 删除n天前的图片
        for floder in floders_img:
            if int(floder) < max_time:
                shutil.rmtree(os.path.join(contants_file.IMG_DIR, floder))


if __name__ == '__main__':
    # 测试代码
    x = LogProcess()
    x.get_log_dir()
