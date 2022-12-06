import time
import random
from colorsys import hsv_to_rgb

class River:
    def __init__(self, y_position, speed, frequence):
        self.speed = speed  # 양수이면 오른쪽 방향, 음수이면 왼쪽 방향
        self.frequence = frequence
        if(speed < 0):
            self.position = [240, y_position]
        else:
            self.position = [-64, y_position]
        self.logList = []

    def add(self, log):
        log.setLog(self.speed, self.position)
        self.logList.append(log)

    def isFit(self, counter):
        if(counter % self.frequence == 0):
            return True
        return False

    def returnLog(self, index):
        return self.logList.pop(index)
    
    def outOfRange(self):
        for i in range(len(self.logList)):
            if(self.logList[i].outOfRange(240)):
                return i    # out of Range
        return -1           # 범위를 벗어난 차는 없다.

    def moveObject(self):
        for log in self.logList:
            log.move()

    def collision_check(self, froggyPosition):
        if(self.position[1] == froggyPosition[1]): # 먼저 y 좌표를 비교한다.
            for log in self.logList:
                if(log.on_board_check(froggyPosition[0])): # x 좌표를 비교한다.
                    return False
            return True
        else:
            return False

    def speed_up(self):
        if self.speed > 0:
            self.speed += 1
        else:
            self.speed -= 1