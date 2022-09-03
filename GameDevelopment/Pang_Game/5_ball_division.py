from tkinter import CENTER
import pygame
import os

pygame.init() 
 
# 화면 크기 설정
screen_width = 640  # 가로 크기
screen_height = 480 # 세로 크기
screen = pygame.display.set_mode((screen_width,screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Pang Game") #게임 이름

clock = pygame.time.Clock()

# 1. 사용자 초기화
current_path = os.path.dirname(__file__) # 현재 파일의 위치 반환
image_path = os.path.join(current_path,"img") # image 폴더 위치 반환

# 배경 만들기
background = pygame.image.load(os.path.join(image_path, "background.jpg"))

# 스테이지 만들기
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1]

# 캐릭터 만들기
character = pygame.image.load(os.path.join(image_path, "character.jpg"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - stage_height - character_height

# 캐릭터 이동
character_to_x = 0
character_speed = 0.6

# 무기 만들기
weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

#무기는 한번에 여러발 발사가능
weapons = []

#무기 발사 속도
weapon_speed = 5

#공 만들기
ball_images = [
    pygame.image.load(os.path.join(image_path, "ball1.png")),
    pygame.image.load(os.path.join(image_path, "ball2.png")),
    pygame.image.load(os.path.join(image_path, "ball3.png"))]

#공 크기에 따른 최초 스피드
ball_speed_y = [-17, -15, -12, -9]

# 공들 
balls = []

balls.append({
    "pos_x" : 50, #공의 x 좌표
    "pos_y" : 50, #공의 Y 좌표
    "img_idx" : 0,#공 이미지 인덱스
    "to_x" : 3,
    "to_y": -6,
    "init_spd_y": ball_speed_y[0]}) #최초 속도

# 사라질 무기, 공 정보 저장 변수
weapon_to_remove = -1
ball_to_remove = -1


# 폰트 정의
game_font = pygame.font.Font(None, 40) # 폰트 객체 생성(폰트, 크기)

# 게임 시간
total_time = 100
start_ticks =pygame.time.get_ticks()

#게임 종료 메시지
game_result = "GAME OVER"

running = True #게임이 진행중인가?
while running:

    dt = clock.tick(60) # 게임 화면의 초당 프레임 수를 설정

    print("fps : " + str(clock.get_fps())) # 게임화면의 프레임 수를 확인

    for event in pygame.event.get():  # 어떤 이벤트가 발생하였는가
        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트가 발생하였는가?
            running = False  # 게임이 진행중이 아님
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                character_to_x += character_speed
            elif event.key == pygame.K_SPACE:
                weapon_x_pos = character_x_pos + (character_width/2) -(weapon_width/2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos,weapon_y_pos])
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x  = 0

        
    if character_x_pos < 0:
            character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
            character_x_pos = screen_width - character_width

    character_x_pos += character_to_x * dt

    weapons = [ [ w[0],w[1] - weapon_speed ] for w in weapons if w[1] > -2 ]

    #공 위치 정의
    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        ball_size = ball_images[ball_img_idx].get_rect().size
        ball_width= ball_size[0]
        ball_height = ball_size[1]

        #가로 벽에 닿았을때 공 이동 위치 변경
        if ball_pos_x < 0 or ball_pos_x > screen_width - ball_width:
            ball_val["to_x"] = ball_val["to_x"]* -1

        #스테이지에 튕겨서 올라가는 처리
        if ball_pos_y > screen_height - stage_height - ball_height:
            ball_val["to_y"] = ball_val["init_spd_y"]
        else: #그 외에는 속도를 증가
            ball_val["to_y"] += 0.6 

        ball_val["pos_x"]+= ball_val["to_x"]
        ball_val["pos_y"]+= ball_val["to_y"]


    # 충돌처리
    character_rect= character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos
    
    
    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        # 공과 캐릭터 충돌처리
        ball_rect= ball_images[ball_img_idx].get_rect()
        ball_rect.left = ball_pos_x
        ball_rect.top = ball_pos_y
        if character_rect.colliderect(ball_rect):
            running = False
            break

    # 공과 무기들 충돌 처리
    for weapon_idx, weapon_val in enumerate(weapons):
        weapon_x_pos = weapon_val[0]
        weapon_y_pos = weapon_val[1]

        #무기 reck 정보 업데이트
        weapon_reck = weapon.get_rect()
        weapon_reck.left = weapon_x_pos
        weapon_reck.top = weapon_y_pos

        # 충돌 체크
        if weapon_reck.colliderect(ball_rect):
            weapon_to_remove = weapon_idx #해당무기 없애기 위한 값 설정
            ball_to_remove = ball_idx #해당 공 없애기 위한 값 설정
        
        # 가장 작은 크기의 공이 아니라면 다음 단계의 공으로 나눠주기
            if ball_img_idx < 3 :
                
                #현재 공의 정보를 가지고옴
                ball_width = ball_rect.size[0]
                ball_height = ball_rect.size[1]

                # 나눠진 공 정보
                small_ball_rect = ball_images[ball_img_idx + 1].get_rect()
                small_ball_width = small_ball_rect[0]
                small_ball_height = small_ball_rect[1]

                

                #튕겨나가는공
                balls.append({
                    "pos_x" : ball_pos_x + (ball_width/2) - (small_ball_width /2), #공의 x 좌표
                    "pos_y" : ball_pos_y + (ball_height/2) - (small_ball_height /2), #공의 Y 좌표
                    "img_idx" : ball_img_idx + 1,#공 이미지 인덱스
                    "to_x" :3, 
                    "to_y": -6,
                    "init_spd_y": ball_speed_y[ball_img_idx + 1 ]})
            
                balls.append({
                    "pos_x" : ball_pos_x + (ball_width/2) - (small_ball_width /2), #공의 x 좌표
                    "pos_y" : ball_pos_y + (ball_height/2) - (small_ball_height /2), #공의 Y 좌표
                    "img_idx" : ball_img_idx +1,#공 이미지 인덱스
                    "to_x" :-3, 
                    "to_y": -6,
                    "init_spd_y": ball_speed_y[ball_img_idx + 1 ]})        

        
                break
        
    #충돌된 공 or 무기 없애기
    if ball_to_remove > -1:
        del balls[ball_to_remove]
        ball_to_remove = -1

    if weapon_to_remove > -1:
        del weapons[weapon_to_remove]
        weapon_to_remove = -1



    screen.blit(background, (0,0))

    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos,weapon_y_pos))

    for inx, val in enumerate(balls):
        ball_pos_x = val["pos_x"]
        ball_pos_y = val["pos_y"]
        ball_img_idx = val ["img_idx"]
        screen.blit(ball_images[ball_img_idx],(ball_pos_x , ball_pos_y))
    screen.blit(stage, (0,screen_height - stage_height))
    
    screen.blit(character, (character_x_pos,character_y_pos))
    #경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    timer = game_font.render("Time : {}".format(int(total_time - elapsed_time)),True,(255,255,255))


    # 시간 초과했다면
    if total_time - elapsed_time < 0:
        game_result = "TIME OVER"
        running = False
    pygame.display.update() #게임화면을 다시 그리기

#게임 오버 메시지
msg = game_font.render(game_result,True,(255,255,0))
msg_rect = msg.get_rect(CENTER=(int(screen_width /2 ),int(screen_height / 2)))

pygame.display.update()
    
    
    

