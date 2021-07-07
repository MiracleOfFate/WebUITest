from basePage.base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By #筛选器

class SearchPage(BasePage):
    # 搜素框元素。定义一个id=kw的元素
    input_id=(By.ID,'kw')   # 元组数据类型
    # 百度一下按钮
    click_id=(By.ID,'su')

    # 对搜索框进行内容的输入
    def input_text(self,input_text):
        self.locator(*self.input_id).send_keys(input_text)

    # 点击查询按钮，实现本次搜索
    def click_element(self):
        self.locator(*self.click_id).click()

    # 执行业务的方法
    def check(self,url,input_text):
        self.visit(url)
        self.input_text(input_text)
        self.click_element()
        # self.quit_browser()


if __name__ =='__main__':
    url='http://www.baidu.com'
    driver=webdriver.Chrome()
    sp=SearchPage(driver)
    # 进行调试
    sp.check(url,'虚竹')
    # sp.visit(url)
    # sp.input_text('虚竹')
    # sp.click_element()