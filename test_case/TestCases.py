import unittest
from selenium import webdriver
from PageObject.search_page import SearchPage
from ddt import ddt, data, unpack
from time import sleep


@ddt  # "@"：装饰器。这里表示该类即将被调用ddt
class TestCases(unittest.TestCase):
    # class前置条件——对类有效，基于类的
    @classmethod  # 装饰器
    def setUpClass(cls) -> None:
        print('setUpClass')

    # class后置条件
    @classmethod
    def tearDownClass(cls) -> None:
        print('tearDownClass')

    # 前置条件——对测试用例有效，基于测试用例的
    def setUp(self):
        driver = webdriver.Chrome()
        self.sp = SearchPage(driver)

    # 后置条件
    def tearDown(self):  # None：无返回
        self.sp.quit_browser()

    # 测试用例1
    @data(['http://www.baidu.com', '光头强'], ['http://www.baidu.com', '阳光头强'])
    @unpack
    def test(self, url, input_text):
        self.sp.check(url, input_text)
        sleep(3)
        # self.assertEqual(self.sp.get_title(),'百度一下，你就知道',msg='对不起，你不知道') # 断言

    # 一般函数，用于让测试用例调用的函数，只有在调用时才会生效
    def plus(self):
        a = 1
        b = 2
        return a + b


if __name__ == '__main__':
    # 运行UnitTest测试用例
    unittest.main()
