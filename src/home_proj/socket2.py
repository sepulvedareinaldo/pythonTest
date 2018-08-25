'''
Created on Jul 1, 2018

@author: rsepulveda3
'''
import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import socket
import _strptime
'''
This is a simple Websocket Echo server that uses the Tornado websocket handler.
Please run `pip install tornado` with python of version 2.7.9 or greater to install tornado.
This program will echo back the reverse of whatever it recieves.
Messages are output to the terminal for debuggin purposes. 
''' 
 
class WSHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print ('new connection')
        message='test'
        self.date_type_test(message)
      
    def on_message(self, message):
        print ('message received:  %s' % message)
        # Reverse Message and send it back
        print ('sending back message: %s' % message[::-1])
        
        #self.write_message(message[::-1])
        #self.date_type_test(message)
 
    def on_close(self):
        print ('connection closed')
 
    def check_origin(self, origin):
        return True
    
    def date_type_test(self, info):
        stri='string'
        print('sending string',stri)
        self.write_message(stri)
        '''
        inte=67
        print('sending integer',inte)
        self.write_message(inte)
        
        lst=[7,str]
        print('sending list',lst)
        self.write_message(lst)
        '''
        dct={'first':1,'second':2,'third':3}
        print('sending list',dct)
        self.write_message(dct)
        
 
class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("idex.html")
 
application = tornado.web.Application([
    (r'/', IndexHandler),
    (r'/ws', WSHandler),
])
 
 
if __name__ == "__main__":
    #http_server = tornado.httpserver.HTTPServer(application)
    #http_server.listen(8888)
    application.listen(8888)
    myIP = socket.gethostbyname(socket.gethostname())
    print ('*** Websocket Server Started at %s***' % myIP)
    tornado.ioloop.IOLoop.instance().start()