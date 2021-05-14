# -*- coding: utf-8 -*-
# @Time : 2021/3/12 10:24
# @Author : Mr.WANG
# @Version : 
# @Function :获取接口地址信息
# coding:utf-8
import os
import configparser


class Dictionary(dict):
    """
    把config.ini中的参数添加值dict
    """

    def __getattr__(self, keyname):
        # 如果key值不存在则返回默认值"not find config keyname"
        return self.get(keyname, "config.ini中没有找到对应的keyname")


class Config(object):
    """
    ConfigParser二次封装，在字典中获取value
    """

    def __init__(self):
        # 设置conf.ini路径
        current_dir = os.path.dirname(__file__)
        top_one_dir = os.path.dirname(current_dir)
        file_name = top_one_dir + "\\data\\config.ini"
        # 实例化ConfigParser对象
        self.config = configparser.ConfigParser()
        self.config.read(file_name, encoding='utf-8')
        # 根据section把key、value写入字典
        for section in self.config.sections():
            setattr(self, section, Dictionary())
            for keyname, value in self.config.items(section):
                setattr(getattr(self, section), keyname, value)

    def getconf(self, section):
        """
        用法：
        conf = Config()
        info = conf.getconf("main").url
        """
        if section in self.config.sections():
            pass
        else:
            print("config.ini 找不到该 section")
        return getattr(self, section)


conf = Config()

if __name__ == "__main__":
    conf = Config()
    info = conf.getconf("main").url
    print(info)
