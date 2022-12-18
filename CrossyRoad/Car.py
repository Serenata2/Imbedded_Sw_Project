import numpy as np

class Car:
    def __init__(self):
        self.position = [0,0]
        self.width = 0
        self.speed = 0

    def set_car(self, speed, position, width):
        self.speed = speed
        self.position = position.copy()
        self.width = width

        
    def move(self):
        self.position[0] += self.speed

    def collision_check(self, frogger_position):
        if( frogger_position[1] - 8 <= self.position[1] <= frogger_position[1] + 8):
                if( self.position[0] <= frogger_position[0] + 8 <= self.position[0] +  self.width):
                    return True
        return False

    def out_of_range(self, width):
        if(self.position[0] + self.width < 0 or self.position[0] > width+1):
            return True
        return False
    