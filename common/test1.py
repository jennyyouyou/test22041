#@coding=utf-8
#@TIME:2023/5/24 15:12
#@author:SX
from common.test import A
print(getattr(A(),'aa',300))
print(getattr(A(),"AA")())