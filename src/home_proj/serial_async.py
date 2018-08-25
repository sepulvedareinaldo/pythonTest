import asyncio
from concurrent.futures import ProcessPoolExecutor
import time

from serial import Serial

print('running async test')




def say_boo():
    i = 0
    while True:
        print('...boo {0}'.format(i))
        time.sleep(1.5)
        i += 1


if __name__ == "__main__":
    executor = ProcessPoolExecutor(3)
    
    print('out read ', foo.read())
       
    loop = asyncio.get_event_loop()
    boo = asyncio.ensure_future(loop.run_in_executor(executor, say_boo))
    #baa = asyncio.ensure_future(loop.run_in_executor(executor, say_baa))
    
    
    
    loop.run_forever()