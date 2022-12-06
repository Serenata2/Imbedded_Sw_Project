from PIL import Image, ImageDraw, ImageFont
import time
import random
from colorsys import hsv_to_rgb
from Character import Froggy
from Joystick import Joystick
from Car import Car

from ObjectManager import ObjectManager

class GameManager:
        def __init__(self):
            self.joystick = Joystick()
            self.froggy = Froggy(self.joystick.width, self.joystick.height)
            self.objectManager = ObjectManager()
            self.command = None
            self.myImage = Image.open(r"/home/kau-esw/esw/gitHub/ImbeddedSwProject/CrossyRoad/image/New Piskel.png")
            self.flag = 0
            self.successList = [0 for _ in range(3)]
            self.firstImage = Image.open(r"/home/kau-esw/esw/gitHub/ImbeddedSwProject/CrossyRoad/image/New Piskel.png")
            self.lifeImage = Image.open(r"/home/kau-esw/esw/gitHub/ImbeddedSwProject/CrossyRoad/image/life.png")
            self.froggyImageList = []
            for i in range(1,4):
                self.froggyImageList.append(Image.open(r"/home/kau-esw/esw/gitHub/ImbeddedSwProject/CrossyRoad/image/frogup"+str(i)+".png"))
            self.backgroundList = []
            for i in range(1,3):
                self.backgroundList.append(Image.open(r"/home/kau-esw/esw/gitHub/ImbeddedSwProject/CrossyRoad/image/background"+str(i)+".png"))
            self.logImage = Image.open(r"/home/kau-esw/esw/gitHub/ImbeddedSwProject/CrossyRoad/image/log.png")
            self.counter = 0
            

        def endConditionCheck(self):
            if(self.froggy.life <= 0):
                return True
            for i in self.successList:
                if(not i):
                    return False
            return True

        def inputData(self):
            self.command = None
            if not self.joystick.button_U.value:  # up pressed
                self.command = 'up_pressed'

            elif not self.joystick.button_D.value:  # down pressed
                self.command = 'down_pressed'

            elif not self.joystick.button_L.value:  # left pressed
                self.command = 'left_pressed'

            elif not self.joystick.button_R.value:  # right pressed
                self.command = 'right_pressed'
        
            elif not self.joystick.button_A.value: # A pressed
                self.command = 'up_pressed'

            else:
                self.command = None

            
            
        def moveObjects(self):
            self.froggy.move(self.command)
            self.counter = (self.counter % 1000)
            self.objectManager.updatObjects(self.counter)
            self.counter += 1
            self.objectManager.moveObjects(self.froggy)
            if(self.objectManager.collision_check(self.froggy.position)):
                self.froggy.died()
            elif(self.froggy.position[1] == 0):
                if(self.froggy.position[0] + 8 <= 24):
                    self.successList[0] = True
                    self.froggy.succed()
                    self.objectManager.speed_up_objects()
                elif(108 <= self.froggy.position[0] + 8 <= 132):
                    self.successList[1] = True
                    self.froggy.succed()
                    self.objectManager.speed_up_objects()
                elif(self.froggy.position[0] + 8 >= 216):
                    self.successList[2] = True
                    self.froggy.succed()
                    self.objectManager.speed_up_objects()
                else:
                    self.froggy.died()
        

        def draw(self):
            self.myImage.paste(self.backgroundList[int((self.flag) % 8 / 4)]) 
            self.flag = (self.flag + 1) % 8

            for road in self.objectManager.roadList:
                for car in road.carList:
                    self.myImage.paste(self.froggyImageList[0], tuple(car.position), self.froggyImageList[0])
            
            for river in self.objectManager.riverList:
                for log in river.logList:
                    self.myImage.paste(self.logImage, tuple(log.position))

            angle = self.froggy.rotateAngle()
            i = self.froggy.condition()
            self.myImage.paste(self.froggyImageList[i].rotate(angle), tuple(self.froggy.position), self.froggyImageList[i].rotate(angle))

            for i in range(self.froggy.life):
                self.myImage.paste(self.lifeImage, tuple([i * 16, self.joystick.height - 16]), self.lifeImage)
            self.joystick.disp.image(self.myImage)

        def drawEnd(self):
            for i in range(240, -4, -4):
                self.myImage.paste(self.firstImage, tuple([i, 0]))
                self.joystick.disp.image(self.myImage)

