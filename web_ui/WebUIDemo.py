# 调用安装好的selenium模块
from selenium import webdriver
from time import sleep

# 去掉黄条
option=webdriver.ChromeOptions()
option.add_argument('disable-infobars')
# 无头模式（即不会出现页面，但还是会执行测试）
# option.add_argument('headless')

# 通过浏览器驱动，调用chrome浏览器
driver = webdriver.Chrome(chrome_options=option) # 会打开/启动chrome浏览器

driver.implicitly_wait(10)  # 隐式等待

# 访问指定的URL
driver.get('http://www.baidu.com')# http一定记得加
print(driver.title) # 页面标题——eg.百度一下，你就知道

# 定位输入框，输入“测码学院腾讯课堂”
driver.find_element('id','kw').send_keys('测码学院腾讯课堂')
# driver.find_element_by_id('kw').send_keys('测码学院腾讯课堂')

# 定位‘百度一下’按钮，点击一次
driver.find_element_by_id('su').click()

# 等待，有时间让其缓冲得到完整信息。sleep可以作为增加自动化测试稳定性的手段
# sleep(2)

# 点击第一条链接
driver.find_element_by_xpath('//*[@id="1"]/h3/a').click()