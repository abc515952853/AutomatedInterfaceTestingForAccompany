import json
import os

class ReadJson:
    def __init__(self,jsonname,type='CASE'):
        self.casename = jsonname
        proDir = os.getcwd()#获取当前目录
        if type == 'RELYON':
            self.JsonPath = os.path.join(proDir, "testrelyonjson\{0}.json".format(jsonname))
        elif type == 'HEADER':
            self.JsonPath = os.path.join(proDir, "testheaderjson\{0}.json".format(jsonname))
        elif type == 'REPORT':
            self.JsonPath = os.path.join(proDir, "testreportjson\{0}.json".format(jsonname))
        else:
            self.JsonPath = os.path.join(proDir, "testcasejson\{0}.json".format(jsonname))

    def read_json(self):
        try:
            self.fb = open(self.JsonPath,encoding='utf-8-sig')
        except Exception as ex_results:
            print("程序终止,抓了一个异常：",ex_results,)
            os._exit(0)

    def close_json(self):
        self.fb.close()

#     #获取json文件中数据
    def get_json_data(self):
        self.read_json()
        self.data = json.load(self.fb)
        self.close_json()
        return self.data

    #获取指定的参数
    def get_parameter(self,parameter):
        data = self.get_json_data()
        return data[parameter]
        

if __name__ == "__main__":
    a = ReadJson('Send')
    a.get_parameter('send001')