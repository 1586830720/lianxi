
import unittest
class API(unittest.TestCase):
    def kk(self,caka,a,status_code,code,success,message):
        caka.assertEqual(status_code,a.status_code)
        caka.assertEqual(code,a.json().get("code"))
        caka.assertEqual(success,a.json().get("success"))
        caka.assertIn(message,a.json().get("message"))