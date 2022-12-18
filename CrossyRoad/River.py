class River:
    def __init__(self, y_position, speed, frequence, kind):
        self.kind = kind
        self.speed = speed  # 양수이면 오른쪽 방향, 음수이면 왼쪽 방향
        self.frequence = frequence
        if(speed < 0):
            self.position = [240, y_position]
        else:
            self.position = [-64, y_position]

        if kind == "long":
            self.width = 64
        else:
            self.width = 48
        self.log_list = []

    def add(self, log):         # 통나무를 초기화하고 리스트에 넣기
        log.set_log(self.speed, self.position, self.width)
        self.log_list.append(log)

    def is_fit(self, counter):
        if(counter % self.frequence == 0):
            return True
        return False

    def return_log(self, index):
        return self.log_list.pop(index)
    
    def out_of_range(self):
        for i in range(len(self.log_list)):
            if(self.log_list[i].out_of_range(240)):
                return i    # out of Range
        return -1           # 범위를 벗어난 차는 없다.

    def move_object(self):
        for log in self.log_list:
            log.move()

    def collision_check(self, froggyPosition):
        if(self.position[1] == froggyPosition[1]): # 먼저 y 좌표를 비교한다.
            for log in self.log_list:
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
        for log in self.log_list:
            log.speed = self.speed