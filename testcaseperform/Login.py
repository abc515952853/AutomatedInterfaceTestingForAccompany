import unittest
import requests
import ddt
from tools import ReadConfig,ReadExcl
from common import DisposeCase,DisposeApi,DisposeHeader,DisposeReport,RunMain

case_name = "Login"

@ddt.ddt
class Login(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.runmethodhandle = RunMain.RunMethod()
        self.disposeapihandle = DisposeApi.DisposeApi()
        self.disposeheaderhandle = DisposeHeader.DisposeHeader()
        self.disposecasehandle = DisposeCase.DisposeCase(case_name)
        self.disposereporthandle = DisposeReport.DisposeReport(case_name)

    @classmethod
    def tearDownClass(self): 
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    #数据驱动执行字段'是否执行'为是的用例
    @ddt.data(*DisposeCase.DisposeCase(case_name).get_case_data())
    def test_Login(self,data):
        #测试报告用于说明
        print("用例编号为："+data['用例号']+",用例名称为"+data['用例名称'])
        #请求接口url处理
        url = self.disposeapihandle.get_url(data)
        #请求接口hearder处理
        header = self.disposeheaderhandle.get_header(data)
        #请求接口payload处理
        payload = self.disposecasehandle.get_payload(data)
        #获取请求类型
        method = data['请求类型']
        #请求接口
        r = self.runmethodhandle.run_main(url,method,header,payload)
        #获取预期结果数据
        expectedreport = self.disposereporthandle.get_report(data)
        #断言
        if r.status_code == 200:
            pass
        else:
            pass
        self.assertEqual(r.status_code,expectedreport['status_code'],'我是测试结果的说明，想在测试报告中查看')






        
        
