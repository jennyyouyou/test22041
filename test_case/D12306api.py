#@coding=utf-8
#@TIME:2023/5/24 9:43
#@author:SX
import requests
#
# url='https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2023-05-24&leftTicketDTO.from_station=CSQ&leftTicketDTO.to_station=IOQ&purpose_codes=ADULT'
# headers={'Cookie': '_uab_collina=168050312340691856369303; JSESSIONID=B802CE021463A80B72EE325BD85E06FB; _jc_save_wfdc_flag=dc; toolbarStatus=open; RAIL_EXPIRATION=1682127497328; RAIL_DEVICEID=Ri5vYWH1NoGvMeTmVzGTALIqfnUfSsqHX3OXGAX7B_qoxTmuzYqwGZKBkO7hRTuTr3kXMkVlXhPQ0oHCDZSFcklQ7319DmwyS011EgEcVzNtn0EW5u0ksQiYfg3zhjtRrF1ApHjVgIzANHSKJh2HzXGj-jDd_TzL; _jc_save_fromStation=%u957F%u6C99%2CCSQ; _jc_save_toStation=%u6DF1%u5733%u5317%2CIOQ; BIGipServerotn=1440284938.64545.0000; BIGipServerpassport=904397066.50215.0000; guidesStatus=off; highContrastMode=defaltMode; cursorStatus=off; fo=undefined; route=6f50b51faa11b987e576cdb301e545c4; _jc_save_fromDate=2023-05-24; _jc_save_toDate=2023-05-24'}
#
# res=requests.get(url=url,headers=headers)
# print(res.content.decode('utf-8'))
#
# url1='https://www.ctrip.com/?sid=155952&allianceid=4897&ouid=index'
# res=requests.get(url=url1)
# print(res.text)

url='http://10.36.139.42:8887/'
res=requests.get(url=url,auth=('qianfeng','123456'))
print(res.text)
