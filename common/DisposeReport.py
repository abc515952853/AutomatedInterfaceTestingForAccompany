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
        if "expected" not in case_report:
            return expecteddata
        jsondata = self.readcasejsonhandle.get_json_data()
        keyword = case_report['expected']['keyword'].split(',')
        #通过keyword从当前用例获得sql条件，拼装完整查询sql
        sqlword = {}
        for i in range(len(keyword)): 
            sqlword[keyword[i].split('.')[-1]] = self.formatconversionhandle.FormatConversion(keyword[i],jsondata)
        sql = case_report['expected']['sql']
        sql = sql.format(**sqlword)
        #查询数据库获得需要断言字段
        if case_report['expected']['type'] == 'ONE':
            dbdata = self.readdbhandle.search_one(sql)
        elif case_report['expected']['type'] == 'ALL':
            dbdata = self.readdbhandle.search_all(sql)
        #合并返回值字典和数据库的值 返回用例
        if dbdata is not None:
            reportdatamerged ={}
            reportdatamerged = dict(expecteddata)
            reportdatamerged.update(dbdata)
        
        #获取expectedother的预期结果
        if "expectedother" not in case_report:
            return reportdatamerged
        reportdatamerged.update(case_report["expectedother"])
        return reportdatamerged

