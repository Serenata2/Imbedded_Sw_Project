from PIL import Image, ImageDraw, ImageFont
import time
import random
from colorsys import hsv_to_rgb
from Character import Froggy
from Joystick import Joystick
from Car import Car
from Road import Road
from ObjectPool import ObjectPool
import numpy as np

class ObjectManager:
    def __init__(self):
        self.obejectPool = ObjectPool()
        self.roadList = []
        for i in range(5):
            print("road is made")
            self.roadList.append(Road((192 - (16*i)), random.randint(3,10), 4))



    def updatObjects(self):
        for road in self.roadList:
            if(road.isFit()):   # 만약에 확률을 만족한다면 큐에서 car 객체를 빼고 추가
                print("car is maded!")
                road.add(self.obejectPool.post_car())        

    # 자동차, 통나무 객체들을 움직이는 함수
    def moveObjects(self):
        for road in self.roadList:
            road.moveObject()
        for road in self.roadList:
            i = road.outOfRange()
            if(i != -1):
                print("return car~")
                self.obejectPool.return_car(road.returnCar(i))



    # 자동차, 강과 충돌이 일어났는 지 확인하는 함수
    def collision_check(self, froggyPos):
        for road in self.roadList:
            if(road.collision_check(froggyPos)):
                return True
        return False
