#@coding=utf-8
#@TIME:2023/5/23 14:30
#@author:SX
'''
1.安装requests   --cmd   pip install requests
2.导入requests
3.准备数据
4.发送请求
5.获取结果，并解析结果
6.验证结果
'''
# 2.导入requests
import requests
# 3.准备数据
url='https://www.baidu.com'
# 4.发送请求
'''
requests.请求方式(url,data,params,cookis,headers)

请求方式：get,post,delete,....
url:接口地址（协议，服务器IP，端口，路径）
data,json:当你的请求方式为post时才用的，传送到接口的数据
params:当你的请求方式为get时才用的，传送到接口的数据
'''
res=requests.get(url=url)
print(res)
# 5.获取结果，并解析结果
res.encoding='gs2312'   #更改编码
print(res.encoding)   #检查网页的编码
print(res.text)   #响应结果的文本

# 6.验证结果