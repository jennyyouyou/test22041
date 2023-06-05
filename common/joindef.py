#@coding=utf-8
#@TIME:2023/5/24 15:59
#@author:SX
'''MD5(token=value&orderId=value1&count=value2&productCode=value3&notifyUrl=value4&key=密钥)'''

def joinAAA(data):

    dd='token'+'='+data['token']+'&orderId'+'='+data['orderId']+\
           '&count'+'='+str(data['count'])+'&productCode'\
           +'='+data['productCode']+'&notifyUrl'+'='+data['notifyUrl']+\
        '&key=123456'
    return(dd)