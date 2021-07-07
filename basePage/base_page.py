
from selenium import webdriver
from time import sleep

# 定义页面的基础类，所有的页面都需要继承这个基础类
class BasePage(object):
    # 初始化基础类
    def __init__(self,driver):
        self.driver=driver

    # 元素定位
    def locator(self,*locator):
        return self.driver.find_element(*locator)   # *：元组

    # 关闭浏览器
    def quit_browser(self):
        sleep(2)
        self.driver.quit()

    # 访问URL
    def visit(self,url):
        self.driver.get(url)
        self.driver.maximize_window()

    def get_title(self):
        return self.driver.title