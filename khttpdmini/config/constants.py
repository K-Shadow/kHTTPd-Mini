'''
                kHTTPd Mini constants
File to store constants of the program, such as the build number, etc
'''

class httpConstants:
    
    def __init__(self):
        
        ### Current build number ###
        self.build = 18
        ### Config file location ###
        self.conf = 'khttpd.conf'
        ### Log file location ###
        self.log = 'khttpd.log'
        ### 404 error file location ###
        self.notFoundPage = 'www/404.html'
        
    def getBuild(self):
        return self.build
    
    def getConf(self):
        return self.conf
    
    def getLog(self):
        return self.log
    
    def getNotFoundPage(self):
        return self.notFoundPage