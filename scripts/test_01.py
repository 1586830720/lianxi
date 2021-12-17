import unittest
from common.buse_data import API
from api.login import Login_API

class login_api(unittest.TestCase):
    def test01_login(self):

        bb = Login_API().login_a(data_login={"mobile":"13800000002","password":"123456"})
        # API().kk(self,bb,200,10000,True,"成功")
        print(bb.json())
        # self.assertEqual(200,a.status_code)
        # self.assertEqual(10000,a.json().get("code"))
        # self.assertEqual(True,a.json().get("success"))
        # self.assertIn("成功",a.json().get("message"))
    def test02_login(self):
        bb = Login_API().login_a(data_login={"mobile": "13800999002", "password": "123456"})
        API().kk(self, bb, 200, 20001, False, "错误")

        # a = Login_API().login_a(data_login={"mobile":"13833300002","password":"123456"})
        # self.assertEqual(200,a.status_code)
        # self.assertEqual(20001,a.json().get("code"))
        # self.assertEqual(False,a.json().get("success"))
        # self.assertIn("错误",a.json().get("message"))

    def test03_login(self):
        bb = Login_API().login_a(data_login={"mobile": "13800000002", "password": "123336"})
        API().kk(self, bb, 200, 20001, False, "错误")

        # a = Login_API().login_a(data_login={"mobile":"13800000002","password":"123457"})
        # self.assertEqual(200,a.status_code)
        # self.assertEqual(20001,a.json().get("code"))
        # self.assertEqual(False,a.json().get("success"))
        # self.assertIn("错误",a.json().get("message"))