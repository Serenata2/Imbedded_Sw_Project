from PIL import Image, ImageDraw, ImageFont
import time
import random
from colorsys import hsv_to_rgb
from Character import Froggy
from Joystick import Joystick

class Road:
    def __init__(self, y_position, speed, frequency):
        self.speed = speed  # 양수이면 오른쪽 방향, 음수이면 왼쪽 방향
        self.frequency = frequency
        self.position = [-16, y_position]
        self.carList = []

    def add(self, car):
        print("road speed: {}, road position : {}".format(self.speed, self.position))
        car.setCar(self.speed, self.position)
        self.carList.append(car)

    def isFit(self):
        if(random.randint(1,100) < self.frequency):
            return True
        return False

    def returnCar(self, index):
        return self.carList.pop(index)
    
    def outOfRange(self):
        for i in range(len(self.carList)):
            if(self.carList[i].outOfRange(240)):
                return i    # out of Range
        return -1           # 범위를 벗어난 차는 없다.

    def moveObject(self):
        for car in self.carList:
            car.move()

    def collision_check(self, froggyPosition):
        for car in self.carList:
            if(car.collision_check(froggyPosition)):
                return True
        return False
