from PIL import Image, ImageDraw, ImageFont
import time
import random
from colorsys import hsv_to_rgb
from Character import Froggy
from Joystick import Joystick
from Car import Car
from Road import Road
import numpy as np

class ObjectPool:
    def __init__(self):
        self.storage_car = [Car() for _ in range(20)]

    def creat_car(self):
        for i in range(5):
            self.storage_car.append(Car())
        
    def post_car(self):
        if(len(self.storage_car) <= 0):
            self.creat_car()
        return self.storage_car.pop(0)
    
    def return_car(self, car):
        self.storage_car.append(car)


