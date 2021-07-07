import unittest
from time import sleep
from web_ui.test_keywords import TestKeyWords
from ddt import ddt, data, unpack, file_data  # 数据驱动


# 文件读取测试数据
def read_file():
    file = open('parameter.txt', 'r', encoding='utf-8')
    li = []
    for line in file.readlines():
        # print(line)
        li.append(line.strip('\n').split(','))  # 先通过strip去除指定的字符，然后通过split分割指定的位置
    file.close()
    # for l in li:
    #     print(l)
    return li


@ddt
class TestForKey(unittest.TestCase):
    # 前置条件
    def setUp(self):
        # print('setUp')
        self.tk = TestKeyWords('http://www.baidu.com', 'chrome')

    # 后置条件
    def tearDown(self):
        self.tk.quit_browser()
        # print('tearDown')

    # 测试用例1
    # *表示基于元组的形式进行处理，**表示字典，基于键值对的形式去获取
    @data(['id', '虚竹'], ['id', '思恋'])
    @unpack  # 解包，将list集合通过逗号解包
    def test1(self, locator, input_value):
        # tk = TestKeyWords('http://www.baidu.com', 'chrome')
        self.tk.input_text(locator, 'kw', input_value)
        self.tk.click_element('id', 'su')
        sleep(3)

    # 测试用例2
    # 无条件跳过本条用例的执行
    # @unittest.skip('因为我比较帅，所以不想执行')
    def test_2(self):
        # tk = TestKeyWords('http://www.baidu.com', 'chrome')
        self.tk.input_text('id', 'kw', '听虚竹的课')
        self.tk.click_element('id', 'su')
        sleep(3)
        text = self.tk.driver.find_element_by_link_text('虚竹').text
        self.assertEqual('虚竹', text, msg='失败')

    # 测试用例3
    @data(*read_file())  # 以元组形式进行解读
    @unpack  # 解包，将list集合通过逗号解包
    def test_3(self, locator, input_value):
        # tk = TestKeyWords('http://www.baidu.com', 'chrome')
        self.tk.input_text(locator, 'kw', input_value)
        self.tk.click_element('id', 'su')
        sleep(3)

    # 有条件跳过本条用例执行1 =false
    # @unittest.skipUnless(1 > 2, '这是unless的理由')
    def test(self):
        read_file()

    # 测试用例4
    # {
    #     locator:id
    #     input_value:虚竹
    # }
    # 有条件跳过本条用例执行2 = true
    @unittest.skipIf(1 < 2, '这是if的理由')
    @file_data('tests.yaml')  # 传入的参数是字典格式，不需要添加@unpack进行数据的解包
    def test_4(self, **locator):
        locator_new = locator.get('locator')
        input_value = locator.get('input_value')
        print('locator:', locator_new)
        print('input_value:' + input_value)
        # if input_value=='虚竹':
        #     print('successful')
        # else:
        #     print('failed')

        # self.assertEqual('虚竹',input_value,msg='我是msg！')
        # print('这是断言之后的打印内容！')

        self.assertAlmostEqual(9.023456789, 9.02345679, msg='这是一个大约值！')

    # 测试用例5
    @unittest.expectedFailure  # 不记录用例失败当中
    @file_data('tests.yaml')  # 传入的参数是字典格式
    def test_5(self, locator, input_value):
        # tk = TestKeyWords('http://www.baidu.com', 'chrome')
        self.tk.input_text(locator, 'kw', input_value)
        self.tk.click_element('id', 'su')
        sleep(3)

        self.assertEqual('虚竹', input_value, msg='我是msg！')

    # 普通函数（不以test开始的）
    # def pulse(self):
    #     print('plus')


if __name__ == '__main__':
    unittest.main()
