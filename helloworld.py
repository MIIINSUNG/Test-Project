

    
#import sys
#print("Phython", "Java", file=sys.stdout)
#print("Phython", "Java", file=sys.stderr)

#Test Result 
scores = {"MATH":0, "ENGLISH":50, "CODING":100}
for subject, score in scores.items():
    #print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=":")

import pygame

pygame.init() # 초기화 (반드시 필요)

#화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Nado Game") # 게임 이름
\pip
# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        running = False # 게임이 진행중이 아님

    # pygame 종료
    pygame.quit()








