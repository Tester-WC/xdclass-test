# -*- coding: utf-8 -*-
# @Time : 2021/3/5 13:51
# @Author : Mr.WANG
# @Version : 
# @Function :二次封装requests

import requests


class Request:

    def request(self, method, url, data, headers, paramtype='form'):
        """
        :param data: 请求参数
        :param method: 请求方法
        :param url: 请求地址
        :param paramtype: 参数类型
        :param headers: 请求头
        :return:
        """
        try:
            if method.lower() == 'get':
                if paramtype.lower() == 'form':
                    r = requests.get(url=url, headers=headers, params=data, verify=False)
                    return r.json()
                elif paramtype.lower() == 'json':
                    r = requests.get(url=url, headers=headers, data=data, verify=False)
                    return r.json()
            elif method.lower() == 'post':
                if paramtype.lower() == 'form':
                    r = requests.post(url=url, headers=headers, data=data, verify=False)
                    return r.json()
                elif paramtype.lower() == 'json':
                    r = requests.post(url=url, headers=headers, json=data, verify=False)
                    return r.json()
            else:
                return "请求方式请传GET或POST"
        except Exception as e:
            return "request报错：{0}".format(e)


R = Request()
