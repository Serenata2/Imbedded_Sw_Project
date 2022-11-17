from PIL import Image, ImageDraw, ImageFont
import time
import random
from colorsys import hsv_to_rgb
from Character import Froggy
from Joystick import Joystick

def main():
    joystick = Joystick()
    my_image = Image.new("RGB", (joystick.width, joystick.height))
    my_draw = ImageDraw.Draw(my_image)
    my_draw.rectangle((0, 0, joystick.width, joystick.height), fill=(255, 0, 0, 100)) # 빨간 화면

    background = Image.open(r"/home/kau-esw/esw/gitHub/ImbeddedSwProject/CrossyRoad/image/frogger_background.png")
    move1 = Image.open(r"/home/kau-esw/esw/gitHub/ImbeddedSwProject/CrossyRoad/image/frogup1.png")
    move2 = Image.open(r"/home/kau-esw/esw/gitHub/ImbeddedSwProject/CrossyRoad/image/frogup2.png")
    src = Image.open(r"/home/kau-esw/esw/gitHub/ImbeddedSwProject/CrossyRoad/image/New Piskel.png")
    joystick.disp.image(my_image)
    # 잔상이 남지 않는 코드
    froggy = Froggy(joystick.width, joystick.height)
    my_draw.rectangle((0, 0, joystick.width, joystick.height), fill = (255, 255, 255, 100))
    while True:
        command = None
        if not joystick.button_U.value:  # up pressed
            command = 'up_pressed'

        elif not joystick.button_D.value:  # down pressed
            command = 'down_pressed'

        elif not joystick.button_L.value:  # left pressed
            command = 'left_pressed'

        elif not joystick.button_R.value:  # right pressed
            command = 'right_pressed'
        
        elif not joystick.button_A.value: # A pressed
            command = 'up_pressed'

        else:
            command = None
        
        froggy.move(command)

    #그리는 순서가 중요합니다. 배경을 먼저 깔고 위에 그림을 그리고 싶었는데 그림을 그려놓고 배경으로 덮는 결과로 될 수 있습니다.
    #좌표는 동그라미의 왼쪽 위, 오른쪽 아래 점 (x1, y1, x2, y2)
        src.paste(background)
        angle = froggy.rotateAngle()
        if(froggy.moving):
            src.paste(move2.rotate(angle), tuple(froggy.position))
        else:
            src.paste(move1.rotate(angle), tuple(froggy.position))
        joystick.disp.image(src)
        print(froggy.position)
        time.sleep(0.01)


if __name__ == '__main__':
    main()