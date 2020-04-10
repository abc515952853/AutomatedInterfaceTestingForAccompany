import unittest
import ddt
from tools import ReadExcl,ReadDB,ReadConfig

case_name = "Send"

@ddt.ddt
class Send(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        readconfighandle = ReadConfig.ReadConfig()
        self.url = readconfighandle.get_data('INTERFACE','url_app')
        self.version = readconfighandle.get_data('INTERFACE','version_num')

    @classmethod
    def tearDownClass(self): 
        pass

    def setUp(self):

        pass

    def tearDown(self):
        pass

    @ddt.data(*ReadExcl.ReadExcl(case_name).get_xls_next())
    def test_Send(self,data):
        case_isperform = data['是否执行']
        if case_isperform =='否':
            return

        
        
