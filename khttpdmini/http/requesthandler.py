'''
                kHTTPd Mini Request Handler
Determines a request type from data received from the client, and sends the data to the correct parser.
'''

from khttpdmini.http.parseget import parseGet
from khttpdmini.http.parsepost import parsePost
from khttpdmini.http.sendpage import PageSender
from khttpdmini.php.phphandler import handlePhp
import os

class handleRequest:
    
    def __init__(self, docroot, index, errorpage, phpstate, phpexec):
        self.docroot = docroot
        self.errorpage = errorpage
        self.index = index
        self.sender = PageSender(self.docroot, self.errorpage)
        self.php = handlePhp(self.docroot, phpexec, self.errorpage)
        self.phpstate = phpstate
        
    def handle(self, request, remoteaddr):
        if request.startswith('GET /'):
            try:
                ### Begin to parse the GET request ###
                self.get = parseGet(self.docroot, self.index, request)
                self.page = self.get.getReqPage()
                ### If the HTTP version is 1.1, begin page processing phase ###
                if self.get.getProto() == '1.1':
                    ### Fixing directory paths ###
                    if os.path.isdir(self.docroot + self.page) is True:
                        if not self.page.endswith('/'):
                            self.newLocation = 'http://' + self.get.getHost() + self.page + '/' + self.index
                            return self.sender.sendNewLocation(self.newLocation)
                        else:
                            self.page = self.page + self.index
                    
                    ### Handles PHP page sending ###
                    if self.page.endswith('.php'):
                        if self.phpstate is True:
                            self.php.setEnvVars(self.get.getVars(), 'GET', os.path.abspath(self.docroot + self.page), 
                                                remoteaddr, '', '', self.get.getUri())    
                            if self.get.getCookie() != '':
                                self.php.setCookie(self.get.getCookie())                  
                            page =  self.php.parse(self.page, self.get.getVars())
                            self.php.clearVars()
                            return page
                        else:
                            return self.sender.sendNotFound()
                        
                    ### Send page normally ###
                    else:
                        return self.sender.openPage(self.page)
                    
                ### If HTTP protocol is not 1.1, send 505 error ###
                else:
                    return self.sender.sendNotSupported()
            
            ### If the request type is correct but can't be parsed, send 400 error ###
            except:
                return self.sender.sendBadRequest()
        
        elif request.startswith('POST /'):
            try:
                ### Begin to parse the POST request ###
                self.post = parsePost(self.docroot, self.index, request)
                self.page = self.post.getReqPage()         
                ### If the HTTP version is 1.1, begin page processing phase ###
                if self.post.getProto() == '1.1':
                    ### Fixing directory paths ###
                    if os.path.isdir(self.docroot + self.page) is True:
                        if not self.page.endswith('/'):
                            self.newLocation = 'http://' + self.post.getHost() + self.page + '/' + self.index
                            return self.sender.sendNewLocation(self.newLocation)
                        else:
                            self.page = self.page + self.index
                
                    ### Handles PHP page sending ###
                    if self.page.endswith('.php'):
                        if self.phpstate is True:
                            self.php.setEnvVars(self.post.getVars(), 'POST', os.path.abspath(self.docroot + self.page), 
                                                remoteaddr, self.post.getContentType(), self.post.getContentLength(), self.page)
                            if self.post.getCookie() != '':
                                self.php.setCookie(self.get.getCookie())
                            page = self.php.parse(self.page, self.post.getVars())
                            self.php.clearVars()
                            return page
                        else:
                            return self.sender.sendNotFound()
                        
                    ### Send page normally ###
                    else:
                        return self.sender.openPage(self.page) 
                               
                ### If HTTP protocol is not 1.1, send 505 error ###
                else:
                    return self.sender.sendNotSupported()
                     
            except:
                return self.sender.sendInternalError()
        ### If request type is not handled by the server, send 501 error ###
        else:
            return self.sender.sendNotImplemented()
            