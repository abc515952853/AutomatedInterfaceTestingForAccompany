import sys
import os

class ReadTxt:
    def __init__(self):
        proDir = os.getcwd()#获取当前目录
        self.txtPath = os.path.join(proDir, "configurationfile\caselist.txt")
        self.caseList = []

    def open_txt(self):
        try:
            self.fb = open(self.txtPath)
        except Exception as ex_results:
            print("抓了一个异常：",ex_results)
    
    def close_txt(self):
        self.fb.close()

    #获取txt文件中需要执行的接口
    def get_case_list(self):
        self.open_txt()
        for value in self.fb.readlines():
            data = str(value)
            if data != '' and not data.startswith("#"):
                self.caseList.append(data.replace("\n", ""))
        self.close_txt()
        return self.caseList


if __name__ == "__main__":
    a = ReadTxt()
    a.get_case_list()
