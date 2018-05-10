'''
                kHTTPd Mini PHP Handler
Handles passing on requests for .php pages to php-cgi.
'''

from subprocess import PIPE, Popen
from khttpdmini.http.responsehandler import createResponse
from khttpdmini.config.responsecodes import *
from khttpdmini.http.sendpage import PageSender
import os

class handlePhp:
    
    def __init__(self, docroot, phpexec, errorpage):
        self.docroot = docroot
        self.phpexec = phpexec
        self.response = createResponse()
        self.error = PageSender(self.docroot, errorpage)
    
    def checkPage(self, page):
        path = self.docroot + page
        if os.path.isfile(path):
            return True
        else:
            return False
    
    def setEnvVars(self, querystring, reqtype, scriptpath, remoteaddr, ctype, clength, requri):
        os.putenv('SERVER_SOFTWARE', 'kHTTPd Mini')
        os.putenv('GATEWAY_INTERFACE', 'CGI/1.1')
        os.putenv('SERVER_PROTOCOL', 'HTTP/1.1')
        os.putenv('REDIRECT_STATUS', 'true')
        os.putenv('REMOTE_ADDR', remoteaddr)
        os.putenv('SCRIPT_FILENAME', scriptpath)
        os.putenv('REQUEST_METHOD', reqtype)
        os.putenv('REQUEST_URI', requri)
        if reqtype == 'GET':
            os.putenv('QUERY_STRING', querystring)
        if reqtype == 'POST':
            os.putenv('CONTENT_TYPE', ctype)
            os.putenv('CONTENT_LENGTH', clength)
    
    def setCookie(self, cookie):
        os.putenv('HTTP_COOKIE', cookie)
    
    def clearVars(self):
        os.putenv('SERVER_SOFTWARE', '')
        os.putenv('GATEWAY_INTERFACE', '')
        os.putenv('SERVER_PROTOCOL', '')
        os.putenv('REDIRECT_STATUS', '')
        os.putenv('REMOTE_ADDR', '')
        os.putenv('SCRIPT_FILENAME', '')
        os.putenv('REQUEST_METHOD', '')
        os.putenv('QUERY_STRING', '')
        os.putenv('CONTENT_TYPE', '')
        os.putenv('CONTENT_LENGTH', '')
        os.putenv('HTTP_COOKIE', '')
        
    def parse(self, page, request):
        path = self.docroot + page
        if self.checkPage(page) is True:
            phpProc = Popen([self.phpexec, path], stdout=PIPE, stdin=PIPE)
            out, err = phpProc.communicate(input=request)
            page = out.split('\r\n\r\n', 1)[1] ### Actual page content returned from php-cgi ###
            headers = out.split('\r\n\r\n', 1)[0]
            return self.response.phpCreate(complete, headers, page)
        else:
            return self.error.sendNotFound()