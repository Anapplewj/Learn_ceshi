from selenium import webdriver
import unittest
import time
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException

class Baidu1(unittest.TestCase):
    # 初始化
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.url="https://www.baidu.com/"
        self.driver.maximize_window()
    # UI功能测试之后的清理工作
    def tearDown(self):
        self.driver.quit()
    def test_hao(self):
        driver=self.driver
        driver.get(self.url)
        time.sleep(3)
        driver.find_element_by_link_text("hao123").click()
        time.sleep(6)
    def test_baidusearch(self):
        driver=self.driver
        driver.get(self.url)
        time.sleep(3)
        driver.find_element_by_id("kw").send_keys("海贼王")
        driver.find_element_by_id("su").click()
        time.sleep(3)

    if __name__=='__main__':
        unittest.main(verbosity=1)