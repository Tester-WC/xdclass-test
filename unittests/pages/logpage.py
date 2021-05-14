# -*- coding: utf-8 -*-
# @Time : 2021/3/11 16:46
# @Author : Mr.WANG
# @Version : 
# @Function :封装日志类
import logging
import traceback
import os
import time
from unittests.pages.CSVpage import logpath

t = time.strftime('%Y-%m-%d', time.localtime())
loginfopath = os.path.join(logpath, '{0}_log.txt'.format(t))


class LogPrint:
    def __init__(self):
        """
        创建一个日志对象

        """
        self.looger = logging.getLogger(__name__)

        """
        给日志设置级别

        """
        self.looger.setLevel(level=logging.DEBUG)

        """
        创建一个日志格式对象

        """
        self.formater = logging.Formatter('Info:%(asctime)s - %(name)s - %(levelname)s - %(message)s', "%Y-%m-%d %H:%M:%S")

        """
        创建一个FileHandler的对象

        """
        console = logging.FileHandler(loginfopath)

        """
        给日志设置格式

        """

        console.setFormatter(self.formater)

        """
        logger日志对象加载FileHandler对象

        """
        self.looger.addHandler(console)

    def logsinfo(self, message):
        """
        日志输出

        """
        self.looger.debug(message)

    def logtraceback(self):
        """
        输出系统错误信息traceback到日志
        """
        self.logsinfo(traceback.format_exc())


Log = LogPrint()
