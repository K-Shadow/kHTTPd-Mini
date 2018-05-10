'''
                kHTTPd Get Request Parser
Used to get information from a get request, such as the requested page.
'''

class parseGet:
    
    def __init__(self, docroot, index, request):
        self.docroot = docroot
        ### Parse host from the request ###
        self.host = request.split('Host: ')[1].split('\r\n')[0]
        ### Get page from the GET request ###
        self.page = request.split(' HTTP/1.1')[0].split('GET ')[1]
        if self.page.find('?') != -1:
            self.page = self.page.split('?')[0]
        ### Parse full URI ###
        self.uri = request.split(' HTTP/1.1')[0].split('GET /')[1]  
        ### Parse the protocol version ###
        self.getproto = request.split(' HTTP/')[1].split('\r\n')[0]
        ### Parse the connection type ###
        self.conntype = request.split('Connection: ')[1].split('\r\n')[0]
        ### Parse the variables ###
        try:
            self.requestvars = request.split('?', 1)[1].split(' HTTP/1.1')[0]
        except:
            self.requestvars = None
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
        return self.getproto
    
    def getHost(self):
        return self.host
    
    def getUri(self):
        return self.uri
    
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