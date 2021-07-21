from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get("https://www.baidu.com/")
urll=driver.current_url
print(urll)
driver.find_element_by_id("kw").send_keys("海贼王")
driver.find_element_by_id("su").submit()
# 固定等待,必须等待10s
# time.sleep(10)
# 智能等待,需要加载的元素加载出来了,就立即停止等待,超过10s报异常
# driver.implicitly_wait(10)
# driver.find_element_by_link_text("海贼王-高清视频在线观看").click()
# 浏览器最大化
driver.maximize_window()
time.sleep(6)
# 拖动滚动条到最底端
js1="var q=document.documentElement.scrollTop=10000"
driver.execute_script(js1)
time.sleep(3)
# 拖动滚动条到最顶端
js2="var q=document.documentElement.scrollTop=0"
driver.execute_script(js2)
# 设置浏览器的宽和高
# driver.set_window_size(400,1000)
# time.sleep(6)
# 后退
# driver.back()
# time.sleep(6)
# 前进
# driver.forward()
urll=driver.current_url
print(urll)
title=driver.title
print(title)
time.sleep(6)
driver.quit()