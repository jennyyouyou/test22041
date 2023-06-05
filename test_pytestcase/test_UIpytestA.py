#@coding=utf-8
#@TIME:2023/5/26 14:36
#@author:SX
'''
  1.打开浏览器
   2.浏览器最大化
   3.打开https://www.baidu.com
   4.断言标题中包含“百度”

'''
from selenium import webdriver
import pytest

data=[['1001','https://www.baidu.com','百度'],
      ['1002','https://www.sina.com.cn/','新浪'],
      ['1003','https://www.sohu.com/','搜狐']]
@pytest.fixture(scope='function')
def ddriver():
    # 1.打开浏览器
    driver = webdriver.Chrome()
    # 2.浏览器最大化
    driver.maximize_window()
    return(driver)

@pytest.fixture(params=data)
def fix_data(request):
    return(request.param)

def test_baidu(ddriver,fix_data):
    print(fix_data)

    # 3.打开https: // www.baidu.com
    ddriver.get(fix_data[1])
    # 4.断言标题中包含“百度”
    assert fix_data[2] in ddriver.title

# def test_xinlang(ddriver):
#
#     # 3.打开https: // www.baidu.com
#     ddriver.get('https://www.sina.com.cn/')
#     # 4.断言标题中包含“百度”
#     assert '新浪' in ddriver.title
#
# def test_souhu(ddriver):
#
#     # 3.打开https: // www.baidu.com
#     ddriver.get('https://www.sohu.com/')
#
#     # 4.断言标题中包含“百度”
#     assert '搜狐'  in ddriver.title
if __name__ == '__main__':
    pytest.main(['-vs', '--alluredir','../report/reportallure/'])