import numpy as np

class Frogger:
    def __init__(self, width, height):
        self.state = "up_pressed"
        self.position = np.array([int(width/2) - 16, height-32])    # 시작 위치 초기화
        self.life = 5       # 생명력
        self.count = 0      # 완전히 점프를 뛰었는지 체크하는 변수
        self.moving = False # 움직이는 여부를 체크하는 변수

    def move(self, command = None):     # command와 self.moving을 통해 적절히 motion함수 사용
        if command == None:
            if(self.moving):
                self.motion()

        else:
            if(not self.moving):
                self.state = command
                self.moving = True
                self.count = 0

    def motion(self):                   # frogger의 state와 position에 따라 움직여준다.
        if self.state == 'up_pressed':  # 움직이기 전에 화면을 벗어나려는지 확인해 준다.
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

    def rotate_angle(self):              # frogger가 회전한 각도 출력해주는 함수
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

    def condition(self):                # 움직이는 동작을 알려주는 함수
        if(self.moving and self.count == 0):    # 점프 준비 동작
            return 2
        elif(self.moving):                      # 점프 중인 동작
            return 1
        else:                                   # 평상시 동작
            return 0    

    def died(self):                     # frogger가 죽은 경우 호출되는 함수
        self.position = np.array([int(240/2) - 16, 240-32])
        self.life -= 1
        self.moving = False

    def succed(self):                   # frogger가 목표지점에 도착한 경우 호출되는 함수
        self.position = np.array([int(240/2) - 16, 240-32])
        self.moving = False
