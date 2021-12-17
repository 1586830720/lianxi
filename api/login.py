import requests
import config
class Login_API():
    def login_a(self,data_login):
        url = config.url + "/api/sys/login"
        log = requests.post(url=url,json=data_login)
        # print(log)
        return log

if __name__ == '__main__':
    print(Login_API().login_a({"mobile":"13800000002","password":"123456"}).json())