import unittest
import requests
import ddt
from tools import ReadConfig,ReadExcl,ReadDB,ReadTxt
from common import DisposeCase,DisposeApi,DisposeHeader,DisposeReport,RunMain

case_name = "Common"

@ddt.ddt
class Common(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.runmethodhandle = RunMain.RunMethod()
        self.disposeapihandle = DisposeApi.DisposeApi()
        self.disposeheaderhandle = DisposeHeader.DisposeHeader()
        self.disposecasehandle = DisposeCase.DisposeCase(case_name)
        self.disposereporthandle = DisposeReport.DisposeReport(case_name)
        self.readdbhandle = ReadDB.ReadDB()
        self.readtxthandle = ReadTxt.ReadTxt('cleardata')


        # #清除测试数据
        # sql = self.readtxthandle.get_clear_data()
        # print('-------------------开始清除原测试数据-------------------')
        # self.readdbhandle.modify_data(sql)
        # print('-------------------结束清除原测试数据-------------------')
        # print('--------------------开始创建测试数据--------------------')

    @classmethod
    def tearDownClass(self):
        print('--------------------结束创建测试数据--------------------')
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    #数据驱动执行字段'是否执行'为是的用例
    @ddt.data(1)
    def test_Common(self,data):
        case = DisposeCase.DisposeCase(case_name).get_case_data()
        for data in case:
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
            #断言
            if r.status_code == 200:
                pass
                print("用例编号："+data['用例号']+",用例名称:"+data['用例名称']+',执行成功')
            else:
                pass
                print("用例编号："+data['用例号']+",用例名称:"+data['用例名称']+',执行失败')







        
        
