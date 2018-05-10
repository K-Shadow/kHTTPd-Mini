'''
                kHTTPd Mini Debug Log
Logs data such as raw data received from the client
'''

class LogDebug:
    
    def __init__(self, logger, index):
        self.log = logger
        self.index = index
    
    def output(self, data, address):
        data = data.strip('\r\n')
        if data.find('GET /') != -1:
            self.parseGet(data)
        elif data.find('POST /') != -1:
            self.parsePost(data)
        else:
            self.log.output('Data received from client '+ address +': '+ data)
        
    def parseGet(self, request):
        if request.find('GET /') != -1:
            ### Parse host from the request ###
            requesthost = request.split('Host: ')[1].split('\r\n')[0]
            ### Get page from the GET request ###
            requestinfo = request.split(' HTTP/1.1')[0].split('GET ')[1]
            if requestinfo.find('?') != -1:
                requestinfo = requestinfo.split('?')[0]
            if requestinfo == '/':
                requestinfo = '/'+ self.index
            ### Try to find any variables in the request ###
            try:
                requestvars = request.split('?', 1)[1].split(' HTTP/1.1')[0]
            except:
                requestvars = None
            ### Parse the protocol version ###
            requestprotocol = request.split(' HTTP/')[1].split('\r\n')[0]
            ### Parse the connection type ###
            requestconn = request.split('Connection: ')[1].split('\r\n')[0]
            ### Parse the cookie parameter, if any ###
            try:
                requestcookie = request.split('Cookie: ')[1].split('\r\n')[0]
            except:
                requestcookie = None
            ### Print all of the data! ###
            self.log.output('Page request: '+ requestinfo)
            self.log.output('Host: '+ requesthost)
            self.log.output('Protocol: '+requestprotocol)
            self.log.output('Request conn. type: '+requestconn)
            if requestcookie is not None:
                self.log.output('Cookies: '+requestcookie)
            if requestvars is not None:
                self.log.output('Request variables: '+requestvars)
                
    def parsePost(self, request):
        if request.find('POST /') != -1:
            ### Parse host from the request ###
            requesthost = request.split('Host: ')[1].split('\r\n')[0]
            ### Get page from the POST request ###
            requestinfo = request.split(' HTTP/1.1')[0].split('POST ')[1]
            if requestinfo == '/':
                requestinfo = '/'+ self.index
            ### Parse the protocol version ###
            requestprotocol = request.split(' HTTP/')[1].split('\r\n')[0]
            ### Parse the connection type ###
            requestconn = request.split('Connection: ')[1].split('\r\n')[0]
            ### Parse the content type ###
            requesttype = request.split('Content-type: ')[1].split('\r\n')[0]
            ### Parse the content length ###
            requestlength = request.split('Content-length: ')[1].split('\r\n')[0]
            ### Parse the variables if any ###
            try:
                requestvars = request.split('\r\n\r\n', 1)[1]
            except:
                requestvars = None
            ### Parse the cookie parameter, if any ###
            try:
                requestcookie = request.split('Cookie: ')[1].split('\r\n')[0]
            except:
                requestcookie = None
            ### Print all of the data! ###
            self.log.output('Page request: '+ requestinfo)
            self.log.output('Host: '+ requesthost)
            self.log.output('Protocol: '+requestprotocol)
            self.log.output('Request conn. type: '+requestconn)
            self.log.output('Content type: '+requesttype)
            self.log.output('Content length: '+requestlength)
            if requestcookie is not None:
                self.log.output('Cookies: '+requestcookie)
            if requestvars is not None:
                self.log.output('Variables: '+requestvars)