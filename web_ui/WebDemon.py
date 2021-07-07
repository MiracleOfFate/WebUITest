# coding:utf-8
from selenium import webdriver

# 通过浏览器驱动，调用chrome浏览器
driver=webdriver.Chrome()

# 访问指定的URL
driver.get("http://www.baidu.com")

# 定位输入框，输入“虚竹”
driver.find_element_by_id('kw').send_keys('虚竹')

# 定位‘百度一下’按钮，点击一次
driver.find_element_by_id('su').click()

driver.implicitly_wait(10)  # 隐式等待（这样才不会出错）

# 点击第一条链接
driver.find_element_by_xpath('//*[@id="1"]/h3/a').click()

# 点击第二条链接
# driver.find_element_by_xpath('//*[@id="2"]/h3/a').click()

# 切换标签页 handles
handles=driver.window_handles   # 数组类型
print(handles)
driver.close()
driver.switch_to.window(handles[1])

# 点击 影视形象链接
driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[1]/div[9]/div/div/ol/li[5]/span[2]/a').click()