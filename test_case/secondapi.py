#@coding=utf-8
#@TIME:2023/5/25 9:28
#@author:SX
import json

from common.MD5change import md5jm
from common.joindef import joinAAA
from config.urladdress import url2
from test_case.firstapi import First_apiA
import requests
import unittest
from ddt import ddt ,data
dataa=[[1001,'充值成功',First_apiA(),'1001','1001',1,'https://zzz','充值成功'],
       [1002,'token不正确的充值测试','token','1001','1001',1,'https://zzz','token is error!']
       ]

@ddt
class second_apiA(unittest.TestCase):
    def setUp(self) -> None:
        self.url1 = url2

    def tearDown(self) -> None:
        pass


    @data(*dataa)
    def test_jmcz_A(self,dataa1):

        #模块
         data1=  {
                "token":First_apiA(),
                "orderId":"2017020100002104204264aa5f6",
                "productCode":"sp0001024",
                "count":2,
                "notifyUrl":"http://xx",
                "sign":"62d52860ce6105cea93"
          }

         data1['token']=dataa1[2]
         data1['orderId']=dataa1[3]

         data1['productCode'] = dataa1[4]

         data1['count'] = dataa1[5]

         data1['notifyUrl'] = dataa1[6]



         #print('第一次的data:',data)
         #拼接所有的数据英
         BB=joinAAA(data1)
         # print('拼接之后的内容：',BB)
         #加密
         sign=md5jm(BB)
         #print('加密后的sign:',sign)
         #更 改字典data中sign的值
         data1['sign']=sign
         # print('data中sing修改后的值为:',data)
         result=requests.post(url=self.url1,json=data1)
         self.assertEqual(dataa1[-1],json.loads(result.text)['msg'])
         #self.assertEqual(1,1)

if __name__ == '__main__':
    unittest.main()