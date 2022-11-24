from PIL import Image, ImageDraw, ImageFont
import time
import random
from colorsys import hsv_to_rgb
from Character import Froggy
from Joystick import Joystick
from Car import Car
import numpy as np

class ObjectManager:
    def __init__(self):
        self.cars = []
        self.logs = []



    def updatObjects(self):
        car = Car(-7, [240, 160])
        self.cars.append(car)

    # 자동차, 통나무 객체들을 움직이는 함수
    def moveObjects(self):
        for car in self.cars:
            if(car.outOfRange(240)):        # 차가 밖으로 나갔는지 체크
                print("out!")
                self.cars.remove(car)
            else:                           # 아닌 경우 차를 이동시킨다
                car.move()


    # 자동차, 강과 충돌이 일어났는 지 확인하는 함수
    def collision_check(self, froggyPos):
        for car in self.cars:
            if(car.collision_check(froggyPos)):
                return True
        return False