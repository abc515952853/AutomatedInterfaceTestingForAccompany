from tools import ReadExcl


class DisposeCase:
    def __init__(self,casename):
        self.casedata = ReadExcl.ReadExcl(casename).get_xls_next()

    #剔除是否执行为否的用例
    def get_case_data(self):
        casedata = []
        for data in self.casedata:
            if data['是否执行'] == '是':
                casedata.append(data)
        return casedata


# if __name__ == "__main__":
#     a = DisposeCase()




