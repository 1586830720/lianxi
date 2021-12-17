import requests
import config

class StaffAPI():
    def add(self,add_data,token):
        url = config.url +"/api/sys/user"
        # add_data = {
        #     "username":"jack2389",
        #     "mobile":"17687598698",
        #     "timeOfEntry":"2020-07-09",
        #     "formOfEmployment":1,
        #     "workNumber":"10086",
        #     "departmentName":"销售",
        #     "departmentId":"1266699057968001824",
        #     "correctionTime":"2020-07-30T16:00:00.000Z"
        # }
        header_data = {
            "Authorization":token
        }
        response = requests.post(url=url,json=add_data,headers=header_data)
        return response


    def updata_user(self,ID,updata_data,token):
        url = config.url + f"/api/sys/user/{ID}"
        header_data = {
            "Authorization":token
        }
        response = requests.put(url=url,json=updata_data,headers=header_data)
        return response

    def select_user(self,ID,token):
        url = config.url + f"/api/sys/user/{ID}"
        header_data = {
            "Authorization":token
        }
        reponse = requests.get(url=url,headers=header_data)
        return reponse

    def detele_user(self,ID,token):
        url = config.url + f"/api/sys/user/{ID}"
        header_data = {
            "Authorization":token
        }
        reponse = requests.delete(url=url,headers=header_data)
        return reponse
# if __name__ == '__main__':
#     print(StaffAPI().add().json())


