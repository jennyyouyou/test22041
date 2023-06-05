#@coding=utf-8
#@TIME:2023/5/24 15:51
#@author:SX
import hashlib
def md5jm(pw):
    #pw='1234561'
    p=hashlib.md5()
    p.update(pw.encode('utf-8'))
    mm=p.hexdigest()
    return(mm)
