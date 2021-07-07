from web_ui.test_key import TestKeys
from time import sleep

driver=TestKeys('chrome','http://www.baidu.com')

driver.input_text('id','kw','虚竹')
sleep(2)
driver.click_element('id','su')