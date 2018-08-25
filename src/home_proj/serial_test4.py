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
def get_byte(pased):
    i=0
    while True:
        i+=1
        ards = s.read()
        print('ards', ards, i)
        break
    print('im out')
    return 'im out of get_byte %',ards
        #return ards
# Runs blocking function in executor, yielding the result

async def read_forever():
    i=0
    while True:
        i+=1
        await fut_ard()
        print('left forever ', i)
'''
async def get_byte_async():
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        res = await loop.run_in_executor(executor, get_byte)
        return res
async def get_and_print():
    while True:
        b = await get_byte_async()
        print (b)
'''
        
async def get_and_boo():
    while True:
        b = await get_boo()
        print (b)

async def get_boo():
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        res = await loop.run_in_executor(executor, say_boo)
        return res

def say_boo():
    i = 0
    while True:
        print('...boo {0}'.format(i))
        time.sleep(0.5)
        i += 1




s = Serial("COM4", 9600, timeout=10)
loop = asyncio.get_event_loop()
#loop.run_until_complete(get_and_print())
'''
while True:
    loop.run_until_complete(get_and_print())
'''
pa='passed'
#executor = ProcessPoolExecutor(3)
#boo = asyncio.ensure_future(loop.run_in_executor(executor, say_boo))
async def fut_ard():
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=2)
    res= await loop.run_in_executor(executor, get_byte, pa)
    return print(res)

reader = asyncio.ensure_future(read_forever())

#reader = asyncio.ensure_future(get_and_print())
boo = asyncio.ensure_future(get_and_boo())
loop.run_forever()
