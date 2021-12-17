import requests
import unittest
from api.staff import StaffAPI
from api.login import Login_API
from common.buse_data import API
from common.DBUtils import DBUtils

class TestStaffAPI(unittest.TestCase):
    ID = None
    token = None
    @classmethod
    def setUpClass(cls) -> None:
        DBUtils().exe_sql("DELETE from bs_user where mobile = '17699999998';")
    # @classmethod
    # def tearDownClass(cls) -> None:
    #     DBUtils().exe_sql("DELETE from bs_user where mobile = '17699999998';")
    def test00_login(self):
        login_data = {
            "mobile":"13800000002",
            "password":"123456"
        }
        bb = Login_API().login_a(login_data)
        API().kk(self,bb,200,10000,True,"成功")
        TestStaffAPI.token = bb.json().get("data")
        print(TestStaffAPI().token)

    def test01_add(self):
        add_data = {
            "username":"jack2389",
            "mobile":"17699999998",
            "timeOfEntry":"2020-07-09",
            "formOfEmployment":1,
            "workNumber":"10086",
            "departmentName":"销售",
            "departmentId":"1266699057968001824",
            "correctionTime":"2020-07-30T16:00:00.000Z"
        }
        bb = StaffAPI().add(add_data,TestStaffAPI.token)
        API().kk(self,bb,200,10000,True,"成功")
        TestStaffAPI.ID = bb.json().get("data").get("id")

        result = DBUtils().exe_sql("select * from bu_user where mobile = '17699999998';")
        print(result)

    def test02_updata(self):
        updata_data = {
            "username":"rose999"
        }
        response = StaffAPI().updata_user(TestStaffAPI.ID,updata_data,TestStaffAPI.token)
        API().kk(self,response,200,10000,True,"成功")

    def test03_select(self):
        bb = StaffAPI().select_user(TestStaffAPI.ID,TestStaffAPI.token)
        API().kk(self,bb,200,10000,True,"成功")

    def test04_select(self):
        bb = StaffAPI().detele_user(TestStaffAPI.ID,TestStaffAPI.token)
        API().kk(self,bb,200,10000,True,"成功")




