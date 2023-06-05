#@coding=utf-8
#@TIME:2023/5/24 7:11
#@author:SX
import requests
import pytest,json
from config.urladdress import url
from common.read_csv import Readcsv
data4=Readcsv().read_list_csv('../test_data/tpshoplogin1.csv')

@pytest.fixture(params=data4)
def data_fix(request):
    return(request.param)


def test_request_login(data_fix):
    data5={'username':'13800138006',
           'password':'123456',
           'verify_code':1
        }
    data5['username']=data_fix[2]
    data5['password']=data_fix[3]
    print(type(data5))
    print(data_fix)
    res = requests.post(url=url, data=data5)
    result = json.loads(res.text)
    print('标记：',result)
    # # 断言
    #print(data_fix['exp'], result['msg'])
    assert(data_fix[5], result['msg'])
    #assert 1,1


if __name__ == '__main__':
    pytest.main(['-vs','test_11.py'])