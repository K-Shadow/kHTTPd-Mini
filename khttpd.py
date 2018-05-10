'''
                kHTTPd Mini Main Source file
Network framework for kHTTPd, based on the Twisted framework
'''

from twisted.internet import protocol, reactor
from khttpdmini.config.constants import httpConstants
from khttpdmini.config.config import Config
from khttpdmini.logging.logger import Logger
from khttpdmini.logging.debuglog import LogDebug
from khttpdmini.http.requesthandler import handleRequest

### Initializing some objects ###
log = Logger()
conf = Config(log)

class httpHandler(protocol.Protocol):
    
    def connectionMade(self):
        log.output('Connection made from '+ self.transport.getPeer().host + '.')
        
    def connectionLost(self, reason):
        log.output('Connection from '+ self.transport.getPeer().host +' lost.')
    
    def dataReceived(self, data):
        if httpFactory.debug is True:
            httpFactory.debuglog.output(data, self.transport.getPeer().host)
            self.transport.write(httpFactory.reqHandler.handle(data, self.transport.getPeer().host))
        else:
            self.transport.write(httpFactory.reqHandler.handle(data, self.transport.getPeer().host))
            
class httpFactory(protocol.Factory):
    protocol = httpHandler
    ### Loading settings from configuration file ###
    port = conf.getPort()
    docuroot = conf.getDocRoot()
    debug = conf.getDebug()
    index = conf.getIndexFile()
    phpenabled = conf.getPhpEnabled()
    phpexec = conf.getPhpExec()
    errorpage = httpConstants().getNotFoundPage()
    reqHandler = handleRequest(docuroot, index, errorpage, phpenabled, phpexec)
    if debug is True:
        log.output('kHTTPd Mini is starting in debug mode.')
        debuglog = LogDebug(log, index)

log.output('kHTTPd Mini Build '+ str(httpConstants().getBuild()) +' has started on port '+ str(httpFactory.port) + '.')
reactor.listenTCP(httpFactory.port, httpFactory())
reactor.run()    