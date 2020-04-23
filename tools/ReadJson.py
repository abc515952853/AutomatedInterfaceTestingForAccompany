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
            self.fb = open(self.JsonPath,"r",encoding='utf-8-sig')
        except Exception as ex_results:
            print("程序终止,抓了一个异常：",ex_results,)
            os._exit(0)

    def close_json(self):
        self.fb.close()

    def write_json(self):
        try:
            self.fb = open(self.JsonPath,"w",encoding='utf-8-sig')
        except Exception as ex_results:
            print("程序终止,抓了一个异常：",ex_results,)
            os._exit(0)

#     #获取json文件中数据
    def get_json_data(self):
        self.read_json()
        try:
            self.data = json.load(self.fb)
            self.close_json()
            return self.data
        except Exception as ex_results:
            print("程序终止,抓了一个异常：",ex_results,)
            os._exit(0)

    #获取指定的参数
    def get_parameter(self,parameter):
        try:
            data = self.get_json_data()
            return data[parameter]
        except Exception as ex_results:
            print("程序终止,抓了一个异常：",ex_results,)
            os._exit(0)
        

    def set_json_data(self,new_dict):
        self.write_json()
        try:
            json.dump(new_dict,self.fb)
            self.close_json()
        except Exception as ex_results:
            print("程序终止,抓了一个异常：",ex_results,)
            os._exit(0)

        

if __name__ == "__main__":
    a = ReadJson('Send')
    a.get_parameter('send001')