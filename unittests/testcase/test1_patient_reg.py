# -*- coding: utf-8 -*-
# @Time : 2021/3/10 15:53
# @Author : Mr.WANG
# @Version : 
# @Function :病人注册及收费
from unittests.pages.requestpage import R
from unittests.pages.logpage import Log
from unittests.pages.CSVpage import datapath, getdata
from unittests.pages.person_info import persominfo
from unittests.pages.configpage import conf
from unittests.pages.loginpage import Test_GetToken
import unittest
import random
import time


class Test_patient_mz(unittest.TestCase):
    # def setUp(self):
    #     file = datapath + '/logindata.xls'
    #     data = getdata(file)
    #     self.Authorization = Test_GetToken(data[0][0], data[0][1], data[0][2], data[0][3]).gettoken()
    #     self.g = globals()
    #     self.localhost = conf.getconf("main").url

    @classmethod
    def setUpClass(cls):
        file1 = datapath + '/logindata.xls'
        data1 = getdata(file1)
        cls.Authorization = Test_GetToken(data1[0][0], data1[0][1], data1[0][2], data1[0][3]).gettoken()
        cls.orgid = Test_GetToken(data1[0][0], data1[0][1], data1[0][2], data1[0][3]).get_orgid()
        cls.g = globals()
        cls.localhost = conf.getconf("main").url

    @classmethod
    def tearDownClass(cls):
        pass

    # def tearDown(self):
    #     pass

    def testcase_001_getdictionary(self):
        """获取病人注册相关各种字典id"""
        try:
            method = 'get'
            url = self.localhost + '/api/his-platform-global-config/v1/dictionary/page'
            datas = {'pageNo': 1,
                     'pageSize': 10000}
            headers = {'Authorization': self.Authorization}
            respone = R.request(method, url, datas, headers)
            self.assertEqual(respone['msg'], '处理成功', msg=respone)
            lst = respone['data']['list']
            self.g['nation'] = lst[0]['id']
            self.g['sex'] = lst[1]['id']
            self.g['marry'] = lst[2]['id']
            self.g['profession'] = lst[3]['id']
            self.g['family'] = lst[4]['id']
            self.g['country'] = lst[5]['id']
            self.g['education'] = lst[6]['id']
            Log.logsinfo('病人注册相关字典id:{0}'.format(lst))
        except Exception as e:
            Log.logsinfo(self._testMethodName + '\n' + str(e))
            raise

    def testcase_002_getsexid(self):
        """获取性别id"""
        try:
            method = 'get'
            url = self.localhost + '/api/his-platform-global-config/v1/dictionary-item/page'
            datas = {'pageNo': 1,
                     'pageSize': 10000,
                     'dictId': self.g['sex']}
            headers = {'Authorization': self.Authorization}
            respone = R.request(method, url, datas, headers)
            self.assertEqual(respone['msg'], '处理成功', msg=respone)
            lst = respone['data']['list']
            if persominfo['sex'] == '男':
                self.g['sexid'] = lst[1]['id']
            elif persominfo['sex'] == '女':
                self.g['sexid'] = lst[3]['id']
            Log.logsinfo('病人性别:{0}，性别id：{1}'.format(persominfo['sex'], self.g['sexid']))
        except Exception as e:
            Log.logsinfo(self._testMethodName + '\n' + str(e))
            raise

    def testcase_003_getcertificateTypeid(self):
        """获取证件类型id"""
        try:
            method = 'get'
            url = self.localhost + '/api/his-platform-global-common/common-dictionary/org/list'
            datas = {'dictTypeId': 1205314304593182722}
            headers = {'Authorization': self.Authorization}
            respone = R.request(method, url, datas, headers)
            self.assertEqual(respone['msg'], '', msg=respone)
            lst = respone['data']
            for i in lst:
                if i['dictValue'] == '居民户口本':
                    self.g['certificateTypeid'] = i['id']
                    Log.logsinfo('证据类型:居民户口本，证件id：{0}'.format(self.g['certificateTypeid']))
        except Exception as e:
            Log.logsinfo(self._testMethodName + '\n' + str(e))
            raise

    def testcase_004_getcountryid(self):
        """获取国家id"""
        try:
            method = 'get'
            url = self.localhost + '/api/his-platform-global-config/v1/dictionary-item/page'
            datas = {'pageNo': 1,
                     'pageSize': 10000,
                     'dictId': self.g['country']}
            headers = {'Authorization': self.Authorization}
            respone = R.request(method, url, datas, headers)
            self.assertEqual(respone['msg'], '处理成功', msg=respone)
            lst = respone['data']['list']
            self.g['countyrid'] = lst[1]['id']
            Log.logsinfo('国籍:中国，国籍id：{0}'.format(self.g['countyrid']))
        except Exception as e:
            Log.logsinfo(self._testMethodName + '\n' + str(e))
            raise

    def testcase_005_getnationid(self):
        """获取民族id"""
        try:
            method = 'get'
            url = self.localhost + '/api/his-platform-global-config/v1/dictionary-item/page'
            datas = {'pageNo': 1,
                     'pageSize': 10000,
                     'dictId': self.g['nation']}
            headers = {'Authorization': self.Authorization}
            respone = R.request(method, url, datas, headers)
            self.assertEqual(respone['msg'], '处理成功', msg=respone)
            lst = respone['data']['list']
            self.g['nationid'] = lst[0]['id']
            Log.logsinfo('民族id：{0}'.format(self.g['nationid']))
        except Exception as e:
            Log.logsinfo(self._testMethodName + '\n' + str(e))
            raise

    def testcase_006_getmaritalStatusid(self):
        """获取婚姻状况id"""
        try:
            method = 'get'
            url = self.localhost + '/api/his-platform-global-config/v1/dictionary-item/page'
            datas = {'pageNo': 1,
                     'pageSize': 10000,
                     'dictId': self.g['marry']}
            headers = {'Authorization': self.Authorization}
            respone = R.request(method, url, datas, headers)
            self.assertEqual(respone['msg'], '处理成功', msg=respone)
            lst = respone['data']['list']
            self.g['maritalStatusid'] = lst[0]['id']
            Log.logsinfo('婚姻状况未婚id：{0}'.format(self.g['maritalStatusid']))
        except Exception as e:
            Log.logsinfo(self._testMethodName + '\n' + str(e))
            raise

    def testcase_007_getcardTypeId(self):
        """获取金卡id"""
        try:
            method = 'get'
            url = self.localhost + '/api/his-platform-global-common/v1/organization-card-type/valid-list'
            datas = {'orgId': self.orgid}
            headers = {'Authorization': self.Authorization}
            respone = R.request(method, url, datas, headers)
            self.assertEqual(respone['msg'], '', msg=respone)
            lst = respone['data']
            for i in lst:
                if i['cardType'] == '金卡':
                    self.g['cardTypeid'] = i['id']
            Log.logsinfo('金卡id：{0}'.format(self.g['cardTypeid']))
        except Exception as e:
            Log.logsinfo(self._testMethodName + '\n' + str(e))
            raise

    def testcase_008_getcardno(self):
        """获取金卡卡号"""
        try:
            method = 'get'
            url = self.localhost + '/api/his-platform-global-clinic/v1/patient-card/generateCardNumberByCardType/{0}'.format(
                self.g['cardTypeid'])
            datas = None
            headers = {'Authorization': self.Authorization}
            respone = R.request(method, url, datas, headers)
            self.assertEqual(respone['msg'], '', msg=respone)
            self.g['card_no'] = respone['data']
            Log.logsinfo('会员卡卡号：{0}'.format(self.g['card_no']))
        except Exception as e:
            Log.logsinfo(self._testMethodName + '\n' + str(e))
            raise

    def testcase_009_patient_reg(self):
        """病人注册"""
        try:
            method = 'post'
            url = self.localhost + '/api/his-platform-global-clinic/v1/patient-card'
            data = {'threeNoPerson': False,
                    'crmId': '',
                    'id': '',
                    'groupPatientId': '',
                    'name': persominfo['name'],
                    'sex': self.g['sexid'],
                    'birthday': persominfo['birthday_stamp'],
                    'certificateType': self.g['certificateTypeid'],
                    'certificateNo': persominfo['idnum'],
                    'country': self.g['countyrid'],
                    'nation': self.g['nationid'],
                    'maritalStatus': self.g['maritalStatusid'],
                    'profession': '',
                    'educationLevel': '',
                    'phoneNo': persominfo['phone'],
                    'medicalInsuranceType': '',
                    'email': '',
                    'generalRegionProvince': '',
                    'generalRegionCity': '',
                    'generalRegionArea': '',
                    'domicileRegionProvince': '',
                    'domicileRegionCity': '',
                    'domicileRegionArea': '',
                    'mensesTime': '',
                    'remark': '',
                    'generalRegionDetail': '',
                    'domicileRegionDetail': '',
                    'contactName': '',
                    'contactRelationId': '',
                    'contactPhoneNo': '',
                    'orgPatientId': '',
                    'cardId': '',
                    'cardTypeId': self.g['cardTypeid'],
                    'cardNo': self.g['card_no'],
                    'cardPwd': 111111,
                    'invoiceType': '',
                    'lastMenstrualPeriod': '',
                    'billNo': '',
                    'paymentWayId': '',
                    'billTypeId': '',
                    'needCardNumberRule': '',
                    'cardStatus': 1,
                    'stamp': 2}
            headers = {'Authorization': self.Authorization}
            respone = R.request(method, url, data, headers)
            self.assertEqual(respone['code'], 200, msg=respone)
            self.g['groupPatientId'] = respone['data']['groupPatientId']
            self.g['orgPatientId'] = respone['data']['orgPatientId']
            Log.logsinfo('病人注册接口返回信息:{0}'.format(respone['data']))
            Log.logsinfo('病人身份信息：{0}'.format(persominfo))

        except Exception as e:
            Log.logsinfo(self._testMethodName + '\n' + str(e))
            Log.logsinfo('病人身份信息：{0}'.format(persominfo))
            raise

    def testcase_010_regdiscounts(self):
        """获取挂号优惠信息"""
        try:
            method = 'get'
            url = self.localhost + '/api/his-platform-config-center/v1/registration-discount/page-list'
            datas = None
            headers = {'Authorization': self.Authorization}
            respone = R.request(method, url, datas, headers)
            self.assertEqual(respone['msg'], '处理成功', msg=respone)
            self.g['discount'] = random.choice(respone['data'])
            Log.logsinfo('挂号优惠信息：{0}'.format(self.g['discount']['registrationDiscountName']))
        except Exception as e:
            Log.logsinfo(self._testMethodName + '\n' + str(e))
            raise

    def testcase_011_schedule_info(self):
        """获取医生排班信息"""
        try:
            t = time.strftime('%Y-%m-%d', time.localtime())
            method = 'post'
            paramtype = 'json'
            url = self.localhost + '/api/his-platform-global-clinic/v1/scheduling-setting/scheduleDoctorInfoPageForRegistration'
            datas = {"pageNo": 1, "pageSize": 20, "deptId": "", "orgId": self.orgid,
                     "scheduleDate": t, "scheduleDetailsId": "", "shiftId": [], "userId": []}
            headers = {'Authorization': self.Authorization}
            respone = R.request(method, url, datas, headers, paramtype)
            self.assertEqual(respone['msg'], '处理成功', msg=respone)
            lst = respone['data']['list']
            for i in lst:
                if i['theSourceNumber'] == '0':
                    lst.remove(i)
            self.g['scheduleinfo'] = random.choice(lst)
            Log.logsinfo(
                '挂号医生信息:{0}，挂号科室信息:{1}'.format(self.g['scheduleinfo']['userName'], self.g['scheduleinfo']['deptName']))
        except Exception as e:
            Log.logsinfo(self._testMethodName + '\n' + str(e))
            raise

    def testcase_012_getclassinfo(self):
        """获取班次时间段信息"""
        try:
            method = 'get'
            url = self.localhost + '/api/his-platform-config-center/outCallClassesConfigController/page-list'
            datas = {'keyWord': '', 'pageNo': 1, 'pageSize': 1000}
            headers = {'Authorization': self.Authorization}
            respone = R.request(method, url, datas, headers)
            self.assertEqual(respone['msg'], '处理成功', msg=respone)
            lst = respone['data']['list']
            for i in lst:
                if i['id'] == self.g['scheduleinfo']['shiftId']:
                    self.g['visitShiftName'] = i['classesName'] + '（' + i['classesStartDate'] + '-' + i[
                        'classesEndDate'] + '）'

        except Exception as e:
            Log.logsinfo(self._testMethodName + '\n' + str(e))
            raise

    def testcase_013_getBillTypeId(self):
        """获取纸质发票id"""
        try:
            method = 'get'
            url = self.localhost + '/api/his-platform-global-common/charge-business/getBillTypeIdByBusinessCode'
            datas = {'businessCode': 'registration'}
            headers = {'Authorization': self.Authorization}
            respone = R.request(method, url, datas, headers)
            self.assertEqual(respone['msg'], '', msg=respone)
            self.g['BillTypeId'] = respone['data']

        except Exception as e:
            Log.logsinfo(self._testMethodName + '\n' + str(e))
            raise

    def testcase_014_getBillNo(self):
        """获取纸质发票流水号"""
        try:
            method = 'get'
            url = self.localhost + '/api/global-bill/v1/bill/use/getBillNowNo'
            datas = {'billTypeId': self.g['BillTypeId']}
            headers = {'Authorization': self.Authorization}
            respone = R.request(method, url, datas, headers)
            self.assertEqual(respone['msg'], '', msg=respone)
            self.g['billno'] = respone['data']['nowNum']

        except Exception as e:
            Log.logsinfo(self._testMethodName + '\n' + str(e))
            raise

    def testcase_015_PayMoneyInfo(self):
        """获取挂号实际支付信息"""
        try:
            method = 'post'
            paramtype = 'json'
            url = self.localhost + '/api/his-platform-global-clinic/v1/globalRegistrationSystem/selectScheduleToCountMoney'
            datas = {"cardNo": self.g['card_no'], "deptId": self.g['scheduleinfo']['deptId'],
                     "fee": self.g['scheduleinfo']['fee'], "isEnjoyDiscountCard": 0,
                     "payCardNo": self.g['card_no'], "registrationDiscountId": self.g['discount']['id'],
                     "scheduleDetailsId": self.g['scheduleinfo']['scheduleDetailsId'],
                     "shiftId": self.g['scheduleinfo']['shiftId'],
                     "userId": self.g['scheduleinfo']['userId'], "visitLevelId": self.g['scheduleinfo']['visitLevelId']}
            headers = {'Authorization': self.Authorization}
            respone = R.request(method, url, datas, headers, paramtype)
            self.assertEqual(respone['msg'], '', msg=respone)
            self.g['PayInfo'] = respone['data']
        except Exception as e:
            Log.logsinfo(self._testMethodName + '\n' + str(e))
            raise

    def testcase_016_getTreatmentTypeId(self):
        """获取治疗类型id"""
        try:
            method = 'get'
            url = self.localhost + '/api/his-platform-config-center/v1/treatment/type/list'
            datas = {'orgId': self.orgid}
            headers = {'Authorization': self.Authorization}
            respone = R.request(method, url, datas, headers)
            self.assertEqual(respone['msg'], '', msg=respone)
            lst = respone['data']
            for i in lst:
                if i['name'] == '门诊':
                    self.g['TreatmenTypeId'] = i['id']
                    self.g['TreatmenTypeName'] = i['name']

        except Exception as e:
            Log.logsinfo(self._testMethodName + '\n' + str(e))
            raise

    def testcase_017_getPayWayTypeId(self):
        """获取支付方式id"""
        try:
            method = 'get'
            url = self.localhost + '/api/his-platform-global-common/charge-business/list'
            datas = {'businessCode': 'registration',
                     'cardNo': self.g['card_no']}
            headers = {'Authorization': self.Authorization}
            respone = R.request(method, url, datas, headers)
            self.assertEqual(respone['msg'], '', msg=respone)
            lst = respone['data']
            for i in lst:
                if i['businessDesc'] == '挂号':
                    PayWayList = i['payWayList']
            for j in PayWayList:
                for key, value in j.items():
                    if value == '现金':
                        self.g['PayWayTypeId'] = key

        except Exception as e:
            Log.logsinfo(self._testMethodName + '\n' + str(e))
            raise

    def testcase_018_registration(self):
        """挂号"""
        try:
            method = 'post'
            paramtype = 'json'
            url = self.localhost + '/api/his-platform-global-clinic/v1/globalRegistrationSystem/registrationRecord'
            datas = {"orgId": self.orgid, "groupId": None, "groupPatientId": self.g['groupPatientId'],
                     "orgPatientId": self.g['orgPatientId'], "cardTypeId": self.g['cardTypeid'], "cardTypeName": "金卡",
                     "cardStatus": "1", "patientName": persominfo['name'], "birthDate": persominfo['birthday_stamp'],
                     "phoneNo": persominfo['phone'], "sex": self.g['sexid'], "age": persominfo['age'],
                     "cardBalance": None, "balanceAmount": None, "cardDiscount": None,
                     "insideDiscount": None, "extWhetherDiscount": None, "vipCard": None, "allowCharge": None,
                     "payCardNo": self.g['card_no'], "cardNo": self.g['card_no'], "other": None, "registrationType": 1,
                     "discountMoneyOfRegistration": self.g['PayInfo']['discountMoneyOfRegistration'],
                     "discountMonetOfmemberCard": self.g['PayInfo']['discountMonetOfmemberCard'],
                     "isEnjoyDiscountCard": self.g['PayInfo']['isEnjoyDiscountCard'],
                     "invoiceNo": self.g['billno'], "payMoney": self.g['PayInfo']['payMoney'],
                     "registrationDiscountId": self.g['discount']['id'],
                     "invoiceType": 2,
                     "treatmentTypeName": self.g['TreatmenTypeName'], "treatmentTypeId": self.g['TreatmenTypeId'],
                     "billTypeId": self.g['BillTypeId'],
                     "classesName": None, "deptId": self.g['scheduleinfo']['deptId'],
                     "deptName": self.g['scheduleinfo']['deptName'], "fee": self.g['scheduleinfo']['fee'],
                     "scheduleDetailsId": self.g['scheduleinfo']['scheduleDetailsId'],
                     "shiftId": self.g['scheduleinfo']['shiftId'],
                     "userId": self.g['scheduleinfo']['userId'],
                     "userName": self.g['scheduleinfo']['userName'],
                     "visitLevelId": self.g['scheduleinfo']['visitLevelId'],
                     "visitLevelName": self.g['scheduleinfo']['visitLevelName'],
                     "visitShiftName": self.g['visitShiftName'],
                     "visitTimeDate": self.g['scheduleinfo']['scheduleDate'],
                     "sourceNumberType": self.g['scheduleinfo']['sourceNumberWay'],
                     "categoryDTOForMtList": self.g['PayInfo']['categoryDTOForMtList'],
                     "feeDetailForPackageDTOS": self.g['PayInfo']['feeDetailForPackageDTOS'],
                     "discountMembercardId": self.g['card_no'], "payCardId": self.g['PayInfo']['payCardId'],
                     "isPrintInvoice": True,
                     "tradeRecordPaymentTypeRequests": [
                         {"paymentType": self.g['PayWayTypeId'], "paymentTypeName": "现金",
                          "payAmount": self.g['PayInfo']['payMoney'],
                          "payType": 1}],
                     "gender": self.g['sexid'], "remark": ""}
            headers = {'Authorization': self.Authorization}
            respone = R.request(method, url, datas, headers, paramtype)
            self.assertEqual(respone['msg'], '挂号成功！', msg=respone)
            registrationID = respone['data']['id']
            Log.logsinfo('挂号记录ID：{0}'.format(registrationID))
        except Exception as e:
            Log.logsinfo(self._testMethodName + '\n' + str(e))
            raise


if __name__ == '__main__':
    unittest.main()
