from selenium import webdriver
import time


driver=webdriver.Chrome()
driver.get("https://www.baidu.com/")
# driver.find_element_by_id("kw").send_keys("白敬亭")
# driver.find_element_by_id("su").click()
# driver.find_element_by_id("wd").send_keys("白敬亭")
# driver.find_element_by_id("su").click()

# driver.find_element_by_link_text("新闻").click()

# driver.find_element_by_partial_link_text("hao").click()
driver.find_element_by_xpath("//*[@name='wd']").send_keys("100周年")
driver.find_element_by_xpath("//*[@id='su']").click()
time.sleep(8)
driver.quit()