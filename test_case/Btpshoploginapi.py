#@coding=utf-8
#@TIME:2023/5/23 16:05
#@author:SX
''''''
'''
POST http://testingedu.com.cn:8000/index.php?m=Home&c=User&a=do_login&t=0.6818842354364223 HTTP/1.1
Host: testingedu.com.cn:8000
Connection: keep-alive
Content-Length: 50
Accept: application/json, text/javascript, */*; q=0.01
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.50
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Origin: http://testingedu.com.cn:8000
Referer: http://testingedu.com.cn:8000/Home/user/login.html
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
Cookie: province_id=1; city_id=2; district_id=3; is_mobile=0; PHPSESSID=c325c0bf99d9be0596e01d0c6663cdb1

username=13800138006&password=123456&verify_code=1
'''
import requests,json
url='http://testingedu.com.cn:8000/index.php?m=Home&c=User&a=do_login&t=0.6818842354364223'
data={'username':'13800138006',
      'password':'123456',
      'verify_code':1
      }

# res=requests.post(url=url,data=data)
# print(json.loads(res.text))
result=requests.post(url=url,json=data)
print(json.loads(result.text))

