#@coding=utf-8
#@TIME:2023/5/24 11:10
#@author:SX
import requests,json
import re

#json提取法
# url='http://10.36.139.42:8999/stock/producttoken'
# res=requests.get(url=url)
# res=json.loads(res.text)
# print(res)
# print(res['msg'])

#正则表达式提取方法：
from common.MD5change import md5jm
from common.joindef import joinAAA

url='http://10.36.139.42:8999/stock/producttoken'
res=requests.get(url=url)
print(res.text)
r=re.findall('"msg": "(.*?)"',res.text)
print(r[0])

url1='http://10.36.139.42:8999/stock/asynRecharge'
data=  {
        "token":r[0],
        "orderId":"2017020100002104204264aa5f6",
        "productCode":"sp0001024",
        "count":2,
        "notifyUrl":"http://xx",
        "sign":"62d52860ce6105cea93"
  }
print('第一次的data:',data)
#拼接所有的数据英
BB=joinAAA(data)
print('拼接之后的内容：',BB)
#加密
sign=md5jm(BB)
print('加密后的sign:',sign)
#更 改字典data中sign的值
data['sign']=sign
print('data中sing修改后的值为:',data)
result=requests.post(url=url1,json=data)
print(result.text)