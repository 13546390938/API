"""
定义接口测试用例
使用unittest
"""
# 导包
import unittest,requests,json
from api.login_api import LoginAPI
from parameterized import parameterized

# 构造数据
def build_data():
    file = "../data/login.json"
    test_data = []
    with open(file, encoding="utf-8") as f:
        json_data = json.load(f)   #加载json文件数据
        for case_data in json_data:
            desc = case_data.get("desc")
            login_data = case_data.get("login_data")
            content_type = case_data.get("content_type")
            status_code = case_data.get("status_code")
            status = case_data.get("status")
            msg = case_data.get("msg")
            test_data.append((desc, login_data, content_type, status_code, status,msg))
    return test_data
# 创建测试类
class TestLogin(unittest.TestCase):

    # 前置处理
    def setUp(self) -> None:
        self.login_api = LoginAPI()                # 实例化接口类
        self.session = requests.Session()        #创建session对象

    # 后置处理
    def tearDown(self) -> None:
        if self.session:
            self.session.close()

    @parameterized.expand(build_data())
    # 创建测试用例
    def test01_login(self, desc, login_data, content_type, status_code, status, msg):
        print(desc)
        # 调用验证码接口获取验证码，并进行断言
        response = self.login_api.get_verify_code(self.session)
        self.assertEqual(status_code, response.status_code)
        self.assertIn(content_type, response.headers.get("Content-Type"))

        # 调用登录接口获取登录信息，并进行断言
        response = self.login_api.login(self.session,login_data)
        self.assertEqual(status_code, response.status_code)
        self.assertIn(msg, response.json().get("msg"))
        self.assertEqual(status, response.json().get("status"))





