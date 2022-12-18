from Car import Car
from Log import Log

class ObjectPool:
    def __init__(self):
        self.storage_car = [Car() for _ in range(10)]
        self.storage_log = [Log() for _ in range(10)]

    def creat_car(self):    # 객체가 부족하면 더 만들어서 풀에 넣기
        for i in range(5):
            self.storage_car.append(Car())
        
    def post_car(self):     # 객체를 풀에서 전달해 주기
        if(len(self.storage_car) <= 0):
            self.creat_car()
        return self.storage_car.pop(0)
    
    def return_car(self, car):  # 객체를 받아서 풀에 다시 넣기
        self.storage_car.append(car)

    def creat_log(self):    # 객체가 부족하면 더 만들어서 풀에 넣기
        for i in range(5):
            self.storage_log.append(Log())
        
    def post_log(self):     # 객체를 풀에서 전달해 주기
        if(len(self.storage_log) <= 0):
            self.creat_log()
        return self.storage_log.pop(0)
    
    def return_log(self, log):  # 객체를 받아서 풀에 다시 넣기
        self.storage_log.append(log)


