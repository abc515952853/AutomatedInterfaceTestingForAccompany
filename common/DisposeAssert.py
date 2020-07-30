import unittest
import types

class DisposeAssert(unittest.TestCase):
    def AssertReport(self,expectedreport,apireport):
        print(expectedreport)
        print(apireport)
        if type(expectedreport) is dict:
            for c in expectedreport.keys():
                default = self.dict_get(apireport,c,None)
                self.assertIsNotNone(default)
                self.assertEqual(expectedreport[c],default)
        elif type(expectedreport) is list:
            self.assertListEqual(expectedreport,apireport)
            

    def dict_get(self,dict, objkey, default):
        tmp = dict
        for k,v in tmp.items():
            if k == objkey:
                return v
            else:
                if type(v) is dict:
                    ret = self.dict_get(v, objkey, default)
                    if ret is not default:
                        return ret
        return default