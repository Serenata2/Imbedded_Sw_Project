import numpy as np

class Froggy:
    def __init__(self, width, height):
        self.state = "up_pressed"
        self.position = np.array([16, 16])
        self.life = 5
        self.count = 0
        self.outline = "#FFFFFF"
        self.moving = False

    def move(self, command = None):
        if command == None:
            self.outline = "#FFFFFF" #검정색상 코드!
            if(self.moving):
                print("motion!")
                self.motion()

        else:
            if(not self.moving):
                self.state = command
                self.moving = True
                self.count = 0
                self.outline = "#FF0000" #빨강색상 코드!

    def motion(self):
        
        if self.state == 'up_pressed':
            if(self.position[1] <= 0):
                self.moving = False
            else:
                self.position[1] -= 8

        elif self.state == 'down_pressed':
            if(self.position[1] >= 208):
                self.moving = False
            else:
                self.position[1] += 8

        elif self.state == 'left_pressed':
            if(self.position[0] <= 0):
                self.moving = False
            else:
                self.position[0] -= 8
                
        elif self.state == 'right_pressed':
            if(self.position[0] >= 224):
                self.moving = False
            else:
                self.position[0] += 8
        self.count += 1
        if(self.count >= 2):
            self.moving = False

    def rotateAngle(self):
        if self.state == 'up_pressed':
            return 0

        elif self.state == 'down_pressed':
            return 180

        elif self.state == 'left_pressed':
            return 90
                
        elif self.state == 'right_pressed':
            return 270
        else:
            return 0
    
    def edgeTest(self):
        a = self.position[0] < 224 and self.position[1] < 208
        print(a)
        return a