import unittest, os
from unit_demo.test_for_key import *
from HTMLTestRunner import HTMLTestRunner

# 创建测试套件
suite = unittest.TestSuite()

# 添加测试用例    第一种方法  ——根据添加的顺序执行测试用例
# suite.addTest(TestForKey('test'))
# # suite.addTest(TestForKey('test_3'))
# suite.addTest(TestForKey('test_2'))

# 添加测试用例    第二种方法
cases = [TestForKey('test'), TestForKey('test_2')]
# suite.addTests(cases)

# 添加测试用例    第三种方法   ——根据指定的路径下所有与指定的文件名相符合的文件全部都添加进来
# test_dir = './'  # 定义一个路径（这里为当前目录下——unit_demo）
# discover = unittest.defaultTestLoader.discover(start_dir=test_dir, pattern='test_for*.py')

# 添加测试用例    第四种方法   ——根据指定的测试用例类的所有测试用例全部都添加进来
# suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestForKey))

# 添加测试用例    第五种方法   ——根据指定的 文件名.测试用例类 的所有测试用例全部都添加进来
# suite.addTests(unittest.TestLoader().loadTestsFromName('test_for_key.TestForKey'))

# 基于Runner来运行测试套件
# runner = unittest.TextTestRunner()
# # runner.run(discover)
# runner.run(suite)


# 集成测试报告
report_name = '测试报告名称'
report_title = '测试报告标题'
report_desc = '测试报告描述'

report_path = './report/'  # 测试报告保存路径
# ./report/report.html  保存的测试报告的路径
report_file = report_path + 'report.html'  # 测试报告文件保存

# 判断文件夹是否存在
if not os.path.exists(report_path):  # 如果路径不存在
    os.mkdir(report_path)  # 创建文件夹
else:
    pass

# HTMLTestRunner的使用
with open(report_file, 'wb') as report:
    suite.addTests(cases)
    runner = HTMLTestRunner(stream=report, title=report_title, description=report_desc)
    runner.run(suite)
