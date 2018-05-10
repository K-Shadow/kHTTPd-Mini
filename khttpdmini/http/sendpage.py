'''
                kHTTPd Mini Page Handler
Handles opening pages, and sending them to the client.
'''

from khttpdmini.utils.filetypehandler import MimeHandler
from khttpdmini.http.responsehandler import createResponse
from khttpdmini.config.responsecodes import *
from khttpdmini.config.constants import httpConstants
from khttpdmini.utils.timehandler import TimeHandler

class PageSender:
    
    def __init__(self, docroot, errorpage):
        self.docroot = docroot
        self.errorpage = errorpage
        self.response = createResponse()
    
    def openPage(self, page):
        path = self.docroot + page
        if MimeHandler().getType(page).startswith('image/'):
            try:
                page = open(path, 'rb').read()
                return self.response.create(complete, MimeHandler().getType(path), page)
            except:
                if page.endswith('.ico'):
                    pass
                else:
                    return self.sendNotFound()
        else:
            try:
                page = open(path, 'r').read()
                return self.response.create(complete, MimeHandler().getType(path), page)
            except:
                return self.sendNotFound()
            
    def sendNotFound(self):
        try:
            page = open(self.errorpage, 'r').read()
            return self.response.create(notFound, MimeHandler().getType(self.errorpage), page)
        except:
            return self.response.create(notFound, 'text/html', '<h1>404 Not Found</h1>')
        
    def sendBadRequest(self):
        return self.response.create(badRequest, 'text/html', '<h1>400 Bad Request</h1>')
    
    def sendNotSupported(self):
        return self.response.create(notSupported, 'text/html', '<h1>505 HTTP Version Not Supported</h1>')
    
    def sendNotImplemented(self):
        return self.response.create(notImplemented, 'text/html', '<h1>501 Not Implemented</h1>')
    
    def sendInternalError(self):
        return self.response.create(serverError, 'text/html', '<h1>500 Internal Server Error</h1>')
    
    def sendNewLocation(self, location):
        response = '<h1>301 Moved Permanently</h1>'
        return 'HTTP/1.1 %s\r\n' % (movedPerm) + \
                'Date: %s\r\n' % (TimeHandler().getGMTime()) + \
                'Server: kHTTPd Mini Build %i\r\n' % (httpConstants().getBuild()) + \
                'Content-Type: text/html\r\n' + \
                'Content-Length: %i\r\n' % (len(response)) + \
                'Location: %s\r\n\r\n' % (location) + response