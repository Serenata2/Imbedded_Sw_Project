from PIL import Image, ImageDraw, ImageFont
from GameManager import GameManager
from colorsys import hsv_to_rgb

def main():
    
    gameManager = GameManager()
    gameManager.start_draw()        # 시작화면 그리기
    while True:
        gameManager.input_data()
        if gameManager.command == "B_pressed":
            break
    
    while True:
        
        # 종료 조건 검사
        if(gameManager.end_condition_check()):
            gameManager.last_draw()   # 종료화면 그리기
            print("end!")   
            break 
        gameManager.input_data()     # 조이스틱 입력 받기
        gameManager.move_objects()   # 조이스틱 입력에 따라 frogger, 다른 객체들 움직이기
        gameManager.draw()          # 화면 그리기

if __name__ == '__main__':
    main()