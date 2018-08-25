'''
Created on Jul 1, 2018

@author: rsepulveda3
'''

from time import sleep
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.web import Application, asynchronous, RequestHandler
from multiprocessing.pool import ThreadPool
import tornado.web
_workers = ThreadPool(10)

###
import time
from serial import Serial

from tornado.concurrent import run_on_executor
from concurrent.futures import ThreadPoolExecutor   # `pip install futures` for python2

from serial import Serial

MAX_WORKERS = 4




starter=[]
class Handler(tornado.web.RequestHandler):
    executor = ThreadPoolExecutor(max_workers=MAX_WORKERS)
    
    @run_on_executor
    def initialization_time(self):
        """ This will be executed in `executor` pool. """
        i=3
        print('in blocking')
        time.sleep(1)
        print('sent form blocking ')
        return i
    
    
    @tornado.gen.coroutine
    def get(self):
        """ Request that asynchronously calls background task. """
        self.render("index.html")
        
        res = yield self.initialization_time() #necesary timeout for initializatoin
        #ress= yield self.read_forever()
        #FirstSocketHandler.send_message(handlers[0],'from Handler')
        print('back in get')
    '''
    @tornado.gen.coroutine
    def read_forever(self):
        i=0
        while True:
            i+=1
            #print('in forever ', i)
            res = yield self.fut_ard()
            FirstSocketHandler.write_message(handlers[0],res)
            #FirstSocketHandler.send_message(handlers[0],'{}'.format(i))
            print('wrote to socket ', res)
            #print('left forever ', i)
            
    
    @run_on_executor
    def fut_ard(self):
        #print('in fut_ard')
        #time.sleep(2)
        res = ards.read()
        return res
     '''   
###
import tornado.websocket
handlers=[]

class FirstSocketHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        handlers.append(self)
        #print('handler1 ',handlers)
        print ("First Websocket Opened")
        self.write_message("First Socket Handler")

    def on_message(self, message):
        print('received',message)
        #self.write_message("You said: %s" % message)

    def on_close(self):
        print ("First Websocket closed")
    
    def send_message(self, mess):
        self.write_message(mess)
        #print("First after",mess)

class crossTalk(tornado.websocket.WebSocketHandler):
    def open(self):
        print ("3 Opened")
    
    def on_message(self, message):
        print('receiving cross talk (maybe non blocking)')
        #SecondSocketHandler.send_message('__main__'.SecondSocketHandler, 'second')
    
    def on_close(self):
        print ("3 Websocket closed")

ards = Serial("COM3", 115200, timeout=10)

HTTPServer(Application([("/", Handler),
                        (r"/ws1", FirstSocketHandler),
                        (r"/ws3", crossTalk),],debug=True)).listen(8888)
IOLoop.instance().start()
    
    