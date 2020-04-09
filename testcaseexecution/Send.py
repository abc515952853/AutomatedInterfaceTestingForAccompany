import unittest
import ddt
from tools import ReadExcl
# import ReadConfig 
# import requests
# import json
# import uuid 

case_name = "Send"

@ddt.ddt
class Send(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        pass

    @classmethod
    def tearDownClass(self):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @ddt.data(*ReadExcl.ReadExcl(case_name).get_xls_next())
    def test_Send(self,data):
        print('11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111')
        a = 1
        b = 2
        self.assertEqual(1,1,'1234567890')
        self.assertEqual(a,b,'1234567890')
        
        
