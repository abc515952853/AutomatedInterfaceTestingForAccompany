from tools import ReadJson
from common import FormatConversion
import json


class DisposeRely:
    def __init__(self):
        self.formatconversionhandle = FormatConversion.FormatConversion()
        self.readrelyjsonhandle = ReadJson.ReadJson('RelyOn','RELYON')

    def set_rely(self,data,r):
        #是否存入依赖
        if data['是否存入依赖'] == '是':
            fromdata = data['存入字段'].split(',')
            todata = data['保存字段'].split(',')

            for i in range(len(fromdata)):
                #从返回json数据中获取存入字段的值
                reportdatavalue = self.formatconversionhandle.FormatConversion(fromdata[i],r.json())

                #重新赋值relyjson
                jsonrelydata = self.formatconversionhandle.get_rely_json(reportdatavalue,todata[i])

                # #将值存入依赖json
                # self.formatconversionhandle


    def get_rely_json(self,reportdatavalue,todata):
        jsondata = self.readrelyjsonhandle.get_json_data()
        jsonrelydata  = self.formatconversionhandle.FormatSet(reportdatavalue,todata,jsondata)
        return jsonrelydata

