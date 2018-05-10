'''
                kHTTPd Mini Response Handler
Handles creating a response template for sending replies to clients.
'''

from khttpdmini.utils.timehandler import TimeHandler
from khttpdmini.config.constants import httpConstants

class createResponse:
    
    def __init__(self):
        pass
    
    def create(self, code, mimetype, data):
        return 'HTTP/1.1 %s\r\n' % (code) + \
                'Date: %s\r\n' % (TimeHandler().getGMTime()) + \
                'Server: kHTTPd Mini Build %i\r\n' % (httpConstants().getBuild()) + \
                'Content-Type: %s\r\n' % (mimetype) + \
                'Content-Length: %i\r\n\r\n' % (len(data)) + data
                
    def phpCreate(self, code, headers, data):
        return 'HTTP/1.1 %s\r\n' % (code) + \
                'Date: %s\r\n' % (TimeHandler().getGMTime()) + \
                'Server: kHTTPd Mini Build %i\r\n' % (httpConstants().getBuild()) + \
                '%s\r\n' % (headers) + \
                'Content-Length: %i\r\n\r\n' % (len(data)) + data
                