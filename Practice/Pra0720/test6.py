from selenium.webdriver.common.action_chains import  ActionChains
import os
from selenium import webdriver
import time

driver=webdriver.Chrome()
# 打开本地的html文件
file1="file:///"+os.path.abspath("D:/biter/Web/LearnWeb-2-/MyChess2/src/main/webapp/user1.html")
driver.get(file1)
su=driver.find_element_by_id("matchButton")
ActionChains(driver).double_click(su).perform()
time.sleep(6)
driver.quit()