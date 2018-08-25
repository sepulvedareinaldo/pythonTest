'''
Created on Jul 1, 2018

@author: rsepulveda3
'''
import tornado.websocket
import tornado.ioloop
import tornado.web
import socket
import time
import asyncio
import concurrent
#from concurrent.futures import ThreadPoolExecutor
from serial import Serial
import concurrent.futures 

handlers=[]
world_message =''
world_value=''
MAX_WORKERS=4
executor = concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS)


hands=[]



class SocketHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print ("Websocket Opened")
        self.write_message("Socket Handler")

    def on_message(self, message):
        print('message on Socket is *** ',message)
        #FirstSocketHandler.send_message(self,'from second')
        #self.write_message("You said: %s" % message)

    def on_close(self):
        print (" Websocket closed")




class IndexHandler(tornado.web.RequestHandler):
    
    async def initialization_time(self,time):
        #tornado.ioloop.IOLoop.run_in_executor()
        #res = await loop.run_in_executor(executor, self.timer)
        #await asyncio.sleep(time)
        return 'done'
    
    def timer(self):
        time.sleep(1)
        return 'time'
        
    async def get(self):
        #handlers.append(self)
        print('started index handle ', handlers)
        self.render("rpi_index.html")
        #await self.initialization_time(1)
        #await self.out_message_in()


application = tornado.web.Application([
    (r'/', IndexHandler),
    (r"/ws", SocketHandler),
    ])


if __name__ == "__main__":
    
    
    port=8888
    application.listen(port)
    myIP = socket.gethostbyname(socket.gethostname())
    print ('*** Websocket Server Started at {}:{}***'.format(myIP, port))
    ###
    loop = asyncio.get_event_loop()
    loop.run_forever()
    #tornado.ioloop.IOLoop.instance().start()

    
    
    
    
    
    