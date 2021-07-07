from selenium import webdriver

def open_browser(name,url):
    if name=='chrome':
        driver=webdriver.Chrome()
    if name=='firfox':
        driver=webdriver.Firefox()
    if name=='ie':
        driver=webdriver.Ie()
    driver.maximize_window()    # 窗口最大化
    driver.get(url)
    return driver

class TestKeys(object):
    def __init__(self,name,url):
        self.driver=open_browser(name,url)

    def input_text(self,locator_type,locator,text):
        if locator_type=='xpath':
            self.driver.find_element_by_xpath(locator).send_keys(text)
        if locator_type=='id':
            self.driver.find_element_by_id(locator).send_keys(text)
        if locator_type=='name':
            self.driver.find_element_by_name(locator).send_keys(text)

    def click_element(self,locator_type,locator):
        if locator_type=='xpath':
            self.driver.find_element_by_xpath(locator).click()
        if locator_type=='id':
            self.driver.find_element_by_id(locator).click()
        if locator_type=='name':
            self.driver.find_element_by_name(locator).click()