import pymysql
from tools import ReadConfig
import json
import datetime


class ReadDB:
    def __init__(self):
        configdata = ReadConfig.ReadConfig()
        self.db_ip = configdata.get_data('DATABASE','db_ip')
        self.db_port = configdata.get_data('DATABASE','db_port')
        self.db_username = configdata.get_data('DATABASE','db_username')
        self.db_password = configdata.get_data('DATABASE','db_password')
        self.db_dbname = configdata.get_data('DATABASE','db_dbname')
    
    def read_db(self):
        try:
            self.conn = pymysql.connect(
                host = self.db_ip, 
                port = int(self.db_port),
                user = self.db_username,
                password = self.db_password,
                database = self.db_dbname,
                charset = "utf8",
            )
            self.cur = self.conn.cursor(cursor = pymysql.cursors.DictCursor)#数据和字段名称一起带回
        except Exception as ex_results:
            print("抓了一个异常：",ex_results)
    
    def close_db(self):
        self.conn.close()

	#查询一条数据
    def search_one(self,sql):
        self.read_db()
        try:
            self.cur.execute(sql)
            result = self.cur.fetchone()
            # result = json.dumps(result,ensure_ascii=False)   
            return result
        except Exception as ex_results:
            print("抓了一个异常：",ex_results)
        finally:
            self.close_db()


	#查询一条数据
    def search_all(self,sql):
        self.read_db()
        try:
            self.cur.execute(sql)
            result = self.cur.fetchall()
            # result = json.dumps(result,ensure_ascii=False) 
            return result
        except Exception as ex_results:
            print("抓了一个异常：",ex_results)
        finally:
            self.close_db()


	#增加/修改/删除一条数据
    def modify_data(self,sql):
        self.read_db()
        try:
            self.cur.execute(sql)
            self.conn.commit()
        except Exception as ex_results:
            self.conn.Rollback()
            print("抓了一个异常：",ex_results)
        finally:
            self.close_db()





if __name__ == "__main__":
    a = ReadDB()
    sql = "delete from test where name ='wangdachuizi '"
    a.modify_data(sql)


        