import numpy as np
from PIL import Image

class Snake:
    def __init__(self, height):
        self.direction = "right"
        self.position = np.array([0, height])
        self.speed = 2

    def move(self): # Snake 객체를 움직여 주는 함수, 방향에 따라 speed를 양수, 음수로 바꾸어준다.
        if self.position[0] >= 224:
            self.speed = -self.speed
            self.direction = "left"
        elif self.position[0] <= 0 and self.direction == "left":
            self.speed = -self.speed
            self.direction = "right"
        self.position[0] += self.speed

    def reset_snake(self):        # Snake 객체 초기화 해주는 함수
        self.direction = "right"
        self.position[0] = 0
        self.speed = abs(self.speed)


    def transfer_check(self):   # Snake의 방향에 따라 그림을 좌우 반전시켜야 하는지 알려주는 함수
        if self.direction == 'right':
            return 1  # 좌우 반전 시켜야 하므로 1 반환
        else:
            return 0

    def collision_check(self, frogger_position):     # frogger와 Snake간 충돌 확인하는 함수
        if self.position[1] == frogger_position[1]: # 먼저 y 좌표 확인하고 x 좌표 비교
            if self.position[0] <= frogger_position[0] + 8 <= self.position[0] + 16:
                return True
        return False


