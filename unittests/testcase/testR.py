from unittests.pages.requestpage import R
from unittests.pages.logpage import Log
from unittests.pages.CSVpage import datapath, getdata, setdata
from unittests.pages.configpage import conf
import unittest
from urllib import parse
import random

method = 'post'
paramtype = 'json'
url = 'http://172.27.33.4:8001/api/his-platform-global-clinic/v1/globalRegistrationSystem/selectScheduleToCountMoney'
datas = {"cardNo": "0001021124", "deptId": "1304294392539828225", "fee": 20, "isEnjoyDiscountCard": 0,
         "payCardNo": "0001021124", "registrationDiscountId": "1306475869656584193",
         "scheduleDetailsId": "1369825281633370114", "shiftId": "1304657866247819265", "userId": "1304327351879782402",
         "visitLevelId": "1304628584192593921"}
headers = {'Authorization': 'Bearer586a4466-a425-41c3-bd71-be556b34386f'}
respone = R.request(method, url, datas, headers, paramtype)
print(respone)
# lst = respone['data']['list']
# for i in lst:
#     a = i['classesName'] + '（' + i['classesStartDate'] + '-' + i['classesEndDate'] + '）'
#     print(a)
