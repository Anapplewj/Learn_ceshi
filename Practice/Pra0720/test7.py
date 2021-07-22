# 文件的上传
from selenium import webdriver
import time
import os
driver=webdriver.Chrome()
file="file:///"+os.path.abspath("D:/biter/ceshi/selenium2html/upload.html")
driver.get(file)
driver.maximize_window()
time.sleep(3)
driver.find_element_by_tag_name("input").send_keys("D:/biter/ceshi/笔记/QQ登录.png")
time.sleep(6)
driver.quit()