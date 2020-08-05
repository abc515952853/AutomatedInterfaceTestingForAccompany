from tools import ReadJson,ReadRedis
from common import FormatConversion
import json


class DisposeEnv:
    def __init__(self):
        self.readenvjsonhandle = ReadJson.ReadJson('Env','ENV')
        self.readredishandle = ReadRedis.ReadRedis()

    def set_env(self,data):
        if data['环境是否依赖'] == '是':
            jsondata = self.readenvjsonhandle.get_json_data()[data['依赖数据']]
            if "redis" in jsondata:
                for envdata in jsondata['redis']:
                    print(envdata)
            if "sql" in jsondata:
                pass
            if "api" in  jsondata:
                pass


        # #是否存入依赖
        # if data['是否存入依赖'] == '是':
        #     jsondata = self.readrelyjsonhandle.get_json_data()
        #     if data['存入字段'] != '':
        #         fromdata = data['存入字段'].split(',')
        #         todata = data['保存字段'].split(',')
        #         jsondata = self.readrelyjsonhandle.get_json_data()
        #         for i in range(len(fromdata)):
        #             #从返回json数据中获取存入字段的值
        #             reportdatavalue = self.formatconversionhandle.FormatConversion(fromdata[i],r.json())
        #             #重新赋值relyjson
        #             self.formatconversionhandle.FormatSet(reportdatavalue,todata[i],jsondata)
        #     if data['存入sql'] != '':
        #         dbdata = self.readdbhandle.search_one(data['存入sql'])
        #         todata = data['保存sql值'].split(',')
        #         for i in range(len(todata)):
        #             self.formatconversionhandle.FormatSet(dbdata[todata[i].split('.')[-1]],todata[i],jsondata)
        #     self.readrelyjsonhandle.set_json_data(jsondata)
                


