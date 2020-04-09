import xlrd
import xlwt
from xlutils.copy import copy
import os
from datetime import datetime
from xlrd import xldate_as_tuple

class ReadExcl:
    def __init__(self,casename):
        self.casename = casename
        proDir = os.getcwd()#获取当前目录
        self.ExclPath = os.path.join(proDir, "testcasefile\{0}.xls".format(casename))

    def read_excl(self):
        try:
            self.readfile = xlrd.open_workbook(self.ExclPath,'w',formatting_info= True)
        except Exception as ex_results:
            print("抓了一个异常：",ex_results)

    def write_excl(self):
        self.read_excl()
        try:
            self.newfile = copy(self.readfile)
        except Exception as ex_results:
            print("抓了一个异常：",ex_results)

    def save_excl(self):
        self.newfile.save(self.ExclPath)

    #遍历sheet中的用例
    def get_xls_next(self):
        self.read_excl()
        sheet = self.readfile.sheet_by_name(self.casename)
        row = sheet.row_values(0)
        rowNum  = sheet.nrows
        colNum = sheet.ncols 
        
        cls = []
        curRowNo = 1
        while self.hasNext(rowNum,curRowNo):
            s = {}  
            col = sheet.row_values(curRowNo)  
            i = colNum  
            for x in range(i):
                s[row[x]] = self.conversion_cell(sheet,curRowNo,x,col[x])
            cls.append(s)  
            curRowNo += 1
        return cls

    def hasNext(self,rownum,curRowNo):  
        if rownum == 0 or rownum <= curRowNo :  
            return False  
        else:  
            return True  

    #将读取excl整形的float，转换成int
    def conversion_cell(self,sheet,curRowNo,curColNo,cell):
        #判断python读取的返回类型  0 --empty,1 --string, 2 --number(都是浮点), 3 --date, 4 --boolean, 5 --error  
        if sheet.cell(curRowNo,curColNo).ctype == 2:
             no = int(cell)
             
        elif sheet.cell(curRowNo,curColNo).ctype == 3:
            # 转成datetime对象
            date = datetime(*xldate_as_tuple(cell, 0))
            no = date.strftime('%Y-%m-%d')
        else:
             no = cell
        return no


if __name__ == '__main__':
    a = ReadExcl('Send')
    print(a.get_xls_next())

    