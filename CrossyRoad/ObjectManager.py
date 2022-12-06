import time
import random
from colorsys import hsv_to_rgb
from Character import Froggy
from Joystick import Joystick
from Car import Car
from Road import Road
from Log import Log
from River import River
from ObjectPool import ObjectPool
import numpy as np

class ObjectManager:
    def __init__(self):
        self.obejectPool = ObjectPool()
        self.roadList = []
        self.riverList = []
        for i in range(5):
            if(i%2 == 0):
                self.roadList.append(Road((192 - (16*i)), -4, random.randint(20,40)))
                self.riverList.append(River((96 - (16*i)), -random.randint(2,4), random.randint(50,70)))
            else:
                self.roadList.append(Road((192 - (16*i)), 8, random.randint(50, 70)))
                self.riverList.append(River((96 - (16*i)), random.randint(5,6), random.randint(30 ,40)))
        self.riverList.append(River(16, 2, 70))


    def updatObjects(self, counter):
        for road in self.roadList:
            if(road.isFit(counter)):   # 만약에 확률을 만족한다면 큐에서 car 객체를 빼고 추가
                road.add(self.obejectPool.post_car())        
        for river in self.riverList:
            if(river.isFit(counter)):
                river.add(self.obejectPool.post_log())


    # 자동차, 통나무 객체들을 움직이는 함수
    def moveObjects(self, froggy):
        for road in self.roadList:
            road.moveObject()
            i = road.outOfRange()
            if(i != -1):
                print("return car~")
                self.obejectPool.return_car(road.returnCar(i))

        for river in self.riverList:
            river.moveObject()
            if(froggy.position[1] == river.position[1]):
                froggy.position[0] += river.speed
            i = river.outOfRange()
            if(i != -1):
                print("return log")
                self.obejectPool.return_log(river.returnLog(i))


    # 자동차, 강과 충돌이 일어났는 지 확인하는 함수
    def collision_check(self, froggyPos):
        for road in self.roadList:
            if(road.collision_check(froggyPos)):
                return True
        for river in self.riverList:
            if(river.collision_check(froggyPos)):
                return True
        return False


    def speed_up_objects(self):
        for road in self.roadList:
            road.speed_up

        for river in self.riverList:
            river.speed_up