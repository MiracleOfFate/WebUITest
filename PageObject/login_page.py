from basePage.base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By

# 继承公共类
class LoginPage(BasePage):
    # 成员属性
    url = 'https://login.taobao.com/member/login.jhtml?spm=a2e0b.20350158.1997563269.1.7e9f468am5GNKe&f=top&redirectURL=https%3A%2F%2Fuland.taobao.com%2Fsem%2Ftbsearch%3Frefpid%3Dmm_26632360_8858797_29866178%26keyword%3D%25E5%25A5%25B3%25E8%25A3%2585%26clk1%3D2ce98b7bce47310ef1ea9de9d42fce6f%26upsId%3D2ce98b7bce47310ef1ea9de9d42fce6f&pid=mm_26632360_8858797_29866178&union_lens=recoveryid%3A201_11.169.50.154_8609288_1616476701826%3Bprepvid%3A201_11.169.50.154_8609288_1616476701826&clk1=2ce98b7bce47310ef1ea9de9d42fce6f'
    login_name=(By.XPATH,'//*[@id="fm-login-id"]')
    pwd=(By.XPATH,'//*[@id="fm-login-password"]')
    login_button=(By.XPATH,'//*[@id="login-form"]/div[4]/button')

    def input_username(self,username):
        self.locator(self.login_name).send_keys(username)

    def input_pwd(self,pwd):
        self.locator(self.pwd).send_keys(pwd)

    def login(self):
        self.locator(self.login_button).click()

    # 测试函数（实际中不存在）
    def check(self,username,pwd):
        self.visit(self.url)
        self.input_username(username)
        self.input_pwd(pwd)
        self.login()

if __name__=='__main__':
    driver=webdriver.Chrome()
    name='66666'
    pwd='ssssss'
    lp=LoginPage(driver)
    lp.check(name,pwd)