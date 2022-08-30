import pygame
################################################
#기본 초기화 (반드시 해야하는 것들)
pygame.init() 
 
# 화면 크기 설정
screen_width = 480  # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width,screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Py Game") #게임 이름

#fps
clock = pygame.time.Clock()
################################################

################################################
# 1. 사용자 게임 초기화 (배경화면, 게임이미지, 좌표, 속도,폰트)
# 배경 이미지 불러오기
background = pygame.image.load("C:/Users/jongseoung/Documents/Python/GameDevelopment/pygame_basic/background.png")

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("C:/Users/jongseoung/Documents/Python/GameDevelopment/pygame_basic/character.jpg")
character_size = character.get_rect().size  # 이미지의 크기를 구해옴
character_width = character_size[0]  # 캐릭터의 가로크기
character_height = character_size[1]  # 캐릭터의 세로 크기
character_x_pos = (screen_width / 2) - (character_width / 2)  # 화면 가로의 절반 크기에 해당하는 곳에 위치
character_y_pos = screen_height - character_height  # 화면 세로 크기 가장 아래에 해당하는 곳에 위치

# 이동할 좌표
to_x = 0
to_y = 0

# 이동 속도
character_speed = 0.6

# enemy 캐릭터
enemy = pygame.image.load("C:/Users/jongseoung/Documents/Python/GameDevelopment/pygame_basic/enemy.png")
enemy_size = enemy.get_rect().size  # 이미지의 크기를 구해옴
enemy_width = enemy_size[0]  # 캐릭터의 가로크기
enemy_height = enemy_size[1]  # 캐릭터의 세로 크기
enemy_x_pos = (screen_width / 2) - (enemy_width / 2)  # 화면 가로의 절반 크기에 해당하는 곳에 위치
enemy_y_pos = (screen_height / 2) - ( enemy_height /2 ) # 화면 세로 크기 가장 아래에 해당하는 곳에 위치

# 폰트 정의
game_font = pygame.font.Font(None, 40) # 폰트 객체 생성(폰트, 크기)

# 총시간
total_time = 10

#시작 시간 계산
start_ticks = pygame.time.get_ticks()

################################################


# 이벤트 루프
running = True #게임이 진행중인가?
while running:

    dt = clock.tick(60) # 게임 화면의 초당 프레임 수를 설정

    print("fps : " + str(clock.get_fps())) # 게임화면의 프레임 수를 확인
################################################
    # 2.이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():  # 어떤 이벤트가 발생하였는가
        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트가 발생하였는가?
            running = False  # 게임이 진행중이 아님

        if event.type == pygame.KEYDOWN: # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT: # 캐릭터를 왼쪽으로 이동
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT: # 캐릭터를 오른쪽으로 이동
                to_x += character_speed
            elif event.key == pygame.K_UP: # 캐릭터를 위쪽으로 이동
                to_y += character_speed
            elif event.key == pygame.K_DOWN: # 캐릭터를 아래쪽으로 이동
                to_y -= character_speed

        if event.type == pygame.KEYUP: # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x= 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y= 0
################################################
    #. 게임 캐릭터 위치 정의
    character_x_pos += to_x *dt
    character_y_pos -= to_y *dt

    
    # 가로 경계값 처리
    if character_x_pos < 0 :
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 세로 경계값 처리
    if character_y_pos < 0 :
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

################################################
    # 4. 충돌 처리
    #충돌 처리
    character_rect= character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    #충돌 체크
    if character_rect.colliderect(enemy_rect):
        print("충돌 했습니다.")
        running = False

    screen.blit(background, (0,0)) # 배경 그리기
    # screen.fill(0, 0, 255) # RGB를 이용하여 배경 채우기

################################################
    # 5. 화면에 그리기
    elapsed_time = (pygame.time.get_ticks()- start_ticks) / 1000  # 경과 시간(ms)을 1000으로 나누어서 초 단위로 표시
    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255,255,255))

    screen.blit(character, (character_x_pos, character_y_pos)) #캐릭터 그리기
    screen.blit(enemy , (enemy_x_pos,enemy_y_pos))
    screen.blit(timer,(10,10))

    # 만약 시간이 10 이하이면 게임 종료
    if total_time - elapsed_time <= 0:
        print("타임 아웃")
        running = False
    pygame.display.update() #게임화면을 다시 그리기

#잠시 대기
pygame.time.delay(2000) # 2초정도 대기
# Py Game 종료
pygame.quit()