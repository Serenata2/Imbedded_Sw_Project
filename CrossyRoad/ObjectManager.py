import random
from colorsys import hsv_to_rgb
from Road import Road
from River import River
from ObjectPool import ObjectPool

class ObjectManager:
    def __init__(self):
        self.obejectPool = ObjectPool()
        self.road_list = []
        self.river_list = []
        for i in range(5):
            if(i%2 == 0):
                self.road_list.append(Road((192 - (16*i)), -4, random.randint(25,40), "truck"))
                self.river_list.append(River((96 - (16*i)), -random.randint(2,4), random.randint(35,60), "short"))
            else:
                self.road_list.append(Road((192 - (16*i)), 8, random.randint(35, 60), "sport_car"))
                self.river_list.append(River((96 - (16*i)), random.randint(5,6), random.randint(30 ,40), "long"))
        self.river_list.append(River(16, 2, 70, "long"))


    def update_objects(self, counter):  # 만약에 주기를 만족한다면 큐에서 Car,Log 객체를 빼고 추가
        for road in self.road_list:
            if(road.is_fit(counter)):   
                road.add(self.obejectPool.post_car())        
        for river in self.river_list:
            if(river.is_fit(counter)):
                river.add(self.obejectPool.post_log())


    # 자동차, 통나무 객체들을 움직이는 함수
    def move_objects(self, froggy_position):
        for road in self.road_list:
            road.move_object()
            i = road.out_of_range()
            if(i != -1):
                self.obejectPool.return_car(road.return_car(i))

        for river in self.river_list:
            river.move_object()
            if froggy_position[1] == river.position[1]:
                froggy_position[0] += river.speed
            i = river.out_of_range()
            if(i != -1):
                self.obejectPool.return_log(river.return_log(i))


    # 자동차, 강과 충돌이 일어났는 지 확인하는 함수
    def collision_check(self, froggyPos):
        for road in self.road_list:
            if(road.collision_check(froggyPos)):
                return True
        for river in self.river_list:
            if(river.collision_check(froggyPos)):
                return True
        return False


    def speed_up_objects(self):
        for road in self.road_list:
            road.speed_up()

        for river in self.river_list:
            river.speed_up()