#@coding=utf-8
#@TIME:2023/5/25 11:21
#@author:SX
from test_case.F反射函数 import A
nn=getattr(A(),'name')
print(nn)
print(getattr(A(),'eat')())