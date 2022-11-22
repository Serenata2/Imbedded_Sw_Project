import numpy as np

class Car:
    def __init__(self):
        self.direction = "up_pressed"
        self.position = np.array([0, 176])
        self.width = 16
        self.count = 0
        self.outline = "#FFFFFF"
        self.speed = 5

    def move(self):
        self.position[0] += self.speed

    def collision_check(self, froggy_position):
        if( froggy_position[1] - 8 <= self.position[1] <= froggy_position[1] + 8):
                if( self.position[0] <= froggy_position[0] + 8 <= self.position[0] +  self.width):
                    print("collision!!!")
                    return True
        return False

    def outOfRange(self, width):
        if(self.position[0] + self.width < 0 or self.position[0] > width):
            return True
        return False
    