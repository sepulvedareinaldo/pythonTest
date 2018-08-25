'''
Created on Jul 4, 2018

@author: rsepulveda3
'''

import asyncio
import concurrent

from serial import Serial

# Normal serial blocking reads
# This could also do any processing required on the data
def get_byte():
    return s.read()

# Runs blocking function in executor, yielding the result

async def get_byte_async():
    with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
        res = await loop.run_in_executor(executor, get_byte)
        return res

async def get_and_print():
    while True:
        b = await get_byte_async()
        print (b)

s = Serial("COM3", 115200, timeout=10)
loop = asyncio.get_event_loop()
#loop.run_until_complete(get_and_print())
'''
while True:
    loop.run_until_complete(get_and_print())
'''
reader = asyncio.ensure_future(get_and_print())
loop.run_forever()
