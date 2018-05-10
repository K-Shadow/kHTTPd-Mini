'''
                kHTTPd Mini Config File Reader
Configuration parser to read the kHTTPd Mini configuration file
'''

from ConfigParser import RawConfigParser
from constants import httpConstants

class Config:
    
    def __init__(self, logger):
        self.logger = logger
        try:
            self.conf = RawConfigParser()
            self.file = httpConstants().getConf()
            self.conf.read(self.file)
            self.logger.output('kHTTPd Mini config file loaded.')
        except:
            self.logger.output('Can\'t open kHTTPd Mini config file!')
        
    def getDocRoot(self):
        try:
            return self.conf.get('main', 'root')
        except:
            self.logger.output('Can\'t load document root setting of server from '+ self.file +', defaulting to www.')
            return 'www'
    
    def getPort(self):
        try:
            return self.conf.getint('main', 'port')
        except:
            self.logger.output('Can\'t load port to bind server to from '+ self.file +', defaulting to port 80.')
            return 80
    
    def getDebug(self):
        try:
            return self.conf.getboolean('main', 'debugmode')
        except:
            self.logger.output('Can\'t load debug mode setting from '+ self.file +', defaulting to off.')
            return False
    
    def getIndexFile(self):
        try:
            return self.conf.get('main', 'indexfile')
        except:
            self.logger.output('Can\'t load index file setting from '+ self.file +', defaulting to index.html.')
            return 'index.html'
        
    def getPhpEnabled(self):
        try:
            return self.conf.getboolean('php', 'phpenabled')
        except:
            self.logger.output('Can\'t load PHP mode setting from '+ self.file +', defaulting to off.')
            return False
        
    def getPhpExec(self):
        try:
            return self.conf.get('php', 'name')
        except:
            self.logger.output('Can\'t load PHP executable name from '+ self.file +', defaulting to php-cgi.')
            return 'php-cgi'