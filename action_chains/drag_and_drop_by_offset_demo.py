from time import sleep

from selenium import webdriver

# 打开浏览器，并加载项目地址
driver = webdriver.Chrome()
driver.get("https://passport.ctrip.com/user/reg/home")
sleep(2)

# 点击同意并继续
element_agree = driver.find_element_by_css_selector("div.pop_footer>a.reg_btn.reg_agree")
element_agree.click()

sleep(3)   # important!!!

from selenium.webdriver.common.action_chains import ActionChains

# 定位滑块的位置
element_hk = driver.find_element_by_css_selector('div.cpt-drop-box>div.cpt-drop-btn')
# print(element_hk.size)    # {'height': 40, 'width': 40}
# print(element_hk.size['height'], element_hk.size['width'])

# 定义滑块条的位置
element_hkt = driver.find_element_by_css_selector('div.cpt-drop-box>div.cpt-bg-bar')
# print(element_hkt.size)  # {'height': 40, 'width': 268}
# print(element_hkt.size['height'], element_hkt.size['width'])

# 实现滑块操作
# ActionChains.drag_and_drop_by_offset(开始移动的元素——原始元素，鼠标对元素拖到另外一个元素的x坐标，鼠标对元素拖到另外一个元素的y坐标)
x_location = element_hk.size['width'] + element_hkt.size['width']
y_location = element_hkt.size['height']
# print(x_location, y_location) # 308 40
ActionChains(driver).drag_and_drop_by_offset(element_hk, x_location, y_location).perform()
sleep(2)
driver.quit()
