'''
                kHTTPd Post Request Parser
Used to get information from a post request, such as the requested page.
'''

class parsePost:
    
    def __init__(self, docroot, index, request):
        self.docroot = docroot
        ### Parse host from the request ###
        self.host = request.split('Host: ')[1].split('\r\n')[0]
        ### Get page from the POST request ###
        self.page = request.split(' HTTP/1.1')[0].split('POST ')[1]
        ### Parse the protocol version ###
        self.postproto = request.split(' HTTP/')[1].split('\r\n')[0]
        ### Parse the connection type ###
        self.conntype = request.split('Connection: ')[1].split('\r\n')[0]
        ### Parse the variables ###
        try:
            self.requestvars = request.split('\r\n\r\n', 1)[1]
        except:
            self.requestvars = None
        ### Parse the content type ###
        self.requesttype = request.lower().split('content-type: ')[1].split('\r\n')[0]
        ### Parse the content length ###
        self.requestlength = request.lower().split('content-length: ')[1].split('\r\n')[0]
        ### Parse the cookie parameter, if any ###
        try:
            self.cookie = request.split('Cookie: ')[1].split('\r\n')[0]
        except:
            self.cookie = None
        
    def getReqPage(self):
        return self.page
    
    def getConnType(self):
        return self.conntype
    
    def getProto(self):
        return self.postproto
    
    def getHost(self):
        return self.host
    
    def getCookie(self):
        if self.cookie is not None:
            return self.cookie
        else:
            return ''
    
    def getVars(self):
        if self.requestvars is not None:
            return self.requestvars
        else:
            return ''
        
    def getContentType(self):
        return self.requesttype
    
    def getContentLength(self):
        return self.requestlength