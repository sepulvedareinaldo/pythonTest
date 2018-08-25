'''
Created on Jul 4, 2018

@author: rsepulveda3
'''
from serial import Serial
import time
class MeasurementDevice:
    def __init__(self, ser):
        self.ser = ser
        self.idn = None

    def get_identifier(self):
        print(self.ser.read())

foo = Serial('COM3', baudrate=115200, timeout=0.5)
#my_device = MeasurementDevice(foo)

count=0
while True:
    now=time.clock()
    print(foo.read())
    print(1000*(now-time.clock()))
    print()
