'''
Created on Jul 4, 2018

@author: rsepulveda3
'''
#import tornado.platform.asyncio
import tornado.websocket
import tornado.ioloop
import tornado.web
import socket
import time
import asyncio
from Cython.Compiler.Errors import message


handlers=[] #this lists clients tha connect to the socket. needed for defining "self" in websocket handlers



class FirstSocketHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        handlers.append(self)
        #print('handler1 ',handlers)
        print ("First Websocket Opened")
        self.write_message("First Socket Handler")
        print ('First message sent: First Socket Handler')

    def on_message(self, message):
        print('message on First Socket is *** ',message)
        #self.write_message("You said: %s" % message)

    def on_close(self):
        print ("First Websocket closed")
    
    def send_message(self, mess):
        self.write_message("First after",mess)
        print("First after",mess)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")


    
class httpAsyncIOHandler(tornado.web.RequestHandler):
    async def get(self):
        self.write("Hello world!\n")
        print("Hej!")
        self.render("index.html")
        await asyncio.sleep(2)
        print("slept for 2s!")
        await writer('hi')
        #await AsyncIOHandler.writer('hi')
        
'''
class AsyncIOHandler(tornado.web.RequestHandler):
    async def writer(self , message):
        print(message)
'''

async def writer(message):
    print('in writer ' , message)
    await asyncio.sleep(2)
    print('writer 2s later')
    
application = tornado.web.Application([
    (r"/ws1", FirstSocketHandler),
    (r'/',httpAsyncIOHandler),
    #(r'/a', IndexHandler),
    ])

if __name__ == "__main__":
    
    port=8888
    
    
    '''
    #run through tornado event loop
    application.listen(port)
    myIP = socket.gethostbyname(socket.gethostname())
    print ('*** Websocket Server Started at {}:{}***'.format(myIP, port))
    tornado.ioloop.IOLoop.instance().start()
    '''
    
    #run through asyncio event loop
    #tornado.platform.asyncio.AsyncIOMainLoop().install()
    application.listen(port)
    myIP = socket.gethostbyname(socket.gethostname())
    print ('*** Websocket Server Started at {}:{}***'.format(myIP, port))
    asyncio.get_event_loop().run_forever()
    
    
    
    
    
    