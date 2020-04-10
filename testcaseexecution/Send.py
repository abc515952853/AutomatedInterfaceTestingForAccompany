import unittest
import ddt
from tools import ReadExcl,ReadDB

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
        print(data)

        
        
