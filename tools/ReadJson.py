import json
import os

class ReadJson:
    def __init__(self,jsonname):
        self.casename = jsonname
        proDir = os.getcwd()#获取当前目录
        self.JsonPath = os.path.join(proDir, "testcasejson\{0}.json".format(jsonname))

    def read_json(self):
        try:
            self.fb = open(self.JsonPath)
        except Exception as ex_results:
            print("抓了一个异常：",ex_results)

    def close_json(self):
        self.fb.close()

#     #获取json文件中数据
    def get_json_data(self):
        self.read_json()
        self.data = json.load(self.fb)
        print(self.data)
        self.close_json()
        return self.data

    #获取指定的参数
    def get_parameter(self,parameter):
        data = self.get_json_data()
        return data[parameter]
        

if __name__ == "__main__":
    a = ReadJson('Send')
    a.get_parameter('send001')