from selenium import webdriver
from selenium.webdriver.common.action_chains import  ActionChains
import time

driver=webdriver.Chrome()
driver.get("https://www.baidu.com/")

driver.find_element_by_id("kw").send_keys("山河令")
# driver.find_element_by_id("su").submit()
# driver.find_element_by_id("su").click()
su=driver.find_element_by_id("su")
# 双击
# ActionChains(driver).double_click(su).perform()
# 右击
ActionChains(driver).context_click(su).perform()
time.sleep(6)
driver.quit()