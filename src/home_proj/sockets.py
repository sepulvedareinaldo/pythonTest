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
from concurrent.futures import ThreadPoolExecutor
from serial import Serial


handlers=[]
MAX_WORKERS=4
executor = ThreadPoolExecutor(max_workers=MAX_WORKERS)




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

class SecondSocketHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        handlers.append(self)
        #print('handler2 ',handlers)
        print ("Second Websocket Opened")
        self.write_message("Second Socket Handler")
        self.send_message('2')

    def on_message(self, message):
        print('message on Second Socket is *** ',message)
        #FirstSocketHandler.send_message(self,'from second')
        #self.write_message("You said: %s" % message)

    def on_close(self):
        executor=[]
        print ("Second Websocket closed")
    
    def send_message(self, mess):
        sema="SENT AFTER ALL {}".format(mess)
        self.write_message(sema)
        print('SENT AFTER ALL',mess)




class IndexHandler(tornado.web.RequestHandler):
    
    async def initialization_time(self,time):
        #tornado.ioloop.IOLoop.run_in_executor()
        res = await loop.run_in_executor(executor, self.timer)
        #await asyncio.sleep(time)
        return 'done'
    
    def timer(self):
        time.sleep(1)
        return 'dine'
    
    async def async_ard_reader(self):
        message =''
        while True:
            arduino_val = await loop.run_in_executor(executor, self.read_ard)
            if arduino_val.decode("utf-8") != '\n':
                message+=arduino_val.decode("utf-8") 
            else:
                print(message)
                message=''
            
            
    def read_ard(self):
        arduino_val = ards.read()
        return arduino_val
    
    async def get(self):
        self.render("index.html")
        await self.initialization_time(1)
        await self.async_ard_reader()

class crossTalk(tornado.websocket.WebSocketHandler):
    def open(self):
        print ("3 Opened")
    
    def on_message(self, message):
        FirstSocketHandler.write_message(handlers[0], 'ffiirrsstt')
        print(handlers)
        #SecondSocketHandler.send_message('__main__'.SecondSocketHandler, 'second')
    
    def on_close(self):
        executor=[]
        print ("3 Websocket closed")


application = tornado.web.Application([
    (r'/', IndexHandler),
    (r"/ws1", FirstSocketHandler),
    (r"/ws2", SecondSocketHandler),
    (r"/ws3", crossTalk),
    ])

if __name__ == "__main__":
    
    
    port=8888
    application.listen(port)
    myIP = socket.gethostbyname(socket.gethostname())
    print ('*** Websocket Server Started at {}:{}***'.format(myIP, port))
    ards = Serial("COM3", 9600, timeout=10)
    print("connected to Arduino")
    
    loop = asyncio.get_event_loop()
    #loop.run_forever()
    tornado.ioloop.IOLoop.instance().start()

    
    
    
    
    
    