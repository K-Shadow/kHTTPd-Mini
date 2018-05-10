'''
                kHTTPd Mini Logger
Logs events or errors that occur to the console and a log file.
'''

from khttpdmini.utils.timehandler import TimeHandler
from khttpdmini.config.constants import httpConstants

class Logger:
    
    def __init__(self):
        pass
    
    def output(self, data):
        out = '['+ TimeHandler().getLocalTime() +'] '+ data
        print out
        with open(httpConstants().getLog(), 'a') as logfile:
            logfile.write(out + '\n')