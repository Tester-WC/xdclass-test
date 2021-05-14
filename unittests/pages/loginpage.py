# -*- coding: utf-8 -*-
# @Time : 2021/3/5 15:24
# @Author : Mr.WANG
# @Version :
# @Function :获取Authorization
from unittests.pages.requestpage import R
from unittests.pages.logpage import Log
from unittests.pages.CSVpage import datapath, getdata, setdata
from unittests.pages.configpage import conf


class Test_GetToken:

    def __init__(self, name, passwd, orgname, rolename):
        self.g = globals()
        self.Authorization = 'Basic d2ViQXBwOndlYkFwcA=='
        self.localhost = conf.getconf("main").url
        self.name = name
        self.passwd = passwd
        self.orgname = orgname
        self.rolename = rolename
        self.file = datapath + '/info.xls'

    def get_acctoken(self):
        """验证账号是否正确"""
        method = 'get'
        url = self.localhost + '/api/api-uaa/oauth/user/token'
        self.g['data'] = {'username': self.name, 'password': self.passwd,
                          'deviceId': '7B2E6955-D77A-40F7-A37B-4281E703B2A2'}
        headers = {'Authorization': self.Authorization}
        respone = R.request(method, url, self.g['data'], headers)
        if respone['msg'] == '':
            self.g['acctoken'] = respone['data']['token_type'] + respone['data']['access_token']
            Log.logsinfo('获取acctoken成功：{0}'.format(self.g['acctoken']))
        else:
            Log.logsinfo('error!接口返回错误:{0}'.format(respone))
            Log.logtraceback()

    def get_orgid(self):
        """如果账号正确，进行下一步，获取账号机构列表"""
        self.get_acctoken()
        method = 'get'
        url = self.localhost + '/api/his-user-center/staff_organization/getStaffOrganizationList'
        data = None
        headers = {'Authorization': self.g['acctoken']}
        respone = R.request(method, url, data, headers)
        if respone['msg'] == '':
            for i in respone['data']:  # 遍历此账户所有机构
                if i['orgName'] == self.orgname:
                    self.g['orgid'] = i['id']
                    '''保存orgid到文件便于引用'''
                    setdata(self.file, self.g['orgid'], 1, 1)
                    return self.g['orgid']
            Log.logsinfo('获取orgId成功：{0}'.format(self.g['orgid']))
        else:
            Log.logsinfo('error!接口返回错误:{0}'.format(respone))
            Log.logtraceback()

    def get_deptidANDroleid(self):
        """获取部门id和角色id"""
        self.get_orgid()
        method = 'get'
        url = self.localhost + '/api/his-user-center/staff_organization/getStaffDeptRoleList/{0}'.format(
            self.g['orgid'])
        data = None
        headers = {'Authorization': self.g['acctoken']}
        respone = R.request(method, url, data, headers)
        if respone['msg'] == '':
            for i in respone['data']:
                if i['roleName'] == self.rolename:
                    self.g['deptId'] = i['deptId']
                    self.g['roleId'] = i['roleId']
            Log.logsinfo('获取deptId成功：{0}'.format(self.g['deptId']))
            Log.logsinfo('获取roleId成功：{0}'.format(self.g['roleId']))
        else:
            Log.logsinfo('error!接口返回错误:{0}'.format(respone))
            Log.logtraceback()

    def gettoken(self):
        """登录账号角色"""
        self.get_deptidANDroleid()
        method = 'get'
        url = self.localhost + '/api/api-uaa/oauth/user/token'
        data1 = {'username': self.name, 'password': self.passwd,
                 'deviceId': '7B2E6955-D77A-40F7-A37B-4281E703B2A2', 'orgId': self.g['orgid'],
                 'deptId': self.g['deptId'], 'roleId': self.g['roleId']}
        headers = {'Authorization': self.Authorization}
        respone = R.request(method, url, data1, headers)
        if respone['msg'] == '':
            self.g['token'] = respone['data']['token_type'] + respone['data']['access_token']
            Log.logsinfo('获取token成功:{0}'.format(self.g['token']))
            '''保存token到文件'''
            setdata(self.file, self.g['token'],1,0)
            return self.g['token']
        else:
            Log.logsinfo('error!接口返回错误:{0}'.format(respone))
            Log.logtraceback()


if __name__ == '__main__':
    t = Test_GetToken('001722', '/7EQWL+pTZrC8v2JSXU9wA==', '成都安琪儿妇产医院（高攀院区）', '医院收银员')
    print(t.gettoken())
