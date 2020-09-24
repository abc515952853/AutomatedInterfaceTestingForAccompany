import json
import datetime

class DisposeSpecial:
    def DictToList(self,expectedreport):
        expectedreport1 = {}
        expecteddata1 = []
        expectedreport1['status_code'] = expectedreport['status_code']
        for i in expectedreport['expecteddata']:
            expecteddata1 = expecteddata1+list(i.values())
        expectedreport1['expecteddata'] = expecteddata1
        return expectedreport1

    #接口DoctorArea特殊处理
    def DoctorAreaSpecial(self,expectedreport):
        expectedreport1 = self.DictToList(expectedreport)
        return expectedreport1

    #接口FullDate特殊处理
    def FullDateSpecial(self,expectedreport):
        expectedreport1 = self.DictToList(expectedreport)
        #时间范围12点
        d_time =  datetime.datetime.strptime(str(datetime.datetime.now().date())+'12:00', '%Y-%m-%d%H:%M')
        # 当前时间
        n_time = datetime.datetime.now()
        # 判断当前时间是否在范围时间内
        if n_time > d_time:
            expectedreport1['expecteddata'].append(str(datetime.datetime.now().date())+' 上午')
        return expectedreport1

    #接口MeDynamic特殊处理
    def MeDynamicSpecial(self,expectedreport):
        for data in expectedreport['expecteddata']:
            for i in range(len(data['images'])):
                data['images'][i] = 'http://i.peiban85.com/'+data['images'][i]
            if len(data['voice']) != 0:
                data['voice'] = 'http://i.peiban85.com/'+data['voice'] 
            if  len(data['publisher']['avatar']) !=0:
                data['publisher']['avatar'] ='http://i.peiban85.com/'+data['publisher']['avatar']
            data['isCanDelete'] = True
            data['isPraised'] = False
            if len(data['images']) != 0:
                data['share']['shareImage'] = data['images'][0]
        return expectedreport

    #接口Follow特殊处理
    def FollowSpecial(self,expectedreport):
        if  "expecteddata" in expectedreport:
            expectedreport['expecteddata']['followId'] = expectedreport['expecteddata'].pop('userid')
        return expectedreport
    
    #接口ChinaDoctorAgentMy特殊处理
    def ChinaDoctorAgentMySpecial(self,expectedreport):
        if  "expecteddata" in expectedreport:
            expectedreport['expecteddata']['sales'] = float(expectedreport['expecteddata']['sales'])
        return expectedreport
    
        
        