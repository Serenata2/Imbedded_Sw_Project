from PIL import Image, ImageDraw, ImageFont
from colorsys import hsv_to_rgb
from Frogger import Frogger
from Joystick import Joystick
from Snake import Snake

from ObjectManager import ObjectManager

class GameManager:
        def __init__(self):
            self.joystick = Joystick()
            self.frogger = Frogger(self.joystick.width, self.joystick.height)   # frogger 객체
            self.snake_list = []    # snake 객체 리스트
            self.object_manager = ObjectManager()   # ObjectManager 객체
            self.command = None
            self.my_image = Image.open(r"/home/kau-esw/esw/gitHub/ImbeddedSwProject/CrossyRoad/image/New Piskel.png")
            self.flag = 0           # 나중에 배경화면을 그릴 때 물결치는 부분 구현하기 위해서
            self.success_list = {0:0, 112:0, 224:0} # 목표물의 위치의 x 값을 key로, 도착여부를 value로 가지고 있는 딕셔너리
            self.success_image = Image.open(r"/home/kau-esw/esw/gitHub/ImbeddedSwProject/CrossyRoad/image/succed_froggy_image.png")
            self.first_image = Image.open(r"/home/kau-esw/esw/gitHub/ImbeddedSwProject/CrossyRoad/image/New Piskel.png")
            self.life_image = Image.open(r"/home/kau-esw/esw/gitHub/ImbeddedSwProject/CrossyRoad/image/life.png")
            self.frogger_image_list = []
            for i in range(1,4):
                self.frogger_image_list.append(Image.open(r"/home/kau-esw/esw/gitHub/ImbeddedSwProject/CrossyRoad/image/frogup"+str(i)+".png"))
            self.snake_image_list = []
            for i in range(1,3):
                self.snake_image_list.append(Image.open(r"/home/kau-esw/esw/gitHub/ImbeddedSwProject/CrossyRoad/image/snake"+str(i)+".png"))
            self.background_list = []
            for i in range(1,3):
                self.background_list.append(Image.open(r"/home/kau-esw/esw/gitHub/ImbeddedSwProject/CrossyRoad/image/background"+str(i)+".png"))
            self.car_image = {}
            self.car_image["truck"] = Image.open(r"/home/kau-esw/esw/gitHub/ImbeddedSwProject/CrossyRoad/image/trcuk.png")
            self.car_image["sport_car"] = Image.open(r"/home/kau-esw/esw/gitHub/ImbeddedSwProject/CrossyRoad/image/sport_car.png")
            self.log_image = {}
            self.log_image["short"] = Image.open(r"/home/kau-esw/esw/gitHub/ImbeddedSwProject/CrossyRoad/image/log_short.png")
            self.log_image["long"] = Image.open(r"/home/kau-esw/esw/gitHub/ImbeddedSwProject/CrossyRoad/image/log_long.png")
            self.timer_image = Image.open(r"/home/kau-esw/esw/gitHub/ImbeddedSwProject/CrossyRoad/image/timer.png")
            self.counter = 0    # 자체적인 카운터
            self.score = 0      # 이 게임 내에서 점수
            self.max_length = 224       # frogger가 앞으로 전진할 때마다 점수를 얻게 하기 위한 변수
            self.state_changed = True   # 목표물에 도달하거나 frogger가 죽었을 때 True값으로 변경해서 다양한 작업 하도록 하는 변수
            self.timer_length = 80      # timer의 길이
            

        def end_condition_check(self):  # 종료 조건 확인하는 함수
            if(self.frogger.life <= 0):
                return True
            num = 0
            for i in self.success_list:
                if(self.success_list[i]):
                    num += 1
            if num <= 2:
                if num == 1 and len(self.snake_list) == 0:
                    self.snake_list.extend([Snake(208), Snake(112)])
                return False
            return True

        def input_data(self):
            self.command = None
            if not self.joystick.button_U.value:  # up pressed
                self.command = 'up_pressed'

            elif not self.joystick.button_D.value:  # down pressed
                self.command = 'down_pressed'

            elif not self.joystick.button_L.value:  # left pressed
                self.command = 'left_pressed'

            elif not self.joystick.button_R.value:  # right pressed
                self.command = 'right_pressed'
        
            elif not self.joystick.button_A.value: # A pressed
                self.command = 'up_pressed'

            elif not self.joystick.button_B.value: # B pressed
                self.command = 'B_pressed'

            else:
                self.command = None

            
            
        def move_objects(self):                     # 객체들을 움직이는 함수(frogger, 자동차, 통나무, 뱀)
            self.frogger.move(self.command)
            self.counter = (self.counter % 100000)
            self.object_manager.update_objects(self.counter)
            self.counter += 1
            # 자동차, 통나무 움직이기, 통나무에 탔을 때를 알기 위해서 frogger의 좌표값을 인자로 넣기
            self.object_manager.move_objects(self.frogger.position)  
            snake_collision_check = False
            if self.frogger.position[1] < self.max_length:  # 앞으로 전진했는지 확인
                self.max_length -= 16
                self.score += 2

            for snake in self.snake_list:   # 뱀들을 움직이고
                snake.move()
            for snake in self.snake_list:   # 뱀과의 충돌이 있는지 확인
                snake_collision_check = snake.collision_check(self.frogger.position)
                if snake_collision_check:
                    break
            
            if snake_collision_check:
                self.reset_objects()
                self.frogger.died()
            elif(self.object_manager.collision_check(self.frogger.position)):
                self.reset_objects()
                self.frogger.died()
            elif(self.frogger.position[1] == 0):
                if(self.frogger.position[0] + 8 <= 24):
                    if self.success_list[0] == False:
                        self.score += 100       # 성공 점수 추가
                        self.score += self.timer_length  # 시간 점수 추가
                    else:
                        self.score -= 28        # 무한 점수 반복 막기 위해서
                    self.success_list[0] = True
                    self.frogger.succed()
                    self.object_manager.speed_up_objects()
                elif(108 <= self.frogger.position[0] + 8 <= 132):
                    if self.success_list[112] == False:
                        self.score += 100       # 성공 점수 추가
                        self.score += self.timer_length  # 시간 점수 추가
                    else:
                        self.score -= 28        # 무한 점수 반복 막기 위해서
                    self.success_list[112] = True
                    self.frogger.succed()
                    self.object_manager.speed_up_objects()
                elif(self.frogger.position[0] + 8 >= 216):
                    if self.success_list[224] == False:
                        self.score += 100
                        self.score += self.timer_length  # 시간 점수 추가
                    else:
                        self.score -= 28        # 무한 점수 반복 막기 위해서
                    self.success_list[224] = True
                    self.frogger.succed()
                    self.object_manager.speed_up_objects()
                else:
                    self.frogger.died()
                self.reset_objects()
        

        def start_draw(self):
            # Create blank image for drawing.
            # Make sure to create image with mode 'RGB' for color.
            image = Image.new("RGB", (self.joystick.width, self.joystick.height))

            # Get drawing object to draw on image.
            draw = ImageDraw.Draw(image)
            draw.rectangle((0, 0, self.joystick.width, self.joystick.height), outline=0, fill=(0,0,128))
            fnt = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 30)
            draw.text((60, 100), "Press B \nto Start", font=fnt, fill=(255, 255, 255))
            self.joystick.disp.image(image)



        def draw(self):
            self.my_image.paste(self.background_list[int((self.flag) % 8 / 4)])     # 배경 그리기
            self.flag = (self.flag + 1) % 8

            for road in self.object_manager.road_list:   # 자동차들 그리기
                for car in road.car_list:
                    self.my_image.paste(self.car_image[road.kind], tuple(car.position), self.car_image[road.kind])
            
            for river in self.object_manager.river_list: # 통나무들 그리기
                for log in river.log_list:
                    self.my_image.paste(self.log_image[river.kind], tuple(log.position), self.log_image[river.kind])

            angle = self.frogger.rotate_angle()         # frogger 그리기
            i = self.frogger.condition()
            self.my_image.paste(self.frogger_image_list[i].rotate(angle), tuple(self.frogger.position), self.frogger_image_list[i].rotate(angle))

            for i in range(self.frogger.life):          # 목숨 그리기
                self.my_image.paste(self.life_image, tuple([i * 16, self.joystick.height - 16]), self.life_image)

            for i in self.success_list:
                if self.success_list[i] == True:        # 통과한 목표지점 그리기
                    self.my_image.paste(self.success_image, tuple([i, 0]), self.success_image)
            
            if self.state_changed == True:              # frogger가 원래 위치로 초기화되었다면 타이머도 초기화
                self.state_changed = False
                self.timer_length = 80

            self.my_image.paste(self.timer_image.resize(tuple([self.timer_length, 12])), tuple([160, 226])) # 타이머 그리기
            if self.counter % 3 == 0 :                  # 자체적인 counter를 이용해서 줄이기
                self.timer_length -= 1
            if self.timer_length == 0:
                self.frogger.died()
                self.reset_objects()

            for snake in self.snake_list:               # Snake 그리기
                flag = snake.transfer_check()
                if flag:
                    self.my_image.paste(self.snake_image_list[self.counter%2].transpose(Image.FLIP_LEFT_RIGHT), tuple(snake.position), self.snake_image_list[self.counter%2].transpose(Image.FLIP_LEFT_RIGHT))
                else:
                    self.my_image.paste(self.snake_image_list[self.counter%2], tuple(snake.position), self.snake_image_list[self.counter%2])

            draw = ImageDraw.Draw(self.my_image)        # 실시간 점수 그리기
            fnt = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 16)
            draw.text((80, 224), "score {}".format(self.score), font=fnt, fill=(255, 255, 255))
            self.joystick.disp.image(self.my_image)

        def last_draw(self):
            for i in range(240, -8, -4):    # 점점 화면이 닫혀가게 그림 그리기
                self.my_image.paste(self.first_image.resize((244-i, 240)), tuple([i, 0]))
                self.joystick.disp.image(self.my_image)
            self.score += self.frogger.life * 100
            draw = ImageDraw.Draw(self.my_image)
            fnt = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 25)
            if self.frogger.life == 0:
                draw.text((60, 100), "You Lose..", font=fnt, fill=(255, 0, 0))
            else:
                draw.text((60, 100), "You Win!!", font=fnt, fill=(255, 255, 0))
            draw.text((20, 150), "Your score : {}".format(self.score), font=fnt, fill=(255, 255, 255))
            self.joystick.disp.image(self.my_image)     # 최종 점수 그리기

        def reset_objects(self):            # frogger가 죽거나 성공해서 다시 돌아올 경우
            for snake in self.snake_list:    # snake, state_changed, max_length 초기화
                snake.reset_snake()
            self.state_changed = True
            self.max_length = 224
