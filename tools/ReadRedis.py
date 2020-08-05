import redis
from tools import ReadConfig
import os

class ReadRedis:
    def __init__(self):
        configdata = ReadConfig.ReadConfig()
        self.host =  configdata.get_data('REDIS','redis_host')
        self.port =  configdata.get_data('REDIS','redis_port')

    #打开redis
    def read_redis(self):
        try:
            pool = redis.ConnectionPool(host=self.host, port=self.port , decode_responses=True,db = 0)
            self.r = redis.Redis(connection_pool=pool)
        except Exception as ex_results:
            print("程序终止,抓了一个异常：",ex_results,)
            os._exit(0)

    #查询hash数据
    def hashgetall(self,name):
        self.read_redis()
        try:
            self.r.hgetall(name)
        except Exception as ex_results:
            print("程序终止,抓了一个异常：",ex_results,)
            os._exit(0)
    
    #删除hash数据
    def hashdelall(self,name,valuearr):
        self.read_redis()
        try:
            for value in valuearr:
                self.r.hdel(name,value)
        except Exception as ex_results:
            print("程序终止,抓了一个异常：",ex_results,)
            os._exit(0)
        



    