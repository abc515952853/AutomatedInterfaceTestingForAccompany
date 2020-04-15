from tools import ReadConfig,ReadJson
from common import FormatConversion

class DisposeApi:
    def __init__(self):
        readconfighandle = ReadConfig.ReadConfig()
        self.url = readconfighandle.get_data('INTERFACE','url_app')
        self.version = readconfighandle.get_data('INTERFACE','version_num')
        self.formatconversionhandle = FormatConversion.FormatConversion()
        self.readjsonhandle = ReadJson.ReadJson('RelyOn','RELYON')

    #获取接口完整地址
    def get_url(self,data):
        case_api = data['请求API']
        case_api_isrely = data['API是否依赖']
        if case_api_isrely == '是':
            case_data = {}
            case_api_rely= data['API依赖字段'].split(',')
            case_api_relyed = data['API被依赖字段'].split(',')
            for i in range(len(case_api_rely)):
                case_data[case_api_rely[i]] = self.get_rely_json(case_api_relyed[i])
            case_url = self.url + case_api.format(version = self.version,**case_data)
        else:
            case_url = self.url + case_api.format(version = self.version)
        return case_url

    #获取依赖json值
    def get_rely_json(self,case_api_relyed):
        jsondata = self.readjsonhandle.get_json_data()
        jsonrelydata  = self.formatconversionhandle.FormatConversion(case_api_relyed,jsondata)
        return jsonrelydata

        