#@coding=utf-8
#@TIME:2023/5/25 14:13
#@author:SX
'''
1.引入requests2.准备数据3.发送请求4.获得响应5.断言
'''
import requests

url='http://testingedu.com.cn:8000/index.php/home/Uploadify/imageUp/savepath/head_pic/pictitle/banner/dir/images.html'
data={'id':'WU_FILE_0',
      'name':'身份证2.png',
      'type':"image/png"}
#files={'name':(上传的文件名,open('文件的路径','rb'),格式)}
files={'file':('身份证2.png',open(r"C:\Users\DELL\Desktop\宝藏\身份证1.png","rb"),'image/png')}

r=requests.post(url=url,data=data,files=files)
print(r.text)