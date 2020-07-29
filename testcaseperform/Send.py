import unittest
import requests
import ddt
from tools import ReadConfig,ReadExcl
from common import DisposeCase,DisposeApi,DisposeHeader,DisposeReport,RunMain,DisposeRely,DisposeAssert
import os

case_name = "Send"

@ddt.ddt
class Send(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.runmethodhandle = RunMain.RunMethod()
        self.disposeapihandle = DisposeApi.DisposeApi()
        self.disposeheaderhandle = DisposeHeader.DisposeHeader()
        self.disposecasehandle = DisposeCase.DisposeCase(case_name)
        self.disposereporthandle = DisposeReport.DisposeReport(case_name)
        self.disposerelyhandle = DisposeRely.DisposeRely()
        self.disposeasserthandle = DisposeAssert.DisposeAssert()

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
        #测试报告用于说明
        print("正在执行用例:"+data['用例号']+",用例名称:"+data['用例名称'])
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
        try: 
            self.assertEqual(r.status_code,expectedreport['status_code'])
            if r.status_code == 200:
                self.assertIsNotNone(r.json()['verify_token'])
                #数据断言
                self.disposeasserthandle.AssertReport(expectedreport,r.json())
        except AssertionError as e:
            print(e)
            raise
        finally:
            #保存依赖数据
            self.disposerelyhandle.set_rely(data,r)
            

        
        






        
        
