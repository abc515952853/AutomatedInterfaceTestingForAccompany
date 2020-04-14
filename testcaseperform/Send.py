import unittest
import ddt
from tools import ReadConfig,ReadExcl
from common import DisposeCase,DisposeApi,DisposeHeader

case_name = "Send"

@ddt.ddt
class Send(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.disposeapihandle = DisposeApi.DisposeApi()
        self.disposeheaderhandle = DisposeHeader.DisposeHeader()

    @classmethod
    def tearDownClass(self): 
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    #数据驱动执行字段'是否执行'为是的用例
    @ddt.data(*DisposeCase.DisposeCase(case_name).get_case_data())
    def test_Send(self,data): 
        #请求接口url处理
        url = self.disposeapihandle.get_url(data)
        #请求接口hearder处理
        header = self.disposeheaderhandle.get_header(data)
        print(header)
        # payload = 


        
        
