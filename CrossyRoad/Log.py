import numpy as np

class Log:
    def __init__(self):
        self.position = [0,0]
        self.width = 64     # 나중에 상속
        self.speed = 0

    def setLog(self, speed, position):
        self.speed = speed
        self.position = position.copy()

    def move(self):
        self.position[0] += self.speed

    def outOfRange(self, width):
        if(self.position[0] + self.width < 0 or self.position[0] > width+1):
            return True
        return False

    def on_board_check(self, froggy_x_position):
        if( self.position[0] <= froggy_x_position + 8 <= (self.position[0] + self.width)):
            return True
        print("river collision!!!")
        return False