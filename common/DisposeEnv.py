from tools import ReadJson,ReadRedis,ReadDB
from common import FormatConversion
import json


class DisposeEnv:
    def __init__(self):
        self.readenvjsonhandle = ReadJson.ReadJson('Env','ENV')
        self.readredishandle = ReadRedis.ReadRedis()
        self.readdbhandle = ReadDB.ReadDB()

    def set_env(self,data):
        if data['环境是否依赖'] == '是':
            jsondata = self.readenvjsonhandle.get_json_data()[data['依赖数据']]
            if "redis" in jsondata:
                for envdata in jsondata['redis']:
                    if envdata['nodetype'] == 'Hash':
                        if envdata['nodeoperation'] == 'Add':
                            self.readredishandle.hashsetall(envdata['name'],envdata['key'],envdata['value'])
                        elif envdata['nodeoperation'] == 'Delete':
                            self.readredishandle.hashdelall(envdata['name'],envdata['key'])
                    elif envdata['nodetype'] == 'String':
                        pass
                    elif envdata['nodetype'] == 'List':
                        pass
                    elif envdata['nodetype'] == 'Set':
                        pass                             
            if "sql" in jsondata:
                self.readdbhandle.modify_data(jsondata['sql'])
            if "api" in jsondata:
                pass
                


