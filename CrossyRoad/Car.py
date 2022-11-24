import numpy as np

class Car:
    def __init__(self, speed, position):
        self.direction = "up_pressed"
        self.position = np.array([position[0], position[1]])
        self.width = 16     # 나중에 상속
        self.speed = speed

    def move(self):
        self.position[0] += self.speed

    def collision_check(self, froggy_position):
        if( froggy_position[1] - 8 <= self.position[1] <= froggy_position[1] + 8):
                if( self.position[0] <= froggy_position[0] + 8 <= self.position[0] +  self.width):
                    print("collision!!!")
                    return True
        return False

    def outOfRange(self, width):
        if(self.position[0] + self.width < 0 or self.position[0] > width+1):
            return True
        return False
    