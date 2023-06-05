#@coding=utf-8
#@TIME:2023/5/26 10:14
#@author:SX
import pytest
def test_A():
    assert 1==1

def test_B():
    assert 1==1

def test_C():
    assert 1==2

if __name__ == '__main__':
    pytest.main(['-vs','test_pytestA.py', '--alluredir','../report/reportallure/'])