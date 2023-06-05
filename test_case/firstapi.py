#@coding=utf-8
#@TIME:2023/5/25 9:25
#@author:SX
import requests,re

from config.urladdress import url1


def First_apiA():
    url=url1
    res=requests.get(url=url)
    print(res.text)
    r=re.findall('"msg": "(.*?)"',res.text)
    return(r[0])