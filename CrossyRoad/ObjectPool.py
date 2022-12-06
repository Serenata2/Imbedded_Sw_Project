from PIL import Image, ImageDraw, ImageFont
import time
import random
from colorsys import hsv_to_rgb
from Character import Froggy
from Joystick import Joystick
from Car import Car
from Road import Road
from Log import Log
import numpy as np

class ObjectPool:
    def __init__(self):
        self.storage_car = [Car() for _ in range(15)]
        self.storage_log = [Log() for _ in range(15)]

    def creat_car(self):
        print("car object is created~~~~~~~~~~~~")
        for i in range(5):
            self.storage_car.append(Car())
        
    def post_car(self):
        if(len(self.storage_car) <= 0):
            self.creat_car()
        return self.storage_car.pop(0)
    
    def return_car(self, car):
        self.storage_car.append(car)

    def creat_log(self):
        print("log object is created~~~~~~~~~~~~~~~~~")
        for i in range(5):
            self.storage_log.append(Log())
        
    def post_log(self):
        if(len(self.storage_log) <= 0):
            self.creat_log()
        return self.storage_log.pop(0)
    
    def return_log(self, log):
        self.storage_log.append(log)


