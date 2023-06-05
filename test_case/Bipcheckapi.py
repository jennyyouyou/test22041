#@coding=utf-8
#@TIME:2023/5/23 15:18
#@author:SX
import requests,json

#第一种表示方式
'''
url='https://qifu-api.baidubce.com/ip/geo/v1/district?ip=12.12.12.12'
res=requests.get(url=url)
res1=res.text
res1=json.loads(res1)
assert(res1['data']['continent'],'北美洲')
'''
#第二种表示方式
url2='https://qifu-api.baidubce.com/ip/geo/v1/district'
params={'ip':'12.12.12.12'}

r=requests.get(url=url2,params=params)
print(r.text)