class FormatConversion:
    #字符串A.B转换成A[B]并返回值
    def FormatConversion(self,data,jsondata):
        relyeddata = data.split('.')
        for i in range(len(relyeddata)):
            if i == 0:
                data = jsondata[relyeddata[i]]
            else:
                data = data[relyeddata[i]]
        return  data        
