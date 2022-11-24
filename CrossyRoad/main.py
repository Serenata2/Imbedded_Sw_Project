from PIL import Image, ImageDraw, ImageFont
import time
import random
from GameManager import GameManager
from colorsys import hsv_to_rgb
from Character import Froggy
from Joystick import Joystick

def main():
    
    gameManager = GameManager()

    while True:
        
        if(gameManager.endConditionCheck()):
            gameManager.drawEnd()
            print("end!")
            break
        gameManager.inputData()
        gameManager.moveObjects()
    #그리는 순서가 중요합니다. 배경을 먼저 깔고 위에 그림을 그리고 싶었는데 그림을 그려놓고 배경으로 덮는 결과로 될 수 있습니다.
    #좌표는 동그라미의 왼쪽 위, 오른쪽 아래 점 (x1, y1, x2, y2)
        gameManager.draw()

if __name__ == '__main__':
    main()