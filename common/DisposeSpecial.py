import json

class DisposeSpecial:
    def DictToList(self,expectedreport):
        expectedreport1 = {}
        expecteddata1 = []
        expectedreport1['status_code'] = expectedreport['status_code']
        for i in expectedreport['expecteddata']:
            expecteddata1 = expecteddata1+list(i.values())
        expectedreport1['expecteddata'] = expecteddata1
        return expectedreport1
        