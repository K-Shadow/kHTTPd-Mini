'''
                kHTTPd Mini FIle Type Handler
Uses Python's mimetypes module to return the mimetype of a file
'''

from mimetypes import guess_type

class MimeHandler:
    
    def __init__(self):
        pass
    
    def getType(self, filename):
        try:
            if guess_type(filename)[0] == None:
                ### TODO: Add more mimetypes ###
                return 'text/html'
            else:
                return guess_type(filename)[0]
        except:
            return 'text/html'