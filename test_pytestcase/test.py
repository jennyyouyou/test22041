#@coding=utf-8
#@TIME:2023/5/26 14:44
#@author:SX
from time import sleep

from selenium import webdriver
driver = webdriver.Chrome()
# 2.浏览器最大化
driver.maximize_window()
# 3.打开https: // www.baidu.com
driver.get('https://www.baidu.com')
sleep(6)