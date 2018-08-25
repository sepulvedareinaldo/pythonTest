'''
Created on Jul 4, 2018

@author: rsepulveda3
'''

import asyncio
import concurrent

from serial import Serial


import time
from concurrent.futures import ProcessPoolExecutor


# Normal serial blocking reads
# This could also do any processing required on the data
def get_byte():
    return s.read()
# Runs blocking function in executor, yielding the result
async def get_byte_async():
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        res = await loop.run_in_executor(executor, get_byte)
        return res
async def get_and_print():
    while True:
        b = await get_byte_async()
        print (b)


async def get_boo():
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        res = await loop.run_in_executor(executor, say_boo)
        return res
async def get_and_boo():
    while True:
        b = await get_boo()
        print (b)
def say_boo():
    i = 0
    while True:
        print('...boo {0}'.format(i))
        time.sleep(0.5)
        i += 1




s = Serial("COM3", 115200, timeout=10)
loop = asyncio.get_event_loop()
#loop.run_until_complete(get_and_print())
'''
while True:
    loop.run_until_complete(get_and_print())
'''

#executor = ProcessPoolExecutor(3)
#boo = asyncio.ensure_future(loop.run_in_executor(executor, say_boo))


reader = asyncio.ensure_future(get_and_print())
boo = asyncio.ensure_future(get_and_boo())
loop.run_forever()
