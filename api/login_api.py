"""
被测系统接口封装
获取验证码： http://localhost/index.php?m=Home&c=User&a=verify
登录： http://localhost/index.php?m=Home&c=User&a=do_login
"""


# 导包
import requests

# 定义类
class LoginAPI:

    # 初始化
    def __init__(self):
        self.verify_url = "http://localhost/index.php?m=Home&c=User&a=verify"
        self.logion_url = "http://localhost/index.php?m=Home&c=User&a=do_login"

    # 发送请求,获取验证码
    def get_verify_code(self, session):
        return session.get(self.verify_url)


    #登录
    def login(self, session, login_data):
        # login_data = {
        #     "username": username,
        #     "password": password,
        #     "verify_code": verify_code
        # }
        return session.post(url=self.logion_url,data=login_data)
