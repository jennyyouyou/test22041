#@coding=utf-8
#@TIME:2023/5/26 16:57
#@author:SX
import requests
import pytest,json
data=[[100,'13800138006','123456','1','登陆成功'],
      [101,'','123456','1','请填写账号或密码1']]
@pytest.fixture(params=data)
def fix_data(request):
    return(request.param)

def test_login(fix_data):
    url='http://testingedu.com.cn:8000/index.php?m=Home&c=User&a=do_login&t=0.6818842354364223'

    data1={'username':'13800138006',
                  'password':'123456',
                  'verify_code':1
                  }
    data1['username']=fix_data[1]
    data1['password'] = fix_data[2]
    data1['verify_code'] = fix_data[3]
    res=requests.post(url=url,data=data1)
    res=json.loads(res.text)
    assert fix_data[4]==res['msg']

if __name__ == '__main__':
    pytest.main(['-vs','test_tpshoplogin.py','--alluredir','../report/reportallure/'])
