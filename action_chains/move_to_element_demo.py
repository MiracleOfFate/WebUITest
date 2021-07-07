from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://www.taobao.com/")

# 鼠标移动到中国大陆元素上
element_china = driver.find_element_by_css_selector("div.site-nav-menu-hd>span.site-nav-region")
ActionChains(driver).move_to_element(element_china).perform()

# 定位到中国台湾选项
element_taiwan = driver.find_element_by_css_selector(
    "div.site-nav-menu-bd.site-nav-menu-list>#J_SiteNavRegionList>li:nth-child(4)")
element_taiwan.click()

sleep(3)
driver.quit()
