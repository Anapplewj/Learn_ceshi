from selenium import webdriver
# 使用键盘按键一定要导入的包
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome()
driver.get("http://127.0.0.1:8889/zentao/user-login-L3plbnRhby8=.html")
driver.maximize_window()

driver.find_element_by_id("account").send_keys("admin")
driver.find_element_by_id("account").send_keys(Keys.TAB)

password=driver.find_element_by_name("password")
password.send_keys("y=wangjia1234")
time.sleep(3)
password.send_keys(Keys.CONTROL,'a')
time.sleep(3)
password.send_keys(Keys.CONTROL,'x')
time.sleep(3)
password.send_keys("y=wangjia2222")
# driver.find_element_by_id("submit").click()
driver.find_element_by_name("password").send_keys(Keys.ENTER)
time.sleep(6)
driver.quit()
