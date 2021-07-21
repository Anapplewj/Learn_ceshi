# 测试五子棋的项目之点击匹配按钮
from selenium.webdriver.common.action_chains import  ActionChains

from selenium import webdriver
import time

driver1=webdriver.Chrome()

driver1.get("http://1.14.164.161:8080/MyChess/user1.html")
su=driver1.find_element_by_id("matchButton")
ActionChains(driver1).double_click(su).perform()
time.sleep(3)

driver2=webdriver.Chrome()
driver2.get("http://1.14.164.161:8080/MyChess/user2.html")
su=driver2.find_element_by_id("matchButton")
ActionChains(driver2).double_click(su).perform()
time.sleep(8)
time.sleep(8)

time.sleep(8)
driver1.quit()
driver2.quit()