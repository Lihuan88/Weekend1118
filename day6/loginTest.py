import time

from day5.myTestCase import MyTestCase
from day6.page_object.loginPage import LoginPage
from day6.page_object.personalCenterPage import PersonalCenterPage


class LoginTest(MyTestCase):
    def test_login(self):
        #现在这种测试用例可读性比较差，维护起来比较困难，那么测试用例写成什么样可读性比较好呢？
        #1.打开网页
       # self.driver.get("")
        lp = LoginPage(self.driver)  # 实例化一个登录页面
        lp.open()
        #2.输入用户名
       #self.driver.find_element(By.ID,"username").send_keys("ada")
        lp.input_username("ada")


        #self.driver.find_element_by_id("username") 同上
        #3.输入密码
       # self.driver.find_element(By.ID,"password").send_keys("123456")
        lp.input_password("123456")

        #4.点击登陆按钮
        #self.driver.find_element(By.CLASS_NAME,"login_btn").click()
        lp.click_login_button()

        #5.验证是否跳转到管理中心页面
       # time.sleep(5)
        #expectesd = "用户登录 - 道e坊商城 - Powered by Haidao"
       # self.assertIn("我的会员中心",self.driver.title)
        pcp = PersonalCenterPage(self.driver)
        time.sleep(5)
        self.assertEqual(pcp.title,self.driver.title)
