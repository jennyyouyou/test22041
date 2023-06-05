#@coding=utf-8
#@TIME:2023/5/23 16:12
#@author:SX
import requests,json
import unittest
from config.urladdress import url
from common.read_csv import Readcsv
from ddt import ddt ,data
data2=Readcsv().read_dict_csv('../test_data/tpshoplogin1.csv')
print(data2)

@ddt
class tpshop_login(unittest.TestCase):
    def setUp(self) -> None:
        self.url = url

    def tearDown(self) -> None:
        pass

    @data(*data2)
    def test_login_success_api(self,dic):
        print(dic)

        # data={'username':'13800138006',
        #       'password':'123456',
        #       'verify_code':1
        #       }

        res=requests.post(url=url,data=dic)
        result=json.loads(res.text)
        #断言
        print(result['msg'],dic['res'])
        self.assertEqual(dic['res'],result['msg'])

if __name__ == '__main__':
    unittest.main()