"""
Qxf2 Services: A plug-n-play class for logging.
This class wraps around Python's logging module.
"""

import logging, os, inspect
import datetime
import sys

class Base_Logging():

    def __init__(self,log_file_name=None,level=logging.DEBUG,format='%(asctime)s|%(caller_func)s|%(levelname)s| %(message)s'):
        "Constructor for the logging class"
        self.log_file_name=log_file_name
        self.level=level
        self.format=format
        self.log = self.set_log(self.log_file_name,self.level,self.format)
        
        
    def set_log(self,log_file_name,level,format,test_module_name=None):
        "Set logging: 1 stream handler, one file handler"
        if test_module_name is None:
            test_module_name = self.get_calling_module()
        log = logging.getLogger(test_module_name)
        self.reset_log(log)
        self.set_log_level(log,level)
        self.add_stream_handler(log,level,format)
        if log_file_name is None:
            log_file_name = test_module_name + '.log'
        self.add_file_handler(log,level,format,log_file_name)

        return log
    

    def get_calling_module(self):
        "Get the name of the module"
        self.calling_module = inspect.stack()[-1][1].split(os.sep)[-1].split('.')[0]

        return self.calling_module

    
    def reset_log(self,log):
        "Reset the log handlers if they exist"
        try:
            log.handlers = []
        except Exception,e:
            print 'Failed to close the logger object'
            print 'Exception', e
            

    def set_log_level(self,log,level=logging.INFO):
        log.setLevel(level)
        

    def set_stream_handler_level(self,streamHandler,level):
        streamHandler.setLevel(level)


    def set_stream_handler_formatter(self,streamHandler,formatter):
        streamHandler.setFormatter('')


    def add_stream_handler(self,log,handlerLevel,handlerFormat):
        streamHandler = logging.StreamHandler()
        self.set_stream_handler_level(streamHandler,handlerLevel)
        self.set_stream_handler_formatter(streamHandler,handlerFormat)
        log.addHandler(streamHandler)


    def set_file_handler_level(self,fileHandler,level):
        fileHandler.setLevel(level)


    def set_file_handler_formatter(self,fileHandler,formatter):
        fileHandler.setFormatter(formatter)


    def add_file_handler(self,log,handlerLevel,handlerFormat,log_file_name):
        fileHandler = logging.FileHandler(log_file_name)
        self.set_file_handler_level(fileHandler,handlerLevel)
        formatter = logging.Formatter(handlerFormat)
        self.set_file_handler_formatter(fileHandler,formatter)
        log.addHandler(fileHandler)


    def write(self,msg,level='info'):
        fname = inspect.stack()[2][3] #May be use a entry-exit decorator instead
        d = {'caller_func': fname}
        if level.lower()== 'debug':
            self.log.debug(msg, extra=d)
        elif level.lower()== 'info':
            self.log.info(msg, extra=d)    
        elif level.lower()== 'warn' or level.lower()=='warning':
            self.log.warn(msg, extra=d)
        elif level.lower()== 'error':
            self.log.error(msg, extra=d)
        elif level.lower()== 'critical':
            self.log.critical(msg, extra=d)
        else:
            self.log.critical("Unknown level passed for the msg: %s", msg, extra=d)
        

    
