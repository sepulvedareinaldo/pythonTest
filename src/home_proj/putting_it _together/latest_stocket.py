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

class FirstSocketHandler(tornado.websocket.WebSocketHandler):
    
    async def open(self):
        hands.append(self)
        #print('handler1 ',handlers)
        print ("First Websocket Opened")
        self.write_message("First Socket Handler")
        print ('First message sent: First Socket Handler')
        await self.out_message_in()

    def on_message(self, message):
        print('message on First Socket is *** ',message)
        #self.write_message("You said: %s" % message)

    def on_close(self):
        hands.remove(self)
        print ("First Websocket closed")
    
    def send_message(self, mess):
        self.write_message("First after",mess)
        print("First after",mess)
    
    async def out_message_in(self):
        #message =''
        global world_message
        old_value=''
        
        #print('world message ',world_message)
        #print('handlers in out_message_in ', handlers)
        while True:
            #print('in while out message in ',world_message)
            #print('handlers in out_message_in ', handlers)
            #print('print self', self)
            value = await loop.run_in_executor(executor, self.read_out_message, old_value)
            old_value = value
            if value!='':
                print('message from ',hands)
                print('message', value)
                
                
                for i, H in enumerate(hands):
                    H.write_message('your in {}'.format(i+1))
                    H.write_message('arduino is')
                    H.write_message(value)
            
            if self not in hands :
                break
    
    def read_out_message(self, old_value):
        global world_message
        while True:
            if world_message!=old_value:
                old_value = world_message
                break
        #arduino_val = ards.read()
        return old_value

class SecondSocketHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        #handlers.append(self)
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
        #res = await loop.run_in_executor(executor, self.timer)
        #await asyncio.sleep(time)
        return 'done'
    
    def timer(self):
        time.sleep(1)
        return 'time'
        
    async def get(self):
        #handlers.append(self)
        print('started index handle ', handlers)
        self.render("index.html")
        #await self.initialization_time(1)
        #await self.out_message_in()

class crossTalk(tornado.websocket.WebSocketHandler):
    def open(self):
        print ("3 Opened")
    
    def on_message(self, message):
        #FirstSocketHandler.write_message(handlers[0], 'ffiirrsstt')
        print('received from ws3')
        #SecondSocketHandler.send_message('__main__'.SecondSocketHandler, 'second')
    
    def on_close(self):
        #executor=[]
        print ("3 Websocket closed")


application = tornado.web.Application([
    (r'/', IndexHandler),
    (r"/ws1", FirstSocketHandler),
    (r"/ws2", SecondSocketHandler),
    (r"/ws3", crossTalk),
    ])









async def read_forever():
    i=0
    while True:
        i+=1
        print('in forever ', i)
        ress = await fut_ard()
        print(ress)
        return

async def fut_ard():
    #executor = concurrent.futures.ThreadPoolExecutor(max_workers=2)
    message=''
    #print('in fut_ard')
    #res = await loop.run_in_executor(executor, get_byte)
    while True:
        #print('in fut_ard')
        arduino_val = await loop.run_in_executor(executor, get_byte)
        #print(arduino_val)
        
        if (arduino_val.decode("utf-8") != '\r') and (arduino_val.decode("utf-8") !='\n'):
            message+=arduino_val.decode("utf-8") 
        else:
            
            global world_message
            world_message = message
            #print(world_message)
            message=''
    #return print(res)

def get_byte():
    arduino_val = ards.read()
    return arduino_val


if __name__ == "__main__":
    
    
    port=8888
    application.listen(port)
    myIP = socket.gethostbyname(socket.gethostname())
    print ('*** Websocket Server Started at {}:{}***'.format(myIP, port))
    ###
    ards = Serial("COM4", 9600, timeout=10)
    print("connected to Arduino")
    ###
    loop = asyncio.get_event_loop()
    reader = asyncio.ensure_future(fut_ard())
    loop.run_forever()
    #tornado.ioloop.IOLoop.instance().start()

    
    
    
    
    
    