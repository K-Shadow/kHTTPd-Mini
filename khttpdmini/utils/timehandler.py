'''
                kHTTPd Mini Time Handler
Gets the current GMT time to respond to an HTTP request.
'''

from time import strftime, localtime, gmtime

class TimeHandler:
    
    def __init__(self):
        pass
    
    def getGMTime(self):
        return strftime('%a, %d %b %Y %X GMT', gmtime())
    
    def getLocalTime(self):
        return strftime('%a, %d %b %Y %X', localtime())