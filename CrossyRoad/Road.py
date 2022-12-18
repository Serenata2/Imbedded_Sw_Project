class Road:
    def __init__(self, y_position, speed, frequence, kind):
        self.kind = kind
        self.speed = speed  # 양수이면 오른쪽 방향, 음수이면 왼쪽 방향
        self.frequence = frequence
        if(speed < 0):
            self.position = [240, y_position]
        else:
            self.position = [-16, y_position]
        if kind == "truck":
            self.width = 49
        else:
            self.width = 21
        self.car_list = []

    def add(self, car):
        car.set_car(self.speed, self.position, self.width)  # 자동차를 초기화하고 리스트에 넣기
        self.car_list.append(car)

    def is_fit(self, counter):      # counter로 일정 시간마다 객체 만들기
        if(counter % self.frequence == 0):
            return True
        return False

    def return_car(self, index):    # 범위에서 벗어난 자동차 객체 반환
        return self.car_list.pop(index)
    
    def out_of_range(self):
        for i in range(len(self.car_list)):
            if(self.car_list[i].out_of_range(240)):
                return i    # out of Range
        return -1           # 범위를 벗어난 차는 없다.

    def move_object(self):
        for car in self.car_list:
            car.move()

    def collision_check(self, frogger_position):
        for car in self.car_list:
            if(car.collision_check(frogger_position)):
                return True
        return False

    def speed_up(self):
        if self.speed > 0:
            self.speed += 1
        else:
            self.speed -= 1
        for car in self.car_list:
            car.speed = self.speed