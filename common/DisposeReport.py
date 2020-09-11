from tools import ReadConfig,ReadJson,ReadDB
from common import FormatConversion
import json

class DisposeReport:
    def __init__(self,casename=None):
        readconfighandle = ReadConfig.ReadConfig()
        self.url = readconfighandle.get_data('INTERFACE','url_app')
        self.version = readconfighandle.get_data('INTERFACE','version_num')
        self.formatconversionhandle = FormatConversion.FormatConversion()

        self.readreportjsonhandle = ReadJson.ReadJson(casename,'REPORT')
        self.readcasejsonhandle = ReadJson.ReadJson(casename)
        self.readdbhandle = ReadDB.ReadDB()

    #获取预期结果
    def get_report(self,data):
        case_report = data['预期结果']
        if case_report == '':
            return None
        #获取预期结果的json
        expecteddata = {}
        case_report = self.readreportjsonhandle.get_parameter(case_report)
        case_status_code = case_report['status_code']
        expecteddata["status_code"] = case_status_code

        #判断有无sql断言，如果没有则返回接口状态
        if "expected" in case_report:
            sql = case_report['expected']['sql']
            if "keyword" in case_report['expected']:
                jsondata = self.readcasejsonhandle.get_json_data()
                keyword = case_report['expected']['keyword'].split(',') 
                #通过keyword从当前用例获得sql条件，拼装完整查询sql
                sqlword = {}
                for i in range(len(keyword)): 
                    sqlword[keyword[i].split('.')[-1]] = self.formatconversionhandle.FormatConversion(keyword[i],jsondata)
                sql = sql.format(**sqlword)

            #查询数据库获得需要断言字段
            if case_report['expected']['type'] == 'ONE':
                dbdata = self.readdbhandle.search_one(sql)
                if dbdata is not None:
                    if "datalist" in case_report['expected']:
                        for dl in case_report['expected']['datalist']:
                            dbdata[dl] = dbdata[dl].split(',')
                    if "expected2" in case_report['expected']:
                        for ex in case_report['expected']['expected2']:
                            if ex['type'] =='sql':
                                dbdata[ex['key']] = self.readdbhandle.search_all(ex['value'])
            elif case_report['expected']['type'] == 'ALL':
                dbdata = self.readdbhandle.search_all(sql)
                if dbdata is not None:
                    if "datalist" in case_report['expected']:
                        # dbdata1 = []
                        for dl in case_report['expected']['datalist']:
                            for data in dbdata:
                                data[dl] = data[dl].split(',')
                        #         dbdata1.append(data[dl])
                        # dbdata = dbdata1
            expecteddata["expecteddata"] = dbdata

        #获取expectedother的预期结果
        if "expectedother" in case_report:
            if "expecteddata" in expecteddata:
                expecteddata["expecteddata"].update(case_report["expectedother"])
            else:
                expecteddata["expecteddata"] = case_report["expectedother"]

        if "asserttype" in case_report:
            expecteddata['asserttype'] = case_report['asserttype']
        return expecteddata

