import logging
import os

class Logging:
    def __init__(self):
        proDir = os.getcwd()#获取当前目录
        self.ExclPath = os.path.join(proDir, "testlogging\\testlogging.log")
        self.LOG_FORMAT = "\n\n%(asctime)s - %(levelname)s\r日志信息:%(message)s\n日志文件全路径:%(pathname)s\n日志所在行数:%(lineno)s\n日志接口:%(funcName)s\n异常及栈信息:\n"
        self.DATE_FORMAT = "%Y-%m-%d %H:%M:%S %p"
        logging.basicConfig(filename=self.ExclPath,level = logging.DEBUG,format=self.LOG_FORMAT,datefmt=self.DATE_FORMAT)

    def debuglog(self,message = 'This is a debug log.'):
        logging.debug(message,exc_info=True, stack_info=True)
    
    def infolog(self,message = 'This is a infolog log.'):
        logging.info(message,exc_info=True,stack_info=True)

    def warninglog(self,message = 'This is a warninglog log.'):
        logging.warning(message,exc_info=True,stack_info=True)
    
    def errorlog(self,message = 'This is a errorlog log.'):
        logging.error(message,exc_info=True,stack_info=True)
        
if __name__ == "__main__":
    a = Logging()
    a.debuglog()
    a.infolog()
    a.warninglog()
    a.errorlog()


