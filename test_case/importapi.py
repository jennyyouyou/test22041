#@coding=utf-8
#@TIME:2023/5/25 15:48
#@author:SX
import requests
url='http://10.36.139.199:5674/zentao/testcase-import-15937-0.html'
files={'file':('templet.csv',open(r'D:\templet.csv','rb'),'text/csv')}
data={'encode':'utf-8'}
headers={"Host": "10.36.139.199:5674",
"Connection": "keep-alive",
"Content-Length": "1305",
"Cache-Control": "max-age=0",
"Upgrade-Insecure-Requests": "1",
"Origin": "http://10.36.139.199:5674",
"Content-Type": "multipart/form-data; boundary=----WebKitFormBoundaryFIxXLoKSc1OS3vBZ",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.50",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
"Referer": "http://10.36.139.199:5674/zentao/testcase-import-15937-0.html",
"Accept-Encoding": "gzip, deflate",
"Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
"Cookie": "lang=zh-cn; device=desktop; theme=default; preBranch=0; preProductID=15937; lastProduct=15937; ajax_lastNext=on; checkedItem=; downloading=1; downloading=null; windowWidth=800; windowHeight=171; zentaosid=ida84jt1pcv337b6gugin9c405",
 }
r=requests.post(url=url,files=files,data=data,headers=headers)
print(r.text)